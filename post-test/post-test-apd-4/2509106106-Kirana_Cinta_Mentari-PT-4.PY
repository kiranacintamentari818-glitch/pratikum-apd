print("=== Selamat Datang di Toko Furnitur Infordeh ===")

username_asli = "KiranaCintaMentari"
password_asli = "2509106106"
batas_login = 3
login_berhasil = False

for percobaan in range(batas_login):
    print(f"\nPercobaan Login ke-{percobaan + 1}")
    username = input("Masukkan Username (Nama): ")
    password = input("Masukkan Password (NIM): ")

    if username == username_asli and password == password_asli:
        login_berhasil = True
        print("\nLogin berhasil! Selamat datang,", username)
        break
    else:
        print("Login gagal! Username atau Password salah.")
 
if not login_berhasil:
    print("\nAnda gagal login sebanyak 3 kali. Program dihentikan.")
    exit()

while True:
    print("\n=== MENU PEMBELIAN FURNITUR ===")
    print("1. Sofa           - Rp 500.000 per unit")
    print("2. Meja Belajar   - Rp 250.000 per unit")
    print("3. Rak Lemari     - Rp 150.000 per unit")
    print("4. Keluar")

    pilihan = input("Pilih furnitur (1-4): ")

    if pilihan == '4':
        print("\nTerima kasih telah berbelanja di Toko Furnitur Infordeh!")
        break

    if pilihan == '1':
        nama_furnitur = "Sofa"
        harga = 500000
    elif pilihan == '2':
        nama_furnitur = "Meja Belajar"
        harga = 250000
    elif pilihan == '3':
        nama_furnitur = "Rak Lemari"
        harga = 150000
    else:
        print("pilihan tidak valid, coba lagi")

    jumlah = input(f"Masukkan jumlah unit {nama_furnitur} yang ingin dibeli: ")

    if not jumlah.isdigit() or int(jumlah) <= 0:
        print("Jumlah harus berupa angka positif!")
        continue

    jumlah = int(jumlah)

    total_bayar = 0
    for i in range(jumlah):
        total_bayar += harga

    bonus_diskon = "-"
    total_akhir = total_bayar

    if total_bayar >= 700000:
        potongan = total_bayar * 0.20
        total_akhir -= potongan
        bonus_diskon = "Diskon 20%"
    elif total_bayar >= 500000:
        potongan = total_bayar * 0.08
        total_akhir -= potongan
        bonus_diskon = "Diskon 8%"
    elif total_bayar >= 150000:
        bonus_diskon = "Hadiah Kitchen Set"

    print("\n=== STRUK PEMBELIAN ===")
    print("Jenis Furnitur : ", nama_furnitur)
    print("Jumlah Unit    : ", jumlah)
    print("Total Bayar    : Rp", total_bayar)
    print("Bonus/Diskon   : ", bonus_diskon)
    print("Total Akhir    : Rp", int(total_akhir))
    print("===========================")

    lanjut = input("\nApakah ingin membeli furnitur lain? (y/n): ").lower()
    if lanjut != 'y':
        print("\nTerima kasih telah berbelanja di Toko Furnitur Infordeh!")
        break
