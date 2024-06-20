def hitung_harga_jual(harga_dasar, margin_keuntungan, pajak):
    keuntungan = harga_dasar * (margin_keuntungan / 100)
    total_pajak = harga_dasar * (pajak / 100)
    harga_jual = harga_dasar + keuntungan + total_pajak
    return harga_jual

motor_yamaha = {
    "NMAX": 29000000,
    "Aerox": 25000000,
    "Mio": 16000000,
    "XSR155": 36000000,
    "YZF-R15": 38000000
}

print("Pilih jenis motor Yamaha:")
for i, motor in enumerate(motor_yamaha.keys(), 1):
    print(f"{i}. {motor}")

pilihan_motor = int(input("Masukkan nomor pilihan motor: "))
motor_terpilih = list(motor_yamaha.keys())[pilihan_motor - 1]
harga_dasar = motor_yamaha[motor_terpilih]

margin_keuntungan = float(input("Masukkan margin keuntungan (%): "))
pajak = float(input("Masukkan pajak (%): "))

harga_jual = hitung_harga_jual(harga_dasar, margin_keuntungan, pajak)

print(f"\nMotor yang dipilih: {motor_terpilih}")
print(f"Harga dasar: Rp {harga_dasar:,.0f}")
print(f"Harga jual: Rp {harga_jual:,.0f}")
