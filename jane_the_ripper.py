import hashlib

import sys 
import time

def type_out(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def crack_passwords(wordlist_path, hash_file_path):
    hashes_list = []
    with open(hash_file_path, "r") as hashes:
        for line in hashes:
            hash = line.strip()
            if hash:
                hashes_list.append(hash)
    hashes_set = set(hashes_list)
    cracked = {}
    with open(wordlist_path, "r") as wordlist:
        while True:
            match hash_type:
                case "md5":
                    for line in wordlist:
                        password = line.rstrip("\n")
                        hash = hashlib.md5(password.encode()).hexdigest()
                        if hash in hashes_set and hash not in cracked:
                            cracked[hash] = password
                case "sha1":
                        for line in wordlist:
                            password = line.rstrip("\n")
                            hash = hashlib.sha1(password.encode()).hexdigest()
                            if hash in hashes_set and hash not in cracked:
                                cracked[hash] = password
                case "sha256":
                        for line in wordlist:
                            password = line.rstrip("\n")
                            hash = hashlib.sha256(password.encode()).hexdigest()
                            if hash in hashes_set and hash not in cracked:
                                cracked[hash] = password
                case _:
                    return False

    return cracked, hashes_list

def validate_path_to_files(file):
    try:
        with open(file, "r"):
            return True
    except FileNotFoundError:
        return False
    
if __name__ == "__main__":
    type_out("\nWelcome Jane the Ripper\n")
    while True:
        type_out("Enter the path to your wordlist: ")
        path_to_wordlist = input().strip()
        invalid_wordlist = validate_path_to_files(path_to_wordlist)
        if invalid_wordlist == False:
            type_out("Invalid wordlist file")
        else:
            break
    while True:
        type_out("Enter the path to your hashes: ")
        path_to_hashes = input().strip()
        invalid_hashes = validate_path_to_files(path_to_hashes)
        if invalid_hashes == False:
            type_out("Invalid hashes file")
        else:
            break
        type_out("Please enter the hash type (md5, sha1, sha256)")
        hash_type = input().strip().lower()
        invalid_hash_type = crack_passwords
        if invalid_hash_type ==  False:
            type_out("Invalid hash type")
        else:
            break
    fin_hash, set = crack_passwords(path_to_wordlist, path_to_hashes)
    print()
    for hash in set:
        if hash in fin_hash:
            print(f"[+] Cracked: {hash} --> '{fin_hash[hash]}'")
        else:
            print(f"[-] Failed: {hash} ")

