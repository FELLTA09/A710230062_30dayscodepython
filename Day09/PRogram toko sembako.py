class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}: Rp{self.price}, Stok: {self.stock}"


class Store:
    def __init__(self):
        self.inventory = {}

    def add_item(self, name, price, stock):
        if name in self.inventory:
            self.inventory[name].stock += stock
        else:
            self.inventory[name] = Item(name, price, stock)

    def view_inventory(self):
        for item in self.inventory.values():
            print(item)

    def purchase_item(self, name, quantity):
        if name in self.inventory and self.inventory[name].stock >= quantity:
            total_price = self.inventory[name].price * quantity
            self.inventory[name].stock -= quantity
            print(f"Anda telah membeli {quantity} {name} seharga Rp{total_price}.")
        else:
            print("Maaf, stok tidak mencukupi atau barang tidak ditemukan.")


def main():
    store = Store()

    while True:
        print("\nToko Sembako")
        print("1. Tambah Barang ke Inventaris")
        print("2. Lihat Inventaris")
        print("3. Beli Barang")
        print("4. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            name = input("Nama Barang: ")
            price = int(input("Harga Barang (Rp): "))
            stock = int(input("Stok Barang: "))
            store.add_item(name, price, stock)
            print(f"{name} telah ditambahkan ke inventaris.")
        elif choice == '2':
            print("\nInventaris Toko:")
            store.view_inventory()
        elif choice == '3':
            name = input("Nama Barang yang Ingin Dibeli: ")
            quantity = int(input("Jumlah: "))
            store.purchase_item(name, quantity)
        elif choice == '4':
            print("Terima kasih telah menggunakan aplikasi Toko Sembako.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
