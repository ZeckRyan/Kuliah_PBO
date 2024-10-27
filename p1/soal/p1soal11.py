nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: ")) 
tinggiBadan = float(input("Masukkan tinggi badan Anda (dalam meter): "))
tinggiBadaninCM = tinggiBadan * 100

if umur >= 18:
    dewasa = "Sudah"
else:
    dewasa = "Belum"

print(f" {dewasa}")
print(f"Halo {nama}, tinggi badan anda adalah {tinggiBadaninCM} cm dan saya {dewasa} dewasa ")




