# meminta user/pengguna memasukan angka
angka = int(input("masukan angka : "))

# Mengecekangka itu positif,negatif/bernilai nol
if angka > 0:
    print("angka yang dimasukan adalah positif")
    
elif angka < 0:
    print("angka yang dimasukan adalah negatif")
    
else: 
    print("angka yang anda masukan bernilai nol")
    
#fungsi int(integer) untuk mengonversi nilai menjadi bilangan bulat
#fungsi if untuk melakukan percabangan berdasarkan kebenaran atau kesalahan
#fungsi elif untuk mengecek beberapa kondisi secara berurutan dan menjalankan blok kode dengan kondisi yang pertama kali terpenuhi
#fungsi else untuk menentukan blok kode yang akan di eksekusi  ketika kondisi pada 'if' / 'else'' sebelumnya tidak terpenuhi