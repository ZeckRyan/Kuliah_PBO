angka = int(input("Masukkan angka: "))

if angka > 0:
    print("Bilangan Positif")
    if angka % 2 == 0:
        print("Bilangan Genap")
    else:
        print("Bilangan Ganjil")

elif angka < 0:
    print("Bilangan Negatif")
    if angka % 2 == 0:
        print("Bilangan Genap")
    else:
        print("Bilangan Ganjil")

else:
    print("Bilangan Nol")

