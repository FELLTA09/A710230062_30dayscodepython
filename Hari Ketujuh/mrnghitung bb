def input_berat_badan():
    berat_badan_list = []

    while True:
        try:
            berat_badan = float(input("Masukkan berat badan (kg) atau ketik 'selesai' untuk menghentikan: "))
            berat_badan_list.append(berat_badan)
        except ValueError:
            print("Input selesai atau input tidak valid. Program akan berhenti.")
            break

    return berat_badan_list

def hitung_rata_rata(berat_badan_list):
    if len(berat_badan_list) == 0:
        return 0
    return sum(berat_badan_list) / len(berat_badan_list)

def main():
    print("Program Penginputan Berat Badan")
    berat_badan_list = input_berat_badan()
    rata_rata = hitung_rata_rata(berat_badan_list)
    print(f"Berat badan yang diinput: {berat_badan_list}")
    print(f"Rata-rata berat badan: {rata_rata:.2f} kg")

if __name__ == "__main__":
    main()
