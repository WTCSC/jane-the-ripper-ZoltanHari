import pytest
import hashlib
from jane_the_ripper import crack_passwords, validate_path_to_files, validate_hash_type

def test_valid_wordlist():
    assert validate_path_to_files("wordlist.txt") == True

def test_valid_hashes():
    assert validate_path_to_files("hashes_md5.txt") == True

def test_invalid_wordlist():
    assert validate_path_to_files("notwordlist.txt") == False

def test_invalid_hashes():
    assert validate_path_to_files("nothashes.txt") == False

def test_valid_hash_type():
    assert validate_hash_type("md5") == True

def test_valid_hash_type():
    assert validate_hash_type("sha1") == True

def test_valid_hash_type():
    assert validate_hash_type("sha256") == True

def test_invalid_hash_type():
    assert validate_hash_type("crc32") == False

def test_crack_passwords_md5(tmp_path):
    """
    Test that crack_passwords correctly finds passwords that match the given MD5 hashes.
    """

    wordlist_file = tmp_path / "wordlist.txt"
    wordlist_file.write_text("password\nhello\nadmin\n")

    correct_hash = hashlib.md5("hello".encode()).hexdigest()
    wrong_hash = hashlib.md5("wrongpass".encode()).hexdigest()

    hashes_file = tmp_path / "hashes.txt"
    hashes_file.write_text(f"{correct_hash}\n{wrong_hash}\n")

    cracked, hashes_list = crack_passwords(str(wordlist_file), str(hashes_file), "md5")

    assert correct_hash in cracked
    assert cracked[correct_hash] == "hello"

    assert wrong_hash not in cracked

    assert correct_hash in hashes_list
    assert wrong_hash in hashes_list


def test_crack_passwords_sha1(tmp_path):
    """
    Test the same logic, but with SHA1 hashing.
    """
    wordlist_file = tmp_path / "wordlist.txt"
    wordlist_file.write_text("apple\nbanana\ncarrot\n")

    correct_hash = hashlib.sha1("banana".encode()).hexdigest()
    hashes_file = tmp_path / "hashes.txt"
    hashes_file.write_text(f"{correct_hash}\n")

    cracked, _ = crack_passwords(str(wordlist_file), str(hashes_file), "sha1")

    assert correct_hash in cracked
    assert cracked[correct_hash] == "banana"

def test_crack_passwords_sha1(tmp_path):
    """
    Test the same logic, but with SHA256 hashing.
    """
    wordlist_file = tmp_path / "wordlist.txt"
    wordlist_file.write_text("apple\nbanana\ncarrot\n")

    correct_hash = hashlib.sha256("banana".encode()).hexdigest()
    hashes_file = tmp_path / "hashes.txt"
    hashes_file.write_text(f"{correct_hash}\n")

    cracked, _ = crack_passwords(str(wordlist_file), str(hashes_file), "sha256")

    assert correct_hash in cracked
    assert cracked[correct_hash] == "banana"