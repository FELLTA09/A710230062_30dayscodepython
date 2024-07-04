import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt

class NotaBelanja(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.items = []

    def initUI(self):
        self.setWindowTitle('Nota Belanja')
        self.setGeometry(100, 100, 800, 600)
        
        layout = QVBoxLayout()
        
        # Input Item Belanja
        self.item_name_input = QLineEdit(self)
        self.item_name_input.setPlaceholderText('Nama Barang')
        
        self.item_price_input = QLineEdit(self)
        self.item_price_input.setPlaceholderText('Harga Barang')
        
        self.item_quantity_input = QLineEdit(self)
        self.item_quantity_input.setPlaceholderText('Jumlah Barang')
        
        self.add_item_button = QPushButton('Tambahkan Barang', self)
        self.add_item_button.clicked.connect(self.add_item)
        
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.item_name_input)
        input_layout.addWidget(self.item_price_input)
        input_layout.addWidget(self.item_quantity_input)
        input_layout.addWidget(self.add_item_button)
        
        # Tabel Nota Belanja
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Nama Barang', 'Harga', 'Jumlah', 'Total'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Total Harga
        self.total_label = QLabel('Total: Rp. 0', self)
        
        layout.addLayout(input_layout)
        layout.addWidget(self.table)
        layout.addWidget(self.total_label)
        
        self.setLayout(layout)
    
    def add_item(self):
        item_name = self.item_name_input.text()
        try:
            item_price = float(self.item_price_input.text())
            item_quantity = int(self.item_quantity_input.text())
        except ValueError:
            print("Harga harus berupa angka dan jumlah harus berupa integer.")
            return
        
        total_price = item_price * item_quantity
        self.items.append({'name': item_name, 'price': item_price, 'quantity': item_quantity, 'total': total_price})
        
        self.update_table()
        self.update_total()
    
    def update_table(self):
        self.table.setRowCount(0)
        for item in self.items:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(item['name']))
            self.table.setItem(row_position, 1, QTableWidgetItem(f"Rp. {item['price']}"))
            self.table.setItem(row_position, 2, QTableWidgetItem(str(item['quantity'])))
            self.table.setItem(row_position, 3, QTableWidgetItem(f"Rp. {item['total']}"))
    
    def update_total(self):
        total = sum(item['total'] for item in self.items)
        self.total_label.setText(f'Total: Rp. {total}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NotaBelanja()
    ex.show()
    sys.exit(app.exec_())
