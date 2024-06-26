class Penjualan:
    def __init__(self):
        self.data_penjualan = []

    def tambah_penjualan(self, jenis, jumlah, harga_satuan):
        penjualan = {
            'jenis': jenis,
            'jumlah': jumlah,
            'harga_satuan': harga_satuan,
            'total': jumlah * harga_satuan
        }
        self.data_penjualan.append(penjualan)

    def tampilkan_penjualan(self):
        if not self.data_penjualan:
            print("Belum ada penjualan.")
            return

        total_penjualan = 0
        for penjualan in self.data_penjualan:
            print(f"Jenis: {penjualan['jenis']}, Jumlah: {penjualan['jumlah']}, "
                  f"Harga Satuan: {penjualan['harga_satuan']}, Total: {penjualan['total']}")
            total_penjualan += penjualan['total']

        print(f"Total penjualan keseluruhan: {total_penjualan}")

# Contoh penggunaan
penjualan = Penjualan()

# Menambahkan beberapa data penjualan
penjualan.tambah_penjualan('Sepeda Motor', 5, 15000000)
penjualan.tambah_penjualan('Mobil', 2, 250000000)
penjualan.tambah_penjualan('Sepeda', 10, 2000000)

# Menampilkan laporan penjualan
penjualan.tampilkan_penjualan()
