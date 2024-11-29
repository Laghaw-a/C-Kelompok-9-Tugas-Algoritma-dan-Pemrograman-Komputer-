# add_data.py

import pandas as pd
from data_operations import simpan_data, tampilkan_data

# Fungsi untuk menambah kontak keluarga
def kontak_keluarga():
    tampilkan_data("Kontak Keluarga")
    data_kontak = []
    while True:
        nama_kontak = input("Masukkan nama kontak keluarga: ")
        waktu_kontak = input("Masukkan tanggal pengingat kontak (DD-MM-YYYY): ")
        data_kontak.append({"Nama Kontak": nama_kontak, "Tanggal Pengingat": waktu_kontak})
        tambah_lagi = input("Apakah Anda ingin menambah kontak lagi? (iya/tidak): ").lower()
        if tambah_lagi != 'iya':
            break
    data_df = pd.DataFrame(data_kontak)
    simpan_data("Kontak Keluarga", data_df)
    print("Semua pengingat kontak keluarga berhasil disimpan.")

# Fungsi untuk menambah kegiatan harian
def kegiatan_harian():
    tampilkan_data("Kegiatan Harian")
    data_kegiatan = []
    while True:
        kegiatan = input("Masukkan kegiatan harian: ")
        waktu = input("Masukkan waktu (DD-MM-YYYY HH:MM): ")
        data_kegiatan.append({"Kegiatan": kegiatan, "Waktu": waktu})
        tambah_lagi = input("Apakah Anda ingin menambah kegiatan lagi? (iya/tidak): ").lower()
        if tambah_lagi != 'tidak':
            break
    data_df = pd.DataFrame(data_kegiatan)
    simpan_data("Kegiatan Harian", data_df)
    print("Semua kegiatan harian berhasil disimpan.")

# Fungsi untuk menambah tagihan bulanan
def tagihan_bulanan():
    tampilkan_data("Tagihan Bulanan")
    data_tagihan = []
    while True:
        tagihan = input("Masukkan jenis tagihan: ")
        jatuh_tempo = input("Masukkan tanggal jatuh tempo (DD-MM-YYYY): ")
        data_tagihan.append({"Jenis Tagihan": tagihan, "Jatuh Tempo": jatuh_tempo})
        tambah_lagi = input("Apakah Anda ingin menambah tagihan lagi? (iya/tidak): ").lower()
        if tambah_lagi != 'iya':
            break
    data_df = pd.DataFrame(data_tagihan)
    simpan_data("Tagihan Bulanan", data_df)
    print("Semua tagihan bulanan berhasil disimpan.")

# Fungsi untuk menambah belanja bulanan
def belanja_bulanan():
    tampilkan_data("Belanja Bulanan")
    data_belanja = []
    while True:
        item = input("Masukkan item belanja: ")
        jumlah = int(input("Masukkan jumlah: "))
        data_belanja.append({"Item": item, "Jumlah": jumlah})
        tambah_lagi = input("Apakah Anda ingin menambah item belanja lagi? (iya/tidak): ").lower()
        if tambah_lagi != 'iya':
            break
    data_df = pd.DataFrame(data_belanja)
    simpan_data("Belanja Bulanan", data_df)
    print("Semua item belanja bulanan berhasil disimpan.")

# Fungsi untuk menambah catatan keuangan
def catatan_keuangan():
    tampilkan_data("Catatan Keuangan")
    data_keuangan = []
    while True:
        jenis = input("Masukkan jenis transaksi (pemasukan/pengeluaran): ")
        jumlah = float(input("Masukkan jumlah: "))
        tanggal = input("Masukkan tanggal transaksi (DD-MM-YYYY): ")
        data_keuangan.append({"Jenis Transaksi": jenis, "Jumlah": jumlah, "Tanggal": tanggal})
        tambah_lagi = input("Apakah Anda ingin menambah catatan keuangan lagi? (iya/tidak): ").lower()
        if tambah_lagi != 'iya':
            break
    data_df = pd.DataFrame(data_keuangan)
    simpan_data("Catatan Keuangan", data_df)
    print("Semua catatan keuangan berhasil disimpan.")
