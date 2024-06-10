#diskon mancing
tahun_lahir = int(input("masukan tahun kelahiran pemancing :"))
tahun_sekarang = 2024

#menghitung usia pemancing cihuuuy
usia = tahun_sekarang - tahun_lahir

#input harga mancing
harga = int(input("masukan harga mancing :"))

#tentukan diskon berdasarkan usia 
if usia >= 0 and usia <=5:
    diskon = 1.0
elif usia >=5 and usia <=14:
    diskon = 0.5
else:
    diskon = 0.0 
    
#menghitung harga diskon mancing cuyy
harga_setelah_diskon = harga*(1-diskon)

#tampilkan hasil
print(f"usia pemancing: {usia}tahun")
print("diskon :",int(diskon*100),"%")
print("harga setelah diskon :Rp.",int(harga_setelah_diskon))
