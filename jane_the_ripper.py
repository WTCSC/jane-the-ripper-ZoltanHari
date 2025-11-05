import hashlib

import sys 
import time

# Function to simulate typing effect instead of just printing it all at once
def type_out(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Bash colors for output to organize cracked and failed hashes
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

def crack_passwords(wordlist_path, hash_file_path, hash_type):
    """
    Crack passwords from a wordlist that match the given hashes
    
    ARGS: 
        wordlist_path (str): Path to the wordlist file
        hash_file_path (str): Path to the file containing hashes
        hash_type (str): Type of hash (md5, sha1, sha256)

    Returns:
        cracked (dict): A dictionary with hashes as keys and cracked passwords as values
        hashes_list (list): A list of all hashes from the hash file

    """

    hashes_list = []
    with open(hash_file_path, "r") as hashes:
        for line in hashes:
            hash = line.strip()
            if hash:
                hashes_list.append(hash)
    # I used a set because it can instantly find any item instead of going through every item in a list one by one
    hashes_set = set(hashes_list)
    cracked = {}
    with open(wordlist_path, "r") as wordlist:
                match hash_type:
                    case "md5":
                        for line in wordlist:
                            password = line.strip()
                            hash = hashlib.md5(password.encode()).hexdigest()
                            if hash in hashes_set and hash not in cracked:
                                cracked[hash] = password
                    case "sha1":
                        for line in wordlist:
                            password = line.strip()
                            hash = hashlib.sha1(password.encode()).hexdigest()
                            if hash in hashes_set and hash not in cracked:
                                cracked[hash] = password
                    case "sha256":
                        for line in wordlist:
                            password = line.strip()
                            hash = hashlib.sha256(password.encode()).hexdigest()
                            if hash in hashes_set and hash not in cracked:
                                cracked[hash] = password

    # Returned list instead of set to maintain order of hashes from the file
    return cracked, hashes_list

# Added error handling outside of main function for better testability
def validate_path_to_files(file):
    try:
        with open(file, "r"):
            return True
    except FileNotFoundError:
        return False
    
def validate_hash_type(hash_type):
    if hash_type == "md5" or hash_type == "sha1" or hash_type == "sha256":
        return True
    else:
        return False
    
if __name__ == "__main__":
    type_out("\nWelcome Jane the Ripper\n")

    while True:
        type_out("Enter the path to your wordlist: ")
        path_to_wordlist = input().strip()
        if not validate_path_to_files(path_to_wordlist):
            type_out("Invalid wordlist file")
        else:
            break

    while True:
        type_out("Enter the path to your hashes: ")
        path_to_hashes = input().strip()
        if not validate_path_to_files(path_to_hashes):
            type_out("Invalid hashes file")
        else:
            break

    while True:
        type_out("Please enter the hash type (md5, sha1, sha256): ")
        hash_type = input().strip().lower()
        if not validate_hash_type(hash_type):
            type_out("Invalid hash type")
        else:
            break

    fin_hash, set = crack_passwords(path_to_wordlist, path_to_hashes, hash_type)
    print()
    for hash in set:
        if hash in fin_hash:
            print(f"{GREEN}[+] Cracked: {hash} --> '{fin_hash[hash]}'{RESET}")
        else:
            print(f"{RED}[-] Failed: {hash}{RESET}")