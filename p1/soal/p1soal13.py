panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi: "))

volume = panjang * lebar * tinggi

if panjang and lebar == tinggi:
    kubus = "Ya"
else:
    kubus = "Tidak"

if volume > 1000 or panjang > 10:
    lebih = "Ya"
else:
    lebih = "Tidak"

print(f"\nPanjang = {panjang} meter, Lebar = {lebar} meter. Tinggi = {tinggi} meter dan Volumenya adalah {volume} meter")
print(f"Apakah balok tersebut berbentuk kubus? {kubus}")
print(f"Apakah bolume lebih dari 1000 atau panjang lebih dari 10 meter? {lebih}")
