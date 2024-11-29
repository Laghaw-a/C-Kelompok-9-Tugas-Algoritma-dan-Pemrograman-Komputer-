# main.py

from add_data import kontak_keluarga, kegiatan_harian, tagihan_bulanan, belanja_bulanan, catatan_keuangan
from delete_data import hapus_data_menu
from data_operations import tampilkan_data

# Menu utama
def main():
    while True:
        print("\nPilih fitur Kos Mate:")
        print("======================")
        print("1. Tambah Kontak Keluarga")
        print("2. Tambah Kegiatan Harian")
        print("3. Tambah Tagihan Bulanan")
        print("4. Tambah Belanja Bulanan")
        print("5. Tambah Catatan Keuangan")
        print("6. Hapus Data")
        print("7. Keluar")
        print("======================")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == '1':
            kontak_keluarga()
        elif pilihan == '2':
            kegiatan_harian()
        elif pilihan == '3':
            tagihan_bulanan()
        elif pilihan == '4':
            belanja_bulanan()
        elif pilihan == '5':
            catatan_keuangan()
        elif pilihan == '6':
            hapus_data_menu()
        elif pilihan == '7':
            print("Terima kasih telah menggunakan Kos Mate!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Jalankan program
if __name__ == "__main__":
    main()
