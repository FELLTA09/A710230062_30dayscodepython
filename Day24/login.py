import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 280, 80)
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()

        self.label_username = QLabel('Username:')
        self.input_username = QLineEdit()
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)

        self.label_password = QLabel('Password:')
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)

        self.button_login = QPushButton('Login')
        self.button_login.clicked.connect(self.check_credentials)
        layout.addWidget(self.button_login)

        self.setLayout(layout)

    def check_credentials(self):
        username = self.input_username.text()
        password = self.input_password.text()

        # Ganti dengan validasi sebenarnya (misalnya, cek dari database)
        if username == 'admin' and password == 'password':
            QMessageBox.information(self, 'Success', 'Login successful')
            self.open_main_window()
        else:
            QMessageBox.warning(self, 'Error', 'Bad username or password')

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 400, 300)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel('Welcome to the main window!')
        layout.addWidget(self.label)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec_())
