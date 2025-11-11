import pytest
import hashlib
from jane_the_ripper import crack_passwords, validate_path_to_files, validate_hash_type

def test_valid_wordlist():
    """
    Test that a valid wordlist file path returns True
    """
    assert validate_path_to_files("text_files/wordlist.txt") == True

@pytest.mark.parametrize("valid_hashes", ["text_files/hashes_md5.txt", "text_files/hashes_sha1.txt", "text_files/hashes_sha256.txt"])
def test_valid_hashes(valid_hashes):
    """
    Test that valid hashes file paths return True"""
    assert validate_path_to_files(valid_hashes) is True

def test_invalid_wordlist():
    """
    Test that an invalid wordlist file path returns False
    """
    assert validate_path_to_files("notwordlist.txt") == False

def test_invalid_hashes():
    """
    Test that an invalid hashes file path returns False
    """
    assert validate_path_to_files("nothashes.txt") == False

@pytest.mark.parametrize("hash_type", ["md5", "sha1", "sha256"])
def test_valid_hash_type(hash_type):
    """
    Test that valid hash types return True
    """
    assert validate_hash_type(hash_type) is True

def test_invalid_hash_type():
    """
    Test that an invalid hash type returns False
    """
    assert validate_hash_type("crc32") == False

def test_crack_passwords_md5(tmp_path):
    """
    Test that crack_passwords correctly finds passwords that match the given MD5 hashes.
    """

    wordlist_file = tmp_path / "wordlist.txt"
    wordlist_file.write_text("password\nhello\nadmin\n")

    correct_hash = hashlib.md5("hello".encode()).hexdigest()
    wrong_hash = hashlib.md5("wrongpass".encode()).hexdigest()

    hashes_file = tmp_path / "hashes_md5.txt"
    hashes_file.write_text(f"{correct_hash}\n{wrong_hash}\n")

    cracked, hashes_list = crack_passwords(str(wordlist_file), str(hashes_file), "md5")

    assert correct_hash in cracked
    assert cracked[correct_hash] == "hello"

    assert wrong_hash not in cracked

    assert correct_hash in hashes_list
    assert wrong_hash in hashes_list


def test_crack_passwords_sha1(tmp_path):
    """
    Test that crack_passwords correctly finds passwords that match the given SHA1 hashes.
    """

    wordlist_file = tmp_path / "wordlist.txt"
    wordlist_file.write_text("password\nhello\nadmin\n")

    correct_hash = hashlib.sha1("hello".encode()).hexdigest()
    wrong_hash = hashlib.sha1("wrongpass".encode()).hexdigest()

    hashes_file = tmp_path / "hashes_sha1.txt"
    hashes_file.write_text(f"{correct_hash}\n{wrong_hash}\n")

    cracked, hashes_list = crack_passwords(str(wordlist_file), str(hashes_file), "sha1")

    assert correct_hash in cracked
    assert cracked[correct_hash] == "hello"

    assert wrong_hash not in cracked

    assert correct_hash in hashes_list
    assert wrong_hash in hashes_list

def test_crack_passwords_sha256(tmp_path):
    """
    Test that crack_passwords correctly finds passwords that match the given SHA256 hashes.
    """

    wordlist_file = tmp_path / "wordlist.txt"
    wordlist_file.write_text("password\nhello\nadmin\n")

    correct_hash = hashlib.sha256("hello".encode()).hexdigest()
    wrong_hash = hashlib.sha256("wrongpass".encode()).hexdigest()

    hashes_file = tmp_path / "hashes_sha256.txt"
    hashes_file.write_text(f"{correct_hash}\n{wrong_hash}\n")

    cracked, hashes_list = crack_passwords(str(wordlist_file), str(hashes_file), "sha256")

    assert correct_hash in cracked
    assert cracked[correct_hash] == "hello"

    assert wrong_hash not in cracked

    assert correct_hash in hashes_list
    assert wrong_hash in hashes_list
