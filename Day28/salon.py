import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton, QMessageBox

class SalonPriceList(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Daftar harga dari website
        self.price_list = {
            "Hair Cut": 60000,
            "Hair Wash": 30000,
            "Hair Coloring": 150000,
            "Hair Perm": 200000,
            "Manicure": 50000,
            "Pedicure": 50000,
            "Facial": 100000,
            "Body Scrub": 120000,
            "Massage": 80000,
        }

        self.checkboxes = []

        # Tambahkan harga ke layout
        for service, price in self.price_list.items():
            checkbox = QCheckBox(f"{service}: Rp {price:,}")
            self.checkboxes.append(checkbox)
            layout.addWidget(checkbox)

        self.order_button = QPushButton('Pesan')
        self.order_button.clicked.connect(self.show_order)
        layout.addWidget(self.order_button)

        self.setLayout(layout)
        self.setWindowTitle('Daftar Harga Salon')
        self.show()

    def show_order(self):
        order_summary = []
        total_price = 0

        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                service = checkbox.text().split(":")[0]
                price = self.price_list[service]
                order_summary.append(f"{service}: Rp {price:,}")
                total_price += price

        order_details = "\n".join(order_summary)
        order_details += f"\n\nTotal: Rp {total_price:,}"

        QMessageBox.information(self, 'Pesanan Anda', order_details)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SalonPriceList()
    sys.exit(app.exec_())
