input_nilaiTugas = float(input("Masukkan Nilai Tugas: "))
input_nilaiUTS = float(input("Masukkan Nilai UTS: "))
input_nilaiUAS = float(input("Masukkan Nilai UAS: "))

nilai_akhir = (0.3 * input_nilaiTugas) + (0.3 * input_nilaiUTS) +(0.4 * input_nilaiUAS)

if nilai_akhir >= 85:
    nilai_huruf = "A"

elif 70 <= nilai_akhir < 85:
    nilai_huruf = "B"

elif 55 <= nilai_akhir < 70:
    nilai_huruf = "C"

elif 40 <= nilai_akhir < 55:
    nilai_huruf = "D"

else:
    nilai_huruf = "E"

print(f"Nilai Akhir anda adalah: {nilai_huruf}")