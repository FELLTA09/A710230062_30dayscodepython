import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Kalkulator BMI')
        
        self.weight_label = QLabel('Berat badan (kg):')
        self.weight_input = QLineEdit(self)
        
        self.height_label = QLabel('Tinggi badan (cm):')
        self.height_input = QLineEdit(self)
        
        self.calculate_button = QPushButton('Hitung BMI', self)
        self.calculate_button.clicked.connect(self.calculate_bmi)
        
        layout = QVBoxLayout()
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.calculate_button)
        
        self.setLayout(layout)
        
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height_cm = float(self.height_input.text())
            height_m = height_cm / 100
            bmi = weight / (height_m ** 2)
            QMessageBox.information(self, 'Hasil BMI', f'BMI Anda adalah: {bmi:.2f}')
        except ValueError:
            QMessageBox.warning(self, 'Kesalahan', 'Mohon masukkan nilai yang valid untuk berat dan tinggi badan.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BMICalculator()
    ex.show()
    sys.exit(app.exec_())
