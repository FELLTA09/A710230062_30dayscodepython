import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator Sederhana")
        self.setGeometry(100, 100, 300, 400)
        self.initUI()

    def initUI(self):
        # Membuat layout utama
        vbox = QVBoxLayout()

        # Membuat tampilan input/output
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 24px;")
        vbox.addWidget(self.display)

        # Membuat layout grid untuk tombol-tombol
        grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        # Menambahkan tombol ke dalam layout grid
        for text, row, col in buttons:
            button = QPushButton(text, self)
            button.setFixedSize(60, 60)
            button.setStyleSheet("font-size: 18px;")
            button.clicked.connect(self.on_click)
            grid.addWidget(button, row, col)

        vbox.addLayout(grid)
        self.setLayout(vbox)

    def on_click(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
