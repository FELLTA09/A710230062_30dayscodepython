def hitung_ketinggian_air(debit_air, waktu, luas_penampang):
    """
    Menghitung ketinggian air berdasarkan debit air yang masuk, waktu, dan luas penampang wadah.

    :param debit_air: Debit air yang masuk (dalam liter per detik)
    :param waktu: Waktu air mengalir (dalam detik)
    :param luas_penampang: Luas penampang wadah (dalam meter persegi)
    :return: Ketinggian air (dalam meter)
    """
    # Konversi debit air dari liter per detik ke meter kubik per detik
    debit_air_m3_per_s = debit_air / 1000

    # Volume air yang masuk (dalam meter kubik)
    volume_air = debit_air_m3_per_s * waktu

    # Menghitung ketinggian air (dalam meter)
    ketinggian_air = volume_air / luas_penampang

    return ketinggian_air

# Input dari pengguna
debit_air = float(input("Masukkan debit air yang masuk (liter per detik): "))
waktu = float(input("Masukkan waktu air mengalir (detik): "))
luas_penampang = float(input("Masukkan luas penampang wadah (meter persegi): "))

# Menghitung ketinggian air
ketinggian = hitung_ketinggian_air(debit_air, waktu, luas_penampang)

print(f"Ketinggian air setelah {waktu} detik adalah {ketinggian:.2f} meter")
