import hashlib

def main():
    print("\nWeclome Ginats\n")
    while True:
        path_to_wordlist = input("Enter the path to your wordlist: ").strip()
        try:
            with open(path_to_wordlist, "r"):
                break
        except FileNotFoundError:
            print("Invalid wordlist file")
    while True:
        path_to_hashes = input("Enter the path to your hashes: ").strip()
        try:
            with open(path_to_hashes, "r"):
                break
        except FileNotFoundError:
            print("Invalid hashes file")
    fin_hash, set = crack_passwords(path_to_wordlist, path_to_hashes)
    print()
    for hash in set:
        if hash in fin_hash:
            print(f"[+] Cracked: {hash} --> '{fin_hash[hash]}'")
        else:
            print(f"[-] Failed: {hash} ")

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
        for line in wordlist:
            password = line.rstrip("\n")
            hash = hashlib.md5(password.encode()).hexdigest()
            if hash in hashes_set and hash not in cracked:
                cracked[hash] = password

    return cracked, hashes_list

if __name__ == "__main__":
    main()
