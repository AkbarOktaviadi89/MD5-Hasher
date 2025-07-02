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

def save_to_file(content, filename="md5_result.txt"):
    with open(filename, "w") as f:
        f.write(content)
    return filename
def compare_md5(text, hash_to_compare):
    return md5_from_text(text) == hash_to_compare.lower()
def show_menu():
    print("\n====== TOOLS MD5 PYTHON ======")
    print("1. Enkripsi teks ke MD5")
    print("2. Enkripsi file ke MD5")
    print("3. Cek kecocokan teks dengan hash MD5")
    print("4. Keluar")
    print("=" * 33)
def main():
    while True:
        show_menu()
        choice = input("Pilih menu (1/2/3/4): ")

        if choice == '1':
            text = input("Masukkan teks: ")
            result = md5_from_text(text)
            print("MD5 Hash:", result)
            simpan = input("Simpan ke file? (y/n): ").lower()
            if simpan == 'y':
                fname = save_to_file(f"Teks: {text}\nMD5: {result}")
                print(f"Hasil disimpan di: {fname}")

        elif choice == '2':
            file_path = input("Masukkan path file: ")
            result, error = md5_from_file(file_path)
            if error:
                print("❌ Error:", error)
            else:
                print("MD5 Hash:", result)
                simpan = input("Simpan ke file? (y/n): ").lower()
                if simpan == 'y':
                    fname = save_to_file(f"File: {file_path}\nMD5: {result}")
                    print(f"Hasil disimpan di: {fname}")

        elif choice == '3':
            text = input("Masukkan teks asli: ")
            md5_input = input("Masukkan hash MD5: ")
            if compare_md5(text, md5_input):
                print("✅ Cocok! Teks sesuai dengan hash.")
            else:
                print("❌ Tidak cocok.")

        elif choice == '4':
            print("Terima kasih! Keluar...")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
