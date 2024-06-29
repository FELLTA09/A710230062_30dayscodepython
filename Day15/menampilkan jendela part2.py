import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Info Mahasiswa")

        # Membuat label dan entry untuk Nama
        self.label_nama = tk.Label(root, text="Nama:")
        self.label_nama.pack()
        self.entry_nama = tk.Entry(root)
        self.entry_nama.pack()

        # Membuat label dan entry untuk NIM
        self.label_nim = tk.Label(root, text="NIM:")
        self.label_nim.pack()
        self.entry_nim = tk.Entry(root)
        self.entry_nim.pack()

        # Membuat label dan entry untuk Kelas
        self.label_kelas = tk.Label(root, text="Kelas:")
        self.label_kelas.pack()
        self.entry_kelas = tk.Entry(root)
        self.entry_kelas.pack()

        # Membuat tombol untuk menampilkan pesan
        self.button_show = tk.Button(root, text="Tampilkan Pesan", command=self.show_message)
        self.button_show.pack()

    def show_message(self):
        nama = self.entry_nama.get()
        nim = self.entry_nim.get()
        kelas = self.entry_kelas.get()
        message = f"Nama: {nama}\nNIM: {nim}\nKelas: {kelas}"
        messagebox.showinfo("Info Mahasiswa", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
