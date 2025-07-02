import hashlib

def generate_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def compare_md5(text, hash_to_compare):
    return generate_md5(text) == hash_to_compare.lower()

def main():
    print("=== TOOLS ENKRIPSI MD5 PYTHON ===")
    print("1. Enkripsi teks ke MD5")
    print("2. Cek apakah teks cocok dengan hash MD5")
    choice = input("Pilih menu (1/2): ")

    if choice == '1':
        text = input("Masukkan teks yang ingin dienkripsi: ")
        hash_result = generate_md5(text)
        print(f"MD5 Hash: {hash_result}")

if __name__ == "__main__":
    main()
