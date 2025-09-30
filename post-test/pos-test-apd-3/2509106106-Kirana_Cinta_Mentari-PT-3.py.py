nama_asli = "Kirana Cinta Mentari"
nim_asli = "2509106106"

nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")

if nama == nama_asli and nim == nim_asli:
    print("\nLogin berhasil! Pilih metode pembayaran UKT.\n")
    print("1. Lunas (1x bayar) - Admin 1%")
    print("2. Cicilan 2x per Semester - Admin 5%")
    print("3. Cicilan 4x per Semester - Admin 8%")
    print("4. Cicilan 6x per Semester - Admin 12%")
    
    pilihan = int(input("Pilih metode pembayaran (1/2/3/4): "))
    ukt = 6000000
    
    if pilihan == 1:
        admin = 0.01
        total = ukt + (ukt * admin)
        print(f"\nTotal yang harus dibayar: Rp {total:,.0f}")
    
    elif pilihan == 2:
        admin = 0.05
        total = ukt + (ukt * admin)
        cicilan = total / 2
        print(f"\nTotal yang harus dibayar: Rp {total:,.0f}")
        print(f"Periode cicilan: Rp {cicilan:,.0f}")
    
    elif pilihan == 3:
        admin = 0.08
        total = ukt + (ukt * admin)
        cicilan = total / 4
        print(f"\nTotal yang harus dibayar: Rp {total:,.0f}")
        print(f"Periode cicilan: Rp {cicilan:,.0f}")
    
    elif pilihan == 4:
        admin = 0.12
        total = ukt + (ukt * admin)
        cicilan = total / 6
        print(f"\nTotal yang harus dibayar: Rp {total:,.0f}")
        print(f"Periode cicilan: Rp {cicilan:,.0f}")
    
    else:
        print("\nPilihan tidak valid.")
else:
    print("\nLogin gagal! Nama atau NIM salah.")