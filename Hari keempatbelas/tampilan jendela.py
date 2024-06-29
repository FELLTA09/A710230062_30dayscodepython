import tkinter as tk
from tkinter import simpledialog, messagebox

def main():
    # Buat jendela utama
    root = tk.Tk()
    root.withdraw()  # Sembunyikan jendela utama

    # Tampilkan dialog untuk menginput pesan
    message = simpledialog.askstring("Input", "Masukkan pesan Anda:")

    # Tampilkan pesan dalam kotak pesan
    if message:
        messagebox.showinfo("Pesan Anda", message)
    else:
        messagebox.showwarning("Tidak ada pesan", "Anda tidak memasukkan pesan apa pun.")

    # Tutup jendela utama
    root.quit()

if __name__ == "__main__":
    main()
