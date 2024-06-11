#mendapatkan nama dan nomor telepon dari pengguna
kontak = {}
for i in range(1,8):
 nama = input('Masukan nama  pengguna{} : '.format(i))
 no_hp = input('Masukan nomor HP pengguna{} : '.format(i))
 kontak[nama] = no_hp

 #kata asli
 kata = 'Phone Book'

#menampilkan hasil
print()
print(kata.center(50))
print()
for no, nama in enumerate(kontak, start=1):
    print('{}. [{}] = [{}]'.format (no, nama,kontak[nama]))