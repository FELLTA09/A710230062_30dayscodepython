def apakah_prima(n):
    # Mengatasi kasus bilangan kurang dari 2
    if n < 2:
        print("Bukan Bilangan Prima coy")
        return

    # Memeriksa faktor dari 2 hingga akar kuadrat dari n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Bukan Bilangan Prima coy")
            return
    
    # Jika tidak ada faktor ditemukan, maka n adalah bilangan prima
    print("Bilangan Prima")

# Contoh Penggunaan
apakah_prima(6)   # Output: Bukan Bilangan Prima
apakah_prima(7)   # Output: Bilangan Prima
apakah_prima(1)   # Output: Bukan Bilangan Prima
apakah_prima(29)  # Output: Bilangan Prima
apakah_prima(25)  # Output: Bukan Bilangan Prima