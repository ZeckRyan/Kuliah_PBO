input_suhu = int(input("Masukkan suhu(dalam Celcius): "))

if input_suhu > 30:
    suhu = "Panas"

elif input_suhu >= 15:
    suhu = "Sejuk"

else:
    suhu = "Dingin"

print("")
print(f"Suhu sekarang {suhu}")
