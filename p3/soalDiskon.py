def hitung_diskon(harga, kategori):
    if kategori == "A":
        diskon = 0.1
    elif kategori == "B":
        diskon = 0.15
    elif kategori == "C":
        diskon = 0.2
    else:
        diskon = 1.0
    
    harga_akhir = harga * diskon
    return harga_akhir

pelanggan1 = hitung_diskon(300000, "A")
pelanggan2 = hitung_diskon(500000, "B")
pelanggan3 = hitung_diskon(800000, "C")
pelanggan4 = hitung_diskon(300000, "D")

print(f"Harga akhir Pelanggan 1: {pelanggan1}")
print(f"Harga akhir Pelanggan 2: {pelanggan2}")
print(f"Harga akhir Pelanggan 3: {pelanggan3}")
print(f"Harga akhir Pelanggan 4: {pelanggan4}")