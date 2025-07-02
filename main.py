import hashlib

def md5_from_text(text):
    return hashlib.md5(text.encode()).hexdigest()

def md5_from_file(file_path):
    if not os.path.isfile(file_path):
        return None, "File tidak ditemukan."
    with open(file_path, "rb") as f:
        data = f.read()
        hash_result = hashlib.md5(data).hexdigest()
    return hash_result, None

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

    elif choice == '2':
        text = input("Masukkan teks asli: ")
        md5_hash = input("Masukkan hash MD5: ")
        if compare_md5(text, md5_hash):
            print("✅ Teks cocok dengan hash MD5!")
        else:
            print("❌ Teks TIDAK cocok dengan hash MD5.")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
