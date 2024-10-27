total_pembelian = float(input("Masukkan total pembelian anda: "))

if total_pembelian >= 500000:
    diskon = 0.2

elif 200000 <= total_pembelian < 500000:
    diskon = 0.1

else:
    diskon = 0.05

harga_akhir = total_pembelian * diskon

print(f"Total pembayaran anda adalah {harga_akhir}")