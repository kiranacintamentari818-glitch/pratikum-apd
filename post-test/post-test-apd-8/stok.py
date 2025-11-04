# stok.py
from prettytable import PrettyTable
from data import stok

def tampilkan_stok():
    print("\n=== DAFTAR STOK BONEKA ===")
    tabel = PrettyTable(["Nama Boneka", "Jumlah (pcs)"])
    for nama, jumlah in stok.items():
        tabel.add_row([nama, jumlah])
    print(tabel)

def tambah_stok(nama_boneka, jumlah):
    if nama_boneka in stok:
        stok[nama_boneka] += jumlah
    else:
        stok[nama_boneka] = jumlah
    print(f"{nama_boneka} berhasil ditambah. Sekarang stoknya: {stok[nama_boneka]} pcs")
    


