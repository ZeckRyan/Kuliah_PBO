sisi1 = float(input("Masukkan sisi pertama anda: "))
sisi2 = float(input("Masukkan sisi kedua anda: "))
sisi3 = float(input("Masukkan sisi ketiga anda: "))

if sisi1 == sisi2 == sisi3:
    segitiga = "Segitiga Sama Sisi"

elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
    segitiga = "Segitiga Sama Kaki"

else:
    segitiga = "Segitiga Sembarang"

print(f"Segitiga anda adalah: {segitiga}")