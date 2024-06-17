def input_data_diri():
    data_diri = {}

    data_diri['Nama'] = input("Masukkan Nama: ")
    data_diri['NIM'] = input("Masukkan NIM: ")
    data_diri['Alamat'] = input("Masukkan Alamat: ")

    return data_diri

def tampilkan_data_diri(data_diri):
    print("\nData Diri Anda:")
    for kunci, nilai in data_diri.items():
        print(f"{kunci}: {nilai}")

def main():
    data_diri = input_data_diri()
    tampilkan_data_diri(data_diri)

if __name__ == "__main__":
    main()
