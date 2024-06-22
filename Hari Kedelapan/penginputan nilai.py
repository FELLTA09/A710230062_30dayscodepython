# Fungsi untuk mengevaluasi apakah siswa lulus atau gagal
def evaluasi_nilai(nilai_mtk, nilai_inggris, nilai_indonesia):
    # Menentukan apakah ada nilai yang kurang dari 75
    if nilai_mtk < 75 or nilai_inggris < 75 or nilai_indonesia < 75:
        return "Gagal"
    else:
        return "Lulus"

# Input nilai dari pengguna
nilai_mtk = int(input("Masukkan nilai Matematika: "))
nilai_inggris = int(input("Masukkan nilai Bahasa Inggris: "))
nilai_indonesia = int(input("Masukkan nilai Bahasa Indonesia: "))

# Evaluasi nilai
hasil = evaluasi_nilai(nilai_mtk, nilai_inggris, nilai_indonesia)

# Menampilkan hasil
print(f"Hasil evaluasi: {hasil}")
