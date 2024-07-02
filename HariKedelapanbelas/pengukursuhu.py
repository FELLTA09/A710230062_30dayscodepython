import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        # Membuat layout vertikal untuk menampung widget
        layout = QVBoxLayout()
        
        # Membuat label dan input untuk Celcius
        self.celcius_label = QLabel('Celcius:')
        self.celcius_input = QLineEdit(self)
        self.celcius_input.textChanged.connect(self.celciusChanged)
        
        # Membuat layout horisontal untuk Celcius
        celcius_layout = QHBoxLayout()
        celcius_layout.addWidget(self.celcius_label)
        celcius_layout.addWidget(self.celcius_input)
        
        # Membuat label dan input untuk Fahrenheit
        self.fahrenheit_label = QLabel('Fahrenheit:')
        self.fahrenheit_input = QLineEdit(self)
        self.fahrenheit_input.textChanged.connect(self.fahrenheitChanged)
        
        # Membuat layout horisontal untuk Fahrenheit
        fahrenheit_layout = QHBoxLayout()
        fahrenheit_layout.addWidget(self.fahrenheit_label)
        fahrenheit_layout.addWidget(self.fahrenheit_input)
        
        # Menambahkan layout horisontal ke layout vertikal
        layout.addLayout(celcius_layout)
        layout.addLayout(fahrenheit_layout)
        
        # Mengatur layout untuk widget utama
        self.setLayout(layout)
        
        # Mengatur judul dan ukuran jendela
        self.setWindowTitle('Pengukur Suhu')
        self.setGeometry(100, 100, 300, 100)
        self.show()
    
    def celciusChanged(self, text):
        if text:
            try:
                celcius = float(text)
                fahrenheit = (celcius * 9/5) + 32
                self.fahrenheit_input.setText(f"{fahrenheit:.2f}")
            except ValueError:
                self.fahrenheit_input.setText("")
        else:
            self.fahrenheit_input.setText("")
    
    def fahrenheitChanged(self, text):
        if text:
            try:
                fahrenheit = float(text)
                celcius = (fahrenheit - 32) * 5/9
                self.celcius_input.setText(f"{celcius:.2f}")
            except ValueError:
                self.celcius_input.setText("")
        else:
            self.celcius_input.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TemperatureConverter()
    sys.exit(app.exec_())
