import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox, QTextEdit

class TicketApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pembelian Tiket MPL Indonesia')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel('Pilih kategori tiket:', self)
        layout.addWidget(self.label)

        self.combo = QComboBox(self)
        self.combo.addItem('Mythic - Rp. 220.000')
        self.combo.addItem('Legend - Rp. 120.000')
        self.combo.addItem('Epic - Rp. 70.000')
        layout.addWidget(self.combo)

        self.button = QPushButton('Hitung Total', self)
        self.button.clicked.connect(self.show_price)
        layout.addWidget(self.button)

        self.order_details = QTextEdit(self)
        self.order_details.setReadOnly(True)
        layout.addWidget(self.order_details)

        self.setLayout(layout)

    def show_price(self):
        selected_ticket = self.combo.currentText()

        if 'Mythic' in selected_ticket:
            price = 220000
        elif 'Legend' in selected_ticket:
            price = 120000
        elif 'Epic' in selected_ticket:
            price = 70000

        total_price = f'Total harga tiket adalah Rp. {price:,}'
        self.order_details.setText(f'Pesanan Anda:\n\nKategori Tiket: {selected_ticket}\n{total_price}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicketApp()
    ex.show()
    sys.exit(app.exec_())
