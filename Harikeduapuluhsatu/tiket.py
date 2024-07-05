import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QMessageBox

class TicketPriceApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Harga Tiket Bioskop')

        layout = QVBoxLayout()

        self.label = QLabel('Pilih jenis tiket:')
        layout.addWidget(self.label)

        self.comboBox = QComboBox()
        self.comboBox.addItems(['Anak-anak', 'Dewasa', 'Lansia'])
        layout.addWidget(self.comboBox)

        self.button = QPushButton('Tampilkan Harga')
        self.button.clicked.connect(self.showPrice)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.show()

    def showPrice(self):
        ticket_type = self.comboBox.currentText()
        if ticket_type == 'Anak-anak':
            price = 'Rp 30,000'
        elif ticket_type == 'Dewasa':
            price = 'Rp 50,000'
        elif ticket_type == 'Lansia':
            price = 'Rp 25,000'

        QMessageBox.information(self, 'Harga Tiket', f'Harga tiket {ticket_type}: {price}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicketPriceApp()
    sys.exit(app.exec_())
