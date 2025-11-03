import pytest
from jane_the_ripper import crack_passwords, validate_path_to_files, validate_hash_type

def test_valid_wordlist():
    assert validate_path_to_files("wordlist.txt") == True

def test_valid_hashes():
    assert validate_path_to_files("hashes.txt") == True

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
    assert crack_passwords("crc32") == False