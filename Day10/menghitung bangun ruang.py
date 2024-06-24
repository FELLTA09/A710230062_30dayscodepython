import math

def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def luas_permukaan_tabung(jari_jari, tinggi):
    luas_alas = math.pi * jari_jari**2
    luas_selimut = 2 * math.pi * jari_jari * tinggi
    return 2 * luas_alas + luas_selimut

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari**2

def main():
    print("Pilih bentuk untuk menghitung luas permukaan:")
    print("1. Balok")
    print("2. Tabung")
    print("3. Lingkaran")
    
    pilihan = input("Masukkan pilihan (1/2/3): ")
    
    if pilihan == '1':
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        luas = luas_permukaan_balok(panjang, lebar, tinggi)
        print(f"Luas permukaan balok: {luas:.2f} satuan persegi")
    elif pilihan == '2':
        jari_jari = float(input("Masukkan jari-jari tabung: "))
        tinggi = float(input("Masukkan tinggi tabung: "))
        luas = luas_permukaan_tabung(jari_jari, tinggi)
        print(f"Luas permukaan tabung: {luas:.2f} satuan persegi")
    elif pilihan == '3':
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = luas_lingkaran(jari_jari)
        print(f"Luas lingkaran: {luas:.2f} satuan persegi")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
