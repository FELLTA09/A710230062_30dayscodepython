import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class PhonePurchaseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Pembelian Handphone Samsung')

        # Label dan ComboBox untuk model handphone
        self.model_label = QLabel('Pilih Model Handphone:', self)
        self.model_combo = QComboBox(self)
        self.model_combo.addItems([
            'Samsung Galaxy S21', 'Samsung Galaxy S21+', 'Samsung Galaxy S21 Ultra',
            'Samsung Galaxy Note 20', 'Samsung Galaxy Note 20 Ultra', 'Samsung Galaxy A72',
            'Samsung Galaxy A52', 'Samsung Galaxy A32', 'Samsung Galaxy M62',
            'Samsung Galaxy M42', 'Samsung Galaxy Z Fold 2', 'Samsung Galaxy Z Flip',
            'Samsung Galaxy S20 FE', 'Samsung Galaxy A12', 'Samsung Galaxy M12'
        ])
        
        # Label dan LineEdit untuk nama pembeli
        self.name_label = QLabel('Nama Pembeli:', self)
        self.name_input = QLineEdit(self)

        # Label dan LineEdit untuk jumlah pembelian
        self.quantity_label = QLabel('Jumlah Pembelian:', self)
        self.quantity_input = QLineEdit(self)

        # Tombol untuk submit
        self.submit_button = QPushButton('Beli', self)
        self.submit_button.clicked.connect(self.show_purchase_info)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.model_label)
        layout.addWidget(self.model_combo)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.quantity_label)
        layout.addWidget(self.quantity_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
    
    def show_purchase_info(self):
        model = self.model_combo.currentText()
        name = self.name_input.text()
        quantity = self.quantity_input.text()
        
        if name and quantity.isdigit():
            message = f'Terima kasih, {name}!\nAnda telah membeli {quantity} unit {model}.'
            QMessageBox.information(self, 'Informasi Pembelian', message)
        else:
            QMessageBox.warning(self, 'Kesalahan', 'Mohon masukkan nama dan jumlah pembelian yang valid.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PhonePurchaseApp()
    ex.show()
    sys.exit(app.exec_())
