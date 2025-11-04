# transaksi.py
from prettytable import PrettyTable
from data import stok, keranjang

def beli_boneka(nama_boneka, jumlah):
    if nama_boneka in stok and stok[nama_boneka] >= jumlah:
        stok[nama_boneka] -= jumlah
        keranjang[nama_boneka] = keranjang.get(nama_boneka, 0) + jumlah
        print(f"Berhasil membeli {jumlah} {nama_boneka}")
    else:
        print("Stok tidak cukup atau boneka tidak ditemukan.")

def lihat_keranjang():
    print("\n=== KERANJANG ANDA ===")
    if keranjang:
        tabel = PrettyTable(["Nama Boneka", "Jumlah"])
        for nama, jumlah in keranjang.items():
            tabel.add_row([nama, jumlah])
        print(tabel)
    else:
        print("Keranjang masih kosong.")
