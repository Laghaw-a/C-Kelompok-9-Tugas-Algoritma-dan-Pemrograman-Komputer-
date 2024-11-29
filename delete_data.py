# delete_data.py

from data_operations import hapus_data, tampilkan_data, get_data  # Pastikan ada fungsi get_data() yang mengembalikan data

def hapus_data_menu():
    while True:  # Menu utama untuk memilih kategori
        print("\nPilih data yang ingin dihapus:")
        print("1. Kontak Keluarga")
        print("2. Kegiatan Harian")
        print("3. Tagihan Bulanan")
        print("4. Belanja Bulanan")
        print("5. Catatan Keuangan")
        print("6. Keluar")
        
        pilihan = input("Masukkan pilihan (1-6): ").strip()

        if pilihan == '6':  # Keluar dari program
            print("Keluar dari menu penghapusan.")
            break
        
        elif pilihan == '1':
    # Cek apakah data kosong
            data_kontak = get_data("Kontak Keluarga")  # Fungsi get_data() untuk mengambil data
            if data_kontak is None or data_kontak.empty:
                print("\nData Kontak Keluarga kosong. Kembali ke menu utama.")
                continue  # Kembali ke menu utama jika data kosong

            while True:  # Looping dalam kategori "Kontak Keluarga"
                tampilkan_data("Kontak Keluarga")  # Tampilkan data terbaru
                nama_kontak = input("\nMasukkan nama kontak yang ingin dihapus: ").strip()
                hapus_data("Kontak Keluarga", {"Nama Kontak": nama_kontak})
                #print("\nData setelah dihapus:")
                tampilkan_data("Kontak Keluarga")  # Tampilkan data yang baru setelah penghapusan

                hapus_lagi = input("\nApakah Anda ingin menghapus kontak lainnya? (iya/tidak): ").strip().lower()
                if hapus_lagi != 'iya':
                    break  # Keluar dari loop "Kontak Keluarga" jika jawabannya bukan 'iya'

        elif pilihan == '2':
            # Cek apakah data kosong
            data_kegiatan = get_data("Kegiatan Harian")
            if data_kegiatan is None or data_kegiatan.empty :
                print("\nData Kegiatan Harian kosong. Kembali ke menu utama.")
                continue  # Kembali ke menu utama jika data kosong

            while True:  # Looping dalam kategori "Kegiatan Harian"
                tampilkan_data("Kegiatan Harian")  # Tampilkan data terbaru
                kegiatan = input("\nMasukkan kegiatan yang ingin dihapus: ").strip()
                hapus_data("Kegiatan Harian", {"Kegiatan": kegiatan})
                print("\nData setelah dihapus:")
                tampilkan_data("Kegiatan Harian")  # Tampilkan data yang baru setelah penghapusan

                hapus_lagi = input("\nApakah Anda ingin menghapus kegiatan lainnya? (iya/tidak): ").strip().lower()
                if hapus_lagi != 'iya':
                    break  # Keluar dari loop "Kegiatan Harian" jika jawabannya bukan 'iya'

        elif pilihan == '3':
            # Cek apakah data kosong
            data_tagihan = get_data("Tagihan Bulanan")
            if data_tagihan is None or data_tagihan.empty :
                print("\nData Tagihan Bulanan kosong. Kembali ke menu utama.")
                continue  # Kembali ke menu utama jika data kosong

            while True:  # Looping dalam kategori "Tagihan Bulanan"
                tampilkan_data("Tagihan Bulanan")  # Tampilkan data terbaru
                tagihan = input("\nMasukkan jenis tagihan yang ingin dihapus: ").strip()
                hapus_data("Tagihan Bulanan", {"Jenis Tagihan": tagihan})
                print("\nData setelah dihapus:")
                tampilkan_data("Tagihan Bulanan")  # Tampilkan data yang baru setelah penghapusan

                hapus_lagi = input("\nApakah Anda ingin menghapus tagihan lainnya? (iya/tidak): ").strip().lower()
                if hapus_lagi != 'iya':
                    break  # Keluar dari loop "Tagihan Bulanan" jika jawabannya bukan 'iya'

        elif pilihan == '4':
            # Cek apakah data kosong
            data_belanja = get_data("Belanja Bulanan")
            if data_belanja is None or data_belanja.empty :
                print("\nData Belanja Bulanan kosong. Kembali ke menu utama.")
                continue  # Kembali ke menu utama jika data kosong

            while True:  # Looping dalam kategori "Belanja Bulanan"
                tampilkan_data("Belanja Bulanan")  # Tampilkan data terbaru
                item = input("\nMasukkan item belanja yang ingin dihapus: ").strip()
                hapus_data("Belanja Bulanan", {"Item": item})
                print("\nData setelah dihapus:")
                tampilkan_data("Belanja Bulanan")  # Tampilkan data yang baru setelah penghapusan

                hapus_lagi = input("\nApakah Anda ingin menghapus item belanja lainnya? (iya/tidak): ").strip().lower()
                if hapus_lagi != 'iya':
                    break  # Keluar dari loop "Belanja Bulanan" jika jawabannya bukan 'iya'

        elif pilihan == '5':
            # Cek apakah data kosong
            data_keuangan = get_data("Catatan Keuangan")
            if data_keuangan is None or data_keuangan.empty :
                print("\nData Catatan Keuangan kosong. Kembali ke menu utama.")
                continue  # Kembali ke menu utama jika data kosong

            while True:  # Looping dalam kategori "Catatan Keuangan"
                tampilkan_data("Catatan Keuangan")  # Tampilkan data terbaru
                tanggal = input("\nMasukkan tanggal transaksi yang ingin dihapus (YYYY-MM-DD): ").strip()
                hapus_data("Catatan Keuangan", {"Tanggal": tanggal})
                print("\nData setelah dihapus:")
                tampilkan_data("Catatan Keuangan")  # Tampilkan data yang baru setelah penghapusan

                hapus_lagi = input("\nApakah Anda ingin menghapus catatan lainnya? (iya/tidak): ").strip().lower()
                if hapus_lagi != 'iya':
                    break  # Keluar dari loop "Catatan Keuangan" jika jawabannya bukan 'iya'

        else:
            print("Pilihan tidak valid. Silakan pilih nomor yang benar.")
