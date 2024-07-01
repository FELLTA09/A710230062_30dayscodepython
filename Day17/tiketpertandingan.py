import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QSpinBox, QPushButton, QMessageBox

class TicketBookingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aplikasi Pemesanan Tiket Sepak Bola')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.match_label = QLabel('Pilih Pertandingan:')
        self.layout.addWidget(self.match_label)

        self.match_combobox = QComboBox()
        self.match_combobox.addItems(['Tim A vs Tim B', 'Tim C vs Tim D', 'Tim E vs Tim F'])
        self.layout.addWidget(self.match_combobox)

        self.ticket_label = QLabel('Jumlah Tiket:')
        self.layout.addWidget(self.ticket_label)

        self.ticket_spinbox = QSpinBox()
        self.ticket_spinbox.setRange(1, 10)
        self.layout.addWidget(self.ticket_spinbox)

        self.book_button = QPushButton('Pesan Tiket')
        self.book_button.clicked.connect(self.book_ticket)
        self.layout.addWidget(self.book_button)

        self.setLayout(self.layout)

    def book_ticket(self):
        match = self.match_combobox.currentText()
        tickets = self.ticket_spinbox.value()

        message = f'Anda telah memesan {tickets} tiket untuk pertandingan {match}.'
        QMessageBox.information(self, 'Konfirmasi Pemesanan', message)

def main():
    app = QApplication(sys.argv)
    window = TicketBookingApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
