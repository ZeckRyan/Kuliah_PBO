nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: ")) 
tinggiBadan = float(input("Masukkan tinggi badan Anda (dalam meter): "))
tinggiBadaninCM = tinggiBadan * 100

print(f"Halo {nama}, tinggi badan anda adalah {tinggiBadaninCM} cm")
if umur >= 18:
    print(f"Apakah Anda sudah dewasa? Ya")
else:
    print(f"Apakah Anda sudah dewasa? Tidak")
