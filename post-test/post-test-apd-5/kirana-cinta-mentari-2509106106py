import os

akun = [
    ["Kirana Cinta Mentari", "admin123", "admin"]
]
stok = []

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== TOKO BONEKA ===")
    print("1. Masuk")
    print("2. Daftar")
    print("0. Keluar")
    menu_awal = input("Pilih: ")

    if menu_awal == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== DAFTAR AKUN ===")
        user_baru = input("Username baru: ")
        pass_baru = input("Password baru: ")
        akun.append([user_baru, pass_baru, "user"])
        print("Akun berhasil dibuat.")
        input("Enter...")

    elif menu_awal == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== LOGIN ===")
        u = input("Username: ")
        p = input("Password: ")
        masuk = None

        for a in akun:
            if a[0] == u and a[1] == p:
                masuk = a
                break

        if masuk is None:
            print("Username atau password salah.")
            input("Enter...")

        else:
            if masuk[2] == "admin":
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=== MENU ADMIN ===")
                    print("1. Tambah data")
                    print("2. Lihat data")
                    print("3. Edit data")
                    print("4. Hapus data")
                    print("0. Keluar")
                    pilih_admin = input("Pilih: ")

                    if pilih_admin == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        nama = input("Nama item: ")
                        harga = input("Harga: ")
                        jumlah = input("Jumlah: ")
                        stok.append([nama, harga, jumlah])
                        print("Data ditambah.")
                        input("Enter...")

                    elif pilih_admin == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        if stok == []:
                            print("Belum ada data.")
                        else:
                            for i, item in enumerate(stok):
                                print(f"{i+1}. {item[0]} - {item[1]} - {item[2]}")
                        input("Enter...")

                    elif pilih_admin == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        if stok == []:
                            print("Data kosong.")
                            input("Enter...")
                        else:
                            for i, item in enumerate(stok):
                                print(f"{i+1}. {item[0]} - {item[1]} - {item[2]}")
                            idx = int(input("Pilih nomor: ")) - 1
                            if 0 <= idx < len(stok):
                                nama = input("Nama baru: ")
                                harga = input("Harga baru: ")
                                jumlah = input("Jumlah baru: ")
                                stok[idx] = [nama, harga, jumlah]
                                print("Data diperbarui.")
                            input("Enter...")

                    elif pilih_admin == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        if stok == []:
                            print("Data kosong.")
                            input("Enter...")
                        else:
                            for i, item in enumerate(stok):
                                print(f"{i+1}. {item[0]} - {item[1]} - {item[2]}")
                            idx = int(input("Pilih nomor: ")) - 1
                            if 0 <= idx < len(stok):
                                stok.pop(idx)
                                print("Data dihapus.")
                            input("Enter...")

                    elif pilih_admin == "0":
                        break

            else:
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=== MENU PENGGUNA ===")
                    print("1. Lihat data")
                    print("0. Keluar")
                    pilih_user = input("Pilih: ")

                    if pilih_user == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        if stok == []:
                            print("Belum ada data.")
                        else:
                            for i, item in enumerate(stok):
                                print(f"{i+1}. {item[0]} - {item[1]} - {item[2]}")
                        input("Enter...")

                    elif pilih_user == "0":
                        break

    elif menu_awal == "0":
        break

    else:
        print("Pilihan tidak ada.")
        input("Enter...")
