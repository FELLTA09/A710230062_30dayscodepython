# menginput data pribadi dari pengguna
def input_data_pribadi():
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    pekerjaan = input("Masukkan pekerjaan: ")
    pendidikan = input("Masukkan pendidikan: ")
    
    # dictionary untuk menyimpan data pribadi
    data_pribadi = {
        "nama": nama,
        "alamat": alamat,
        "pekerjaan": pekerjaan,
        "pendidikan": pendidikan
    }
    
    return data_pribadi

# menampilkan data pribadi
def tampilkan_data_pribadi(data):
    print("\nInformasi Pribadi:")
    print(f"Nama       : {data['nama']}")
    print(f"Alamat     : {data['alamat']}")
    print(f"Pekerjaan  : {data['pekerjaan']}")
    print(f"Pendidikan : {data['pendidikan']}")

# Input data pribadi dari pengguna
data_pribadi = input_data_pribadi()

# Menampilkan data pribadi
tampilkan_data_pribadi(data_pribadi)
