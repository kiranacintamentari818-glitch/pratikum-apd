nama = input("Masukkan Nama Lengkap: ")
nim = input("Masukkan NIM: ")

harga = float(input("Masukkan harga laptop: "))

diskon_dict = {
    "Acer": 5,
    "Asus": 7,
    "Lenovo": 10
}

print("\n==============================================")
print(f"{nama} dengan NIM {nim} ingin membeli laptop seharga Rp{harga:,.0f}")
print("==============================================")
print("{:<10} {:<15} {:<15}".format("Merk", "Diskon", "Harga Akhir"))
print("==============================================")

for merk, persen in diskon_dict.items():
    diskon = harga * (persen / 100)
    harga_akhir = harga - diskon
    print("{:<10} {:<15} Rp{:,.0f}".format(merk, f"{persen}%", harga_akhir))

print("==============================================")