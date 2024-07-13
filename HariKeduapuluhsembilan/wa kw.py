import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit, QPushButton, QListWidget, QListWidgetItem, QLabel
from PyQt5.QtCore import Qt

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('WhatsApp Chat')

        self.chat_list = QListWidget()
        self.message_input = QTextEdit()
        self.send_button = QPushButton('Send')

        self.send_button.clicked.connect(self.send_message)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.message_input)
        input_layout.addWidget(self.send_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.chat_list)
        main_layout.addLayout(input_layout)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)

    def send_message(self):
        message = self.message_input.toPlainText()
        if message.strip():
            list_item = QListWidgetItem()
            list_item_widget = QLabel(message)
            list_item_widget.setStyleSheet("background-color: #DCF8C6; padding: 5px; border-radius: 5px;")
            list_item.setSizeHint(list_item_widget.sizeHint())

            self.chat_list.addItem(list_item)
            self.chat_list.setItemWidget(list_item, list_item_widget)
            self.message_input.clear()

app = QApplication(sys.argv)
window = ChatWindow()
window.show()
sys.exit(app.exec_())
