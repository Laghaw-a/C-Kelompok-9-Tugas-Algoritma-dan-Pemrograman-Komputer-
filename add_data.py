# add_data.py

import pandas as pd
from data_operations import simpan_data, tampilkan_data, get_data

file_path = 'Kos_Mate_Data.xlsx'

#Fungsi untuk menambahkan kontak keluarga
def kontak_keluarga():
    sheet_name = "Kontak Keluarga"
    
    # Tampilkan data sebelumnya
    tampilkan_data(sheet_name)
    
    # Ambil data yang sudah ada dari sheet
    existing_data = get_data(sheet_name)
    if existing_data is not None:
        # Buat set nama kontak yang sudah ada (case-insensitive)
        existing_kontak = set(existing_data['Nama Kontak'].str.lower())
    else:
        existing_kontak = set()

    data_kontak = []
    while True:
        nama_kontak = input("Masukkan nama kontak keluarga: ")
        
        # Cek jika kontak sudah ada di database
        if nama_kontak.lower() in existing_kontak:
            print(f"Kontak '{nama_kontak}' sudah ada dalam data. Silakan tambahkan kontak lain.")
            continue
        
        nomor_kontak = input("Masukkan nomor telepon: ")
        waktu_kontak = input("Masukkan tanggal pengingat kontak (DD-MM-YYYY): ")
        data_kontak.append({"Nama Kontak": nama_kontak, "Nomor Telepon": nomor_kontak, "Tanggal Pengingat": waktu_kontak})
        
        # Tambahkan nama kontak ke set existing_kontak
        existing_kontak.add(nama_kontak.lower())
        
        tambah_lagi = input("Apakah Anda ingin menambah kontak lagi? (iya/tidak): ").lower()
        if tambah_lagi != 'iya':
            break

    if data_kontak:
        data_baru = pd.DataFrame(data_kontak)
        simpan_data(sheet_name, data_baru)
        print("Semua pengingat kontak keluarga berhasil disimpan.")
    else:
        print("Tidak ada data baru yang ditambahkan.")

#Fungsi untuk menambahkan kegiatan harian
def kegiatan_harian():
    sheet_name = "Kegiatan Harian"
    
    # Tampilkan data sebelumnya
    tampilkan_data(sheet_name)
    
    # Ambil data yang sudah ada dari sheet
    existing_data = get_data(sheet_name)
    if existing_data is not None:
        # Buat set dari kegiatan yang sudah ada (case-insensitive)
        existing_kegiatan = set(existing_data['Kegiatan'].str.lower())
    else:
        existing_kegiatan = set()

    data_kegiatan = []
    while True:
        kegiatan = input("Masukkan kegiatan harian: ")
        
        # Cek jika kegiatan sudah ada di database
        if kegiatan.lower() in existing_kegiatan:
            print(f"Kegiatan '{kegiatan}' sudah ada dalam data. Silakan tambahkan kegiatan lain.")
            continue
        
        waktu = input("Masukkan waktu (DD-MM-YYYY HH:MM): ")
        data_kegiatan.append({"Kegiatan": kegiatan, "Waktu": waktu})
        
        # Tambahkan kegiatan ke set existing_kegiatan
        existing_kegiatan.add(kegiatan.lower())
        
        tambah_lagi = input("Apakah Anda ingin menambah kegiatan lagi? (iya/tidak): ").lower()
        if tambah_lagi != 'iya':
            break

    if data_kegiatan:
        data_baru = pd.DataFrame(data_kegiatan)
        simpan_data(sheet_name, data_baru)
        print("Semua kegiatan harian berhasil disimpan.")
    else:
        print("Tidak ada data baru yang ditambahkan.")

#Fungsi untuk menambahkan tagihan bulanan
def tagihan_bulanan():
    sheet_name = "Tagihan Bulanan"
    
    # Tampilkan data sebelumnya
    tampilkan_data(sheet_name)
    
    # Ambil data yang sudah ada dari sheet
    existing_data = get_data(sheet_name)
    if existing_data is not None:
        # Buat set jenis tagihan yang sudah ada (case-insensitive)
        existing_tagihan = set(existing_data['Jenis Tagihan'].str.lower())
    else:
        existing_tagihan = set()

    data_tagihan = []
    while True:
        tagihan = input("Masukkan jenis tagihan: ")
        
        # Cek jika tagihan sudah ada di database
        if tagihan.lower() in existing_tagihan:
            print(f"Tagihan '{tagihan}' sudah ada dalam data. Silakan tambahkan tagihan lain.")
            continue
        
        jatuh_tempo = input("Masukkan tanggal jatuh tempo (DD-MM-YYYY): ")
        data_tagihan.append({"Jenis Tagihan": tagihan, "Jatuh Tempo": jatuh_tempo})
        
        # Tambahkan tagihan ke set existing_tagihan
        existing_tagihan.add(tagihan.lower())
        
        tambah_lagi = input("Apakah Anda ingin menambah tagihan lagi? (iya/tidak): ").lower()
        if tambah_lagi != 'iya':
            break

    if data_tagihan:
        data_baru = pd.DataFrame(data_tagihan)
        simpan_data(sheet_name, data_baru)
        print("Semua tagihan bulanan berhasil disimpan.")
    else:
        print("Tidak ada data baru yang ditambahkan.")
        
#Fungsi untuk menambah belanja bulanan
def belanja_bulanan():
    sheet_name = "Belanja Bulanan"
    
    # Tampilkan data sebelumnya
    tampilkan_data(sheet_name)
    
    # Ambil data yang sudah ada dari sheet
    existing_data = get_data(sheet_name)
    if existing_data is not None:
        # Buat set item belanja yang sudah ada (case-insensitive)
        existing_items = set(existing_data['Item'].str.lower())
    else:
        existing_items = set()
    
    data_belanja = []
    while True:
        item = input("Masukkan item belanja: ")
        
        # Cek jika item sudah ada di database
        if item.lower() in existing_items:
            print(f"Item '{item}' sudah ada dalam data. Silakan tambahkan item lain.")
            continue
        
        jumlah = int(input("Masukkan jumlah: "))
        data_belanja.append({"Item": item, "Jumlah": jumlah})
        
        # Tambahkan item ke set existing_items
        existing_items.add(item.lower())
        
        tambah_lagi = input("Apakah Anda ingin menambah item belanja lagi? (iya/tidak): ").lower()
        if tambah_lagi != 'iya':
            break
    
    if data_belanja:
        data_baru = pd.DataFrame(data_belanja)
        simpan_data(sheet_name, data_baru)
        print("Semua item belanja bulanan berhasil disimpan.")
    else:
        print("Tidak ada data baru yang ditambahkan.")


#Fungsi untuk menambahkan catatan keuangan

def catatan_keuangan():
    sheet_name = "Catatan Keuangan"
    
    # Tampilkan data sebelumnya
    tampilkan_data(sheet_name)
    
    # Ambil data yang sudah ada dari sheet
    existing_data = get_data(sheet_name)
    if existing_data is not None:
        # Buat set transaksi yang sudah ada (case-insensitive)
        existing_transactions = set(existing_data['Nama Transaksi'].str.lower())
    else:
        existing_transactions = set()
    
    data_keuangan = []
    while True:
        jenis = input("Masukkan jenis transaksi (pemasukan/pengeluaran): ")
        nama = input("Masukkan nama transaksi: ")
        
        # Cek jika transaksi sudah ada dalam data
        if nama.lower() in existing_transactions:
            print(f"Transaksi '{nama}' sudah ada dalam data. Silakan tambahkan transaksi lain.")
            continue
        
        jumlah = float(input("Masukkan jumlah: "))
        tanggal = input("Masukkan tanggal transaksi (DD-MM-YYYY): ")
        
        # Tambahkan transaksi ke daftar
        data_keuangan.append({"Jenis Transaksi": jenis, "Nama Transaksi": nama, "Jumlah": jumlah, "Tanggal": tanggal})
        
        # Tambahkan nama transaksi ke set existing_transactions
        existing_transactions.add(nama.lower())
        
        tambah_lagi = input("Apakah Anda ingin menambah catatan keuangan lagi? (iya/tidak): ").lower()
        if tambah_lagi != 'iya':
            break
    
    if data_keuangan:
        data_df = pd.DataFrame(data_keuangan)
        simpan_data(sheet_name, data_df)
        print("Semua catatan keuangan berhasil disimpan.")
    else:
        print("Tidak ada catatan keuangan baru yang ditambahkan.")








