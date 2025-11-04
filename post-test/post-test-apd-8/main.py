# main.py
import os
from auth import login, daftar

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== TOKO BONEKA ===")
        print("1. Masuk")
        print("2. Daftar")
        print("0. Keluar")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            login()
        elif pilihan == "2":
            daftar()
        elif pilihan == "0":
            print("Terima kasih sudah datang ke Toko Boneka.")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    main()
