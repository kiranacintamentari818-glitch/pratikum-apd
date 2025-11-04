# auth.py
import os
from data import akun
from stok import tampilkan_stok, tambah_stok
from transaksi import beli_boneka, lihat_keranjang

def tampilkan_menu():
    print("\n1. Lihat Stok")
    print("2. Tambah Stok (Admin)")
    print("3. Beli Boneka (User)")
    print("4. Lihat Keranjang")
    print("5. Logout")

def login():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== LOGIN ===")
    username = input("Masukkan nama pengguna: ")
    password = input("Masukkan password: ")

    if username in akun and akun[username]["password"] == password:
        print(f"\nSelamat datang, {username}.")
        input("Tekan Enter untuk lanjut...")
        menu_utama(username)
    else:
        print("\nLogin gagal. Nama atau password salah.")
        input("Tekan Enter untuk kembali...")

def daftar():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== DAFTAR AKUN BARU ===")
    nama = input("Masukkan nama pengguna baru: ")
    if nama in akun:
        print("Nama sudah digunakan. Coba yang lain.")
        input("Tekan Enter untuk kembali...")
        return
    pw = input("Masukkan password: ")
    akun[nama] = {"password": pw, "role": "user"}
    print("Akun berhasil dibuat. Silakan login.")
    input("Tekan Enter untuk lanjut...")

def menu_utama(username):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"=== MENU UTAMA ({username}) ===")
        tampilkan_menu()

        pilihan = input("Pilih menu: ")

        try:
            if pilihan == "1":
                tampilkan_stok()
            elif pilihan == "2":
                if akun[username]["role"] == "admin":
                    nama = input("Masukkan nama boneka: ")
                    jumlah = int(input("Masukkan jumlah tambahan: "))
                    tambah_stok(nama, jumlah)
                else:
                    print("Anda bukan admin, tidak dapat menambah stok.")
            elif pilihan == "3":
                if akun[username]["role"] == "user":
                    nama = input("Masukkan nama boneka: ")
                    jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
                    beli_boneka(nama, jumlah)
                else:
                    print("Admin tidak dapat membeli boneka.")
            elif pilihan == "4":
                lihat_keranjang()
            elif pilihan == "5":
                print("Logout berhasil.")
                input("Tekan Enter untuk kembali ke menu awal...")
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

        input("\nTekan Enter untuk melanjutkan...")
