import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QVBoxLayout, QPushButton, QHBoxLayout, QMessageBox

class RamenOrderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pesanan Ramen')
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.label_title = QLabel('Pilih jumlah pesanan untuk setiap jenis ramen:', self)
        self.layout.addWidget(self.label_title)

        # Membuat layout horizontal untuk setiap jenis ramen
        self.ramen_types = {
            'Shoyu Ramen': 50000,
            'Miso Ramen': 55000,
            'Shio Ramen': 45000
        }
        
        self.spin_boxes = {}
        for ramen, price in self.ramen_types.items():
            h_layout = QHBoxLayout()
            label = QLabel(f'{ramen} (Rp {price}):', self)
            spin_box = QSpinBox(self)
            spin_box.setRange(0, 100)  # Maksimal 100 pesanan per jenis ramen
            self.spin_boxes[ramen] = spin_box
            h_layout.addWidget(label)
            h_layout.addWidget(spin_box)
            self.layout.addLayout(h_layout)

        self.calculate_button = QPushButton('Hitung Total Pesanan', self)
        self.calculate_button.clicked.connect(self.calculate_order)
        self.layout.addWidget(self.calculate_button)

        self.result_label = QLabel('', self)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def calculate_order(self):
        total_quantity = 0
        total_price = 0

        for ramen, price in self.ramen_types.items():
            quantity = self.spin_boxes[ramen].value()
            total_quantity += quantity
            total_price += quantity * price

        self.result_label.setText(f'Total Pesanan: {total_quantity} mangkok\nTotal Harga: Rp {total_price}')
        QMessageBox.information(self, 'Total Pesanan', f'Total Pesanan: {total_quantity} mangkok\nTotal Harga: Rp {total_price}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RamenOrderApp()
    ex.show()
    sys.exit(app.exec_())
