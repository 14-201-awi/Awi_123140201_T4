def tampilkan_menu():
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")

def tampilkan_tugas(tugas_list):
    if not tugas_list:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for i, tugas in enumerate(tugas_list, 1):
            print(f"{i}. {tugas}")

def main():
    daftar_tugas = []

    while True:
        tampilkan_menu()
        try:
            pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()
            if pilihan not in ['1', '2', '3', '4']:
                raise ValueError("Pilihan tidak valid. Harap masukkan 1, 2, 3, atau 4.")

            if pilihan == '1':
                tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
                if not tugas:
                    raise ValueError("Tugas tidak boleh kosong.")
                daftar_tugas.append(tugas)
                print("Tugas berhasil ditambahkan!")

            elif pilihan == '2':
                if not daftar_tugas:
                    print("Tidak ada tugas untuk dihapus.")
                    continue
                tampilkan_tugas(daftar_tugas)
                try:
                    nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                    if nomor < 1 or nomor > len(daftar_tugas):
                        raise IndexError(f"Tugas dengan nomor {nomor} tidak ditemukan.")
                    hapus = daftar_tugas.pop(nomor - 1)
                    print(f"Tugas '{hapus}' berhasil dihapus.")
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka.")
                except IndexError as e:
                    print(f"Error: {e}")

            elif pilihan == '3':
                tampilkan_tugas(daftar_tugas)

            elif pilihan == '4':
                print("Keluar dari program.")
                break

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
