import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QSpinBox, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox

class BookOrderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pembelian Pesanan Buku')

        layout = QVBoxLayout()

        # Harga buku
        self.prices = {
            'Novel': 100000,
            'Cerita Bergambar': 80000,
            'Buku Tulis': 40000
        }

        # Novel
        novel_layout = QHBoxLayout()
        novel_label = QLabel('Novel (Rp 100.000):')
        self.novel_spinbox = QSpinBox()
        self.novel_spinbox.setRange(0, 100)
        novel_layout.addWidget(novel_label)
        novel_layout.addWidget(self.novel_spinbox)

        # Cerita Bergambar
        cerita_layout = QHBoxLayout()
        cerita_label = QLabel('Cerita Bergambar (Rp 80.000):')
        self.cerita_spinbox = QSpinBox()
        self.cerita_spinbox.setRange(0, 100)
        cerita_layout.addWidget(cerita_label)
        cerita_layout.addWidget(self.cerita_spinbox)

        # Buku Tulis
        tulis_layout = QHBoxLayout()
        tulis_label = QLabel('Buku Tulis (Rp 40.000):')
        self.tulis_spinbox = QSpinBox()
        self.tulis_spinbox.setRange(0, 100)
        tulis_layout.addWidget(tulis_label)
        tulis_layout.addWidget(self.tulis_spinbox)

        # Tombol hitung
        self.calculate_button = QPushButton('Hitung Total')
        self.calculate_button.clicked.connect(self.calculate_total)

        # Tambahkan semua layout ke layout utama
        layout.addLayout(novel_layout)
        layout.addLayout(cerita_layout)
        layout.addLayout(tulis_layout)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

    def calculate_total(self):
        novel_count = self.novel_spinbox.value()
        cerita_count = self.cerita_spinbox.value()
        tulis_count = self.tulis_spinbox.value()

        total_price = (novel_count * self.prices['Novel'] +
                       cerita_count * self.prices['Cerita Bergambar'] +
                       tulis_count * self.prices['Buku Tulis'])

        QMessageBox.information(self, 'Total Harga', f'Total Harga: Rp {total_price:,}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BookOrderApp()
    ex.show()
    sys.exit(app.exec_())
