import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QMessageBox

class YamahaPurchaseApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pembelian Kendaraan Yamaha")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Pilih merk dan jenis kendaraan Yamaha:")
        layout.addWidget(self.label)

        self.merk_combo = QComboBox()
        self.merk_combo.addItems(["Yamaha NMAX", "Yamaha Aerox", "Yamaha XSR", "Yamaha MT-15"])
        layout.addWidget(self.merk_combo)

        self.jenis_combo = QComboBox()
        self.jenis_combo.addItems(["Standar", "Sport", "Premium"])
        layout.addWidget(self.jenis_combo)

        self.confirm_button = QPushButton("Konfirmasi Pembelian")
        self.confirm_button.clicked.connect(self.confirm_purchase)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def confirm_purchase(self):
        merk = self.merk_combo.currentText()
        jenis = self.jenis_combo.currentText()
        QMessageBox.information(self, "Pembelian Dikonfirmasi", f"Anda telah membeli {merk} jenis {jenis}.")

def main():
    app = QApplication(sys.argv)
    window = YamahaPurchaseApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
