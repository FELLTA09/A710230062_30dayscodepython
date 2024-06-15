# Kelas utama 
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    
    def suara(self):
        raise NotImplementedError("Metode ini harus dioverride oleh kelas turunan")
    
    def bergerak(self):
        print(f"{self.nama} sedang bergerak.")
    
    def info(self):
        return f"{self.nama} adalah {self.jenis}."

# Kelas Turunan
class Mamalia(Hewan):
    def __init__(self, nama, jenis, warna_bulu):
        super().__init__(nama, jenis)
        self.warna_bulu = warna_bulu
    
    def suara(self):
        print(f"{self.nama} epooss roar.")
    
    def info(self):
        return f"{self.nama} adalah {self.jenis} dengan bulu berwarna {self.warna_bulu}."

class Burung(Hewan):
    def __init__(self, nama, jenis, rentang_sayap):
        super().__init__(nama, jenis)
        self.rentang_sayap = rentang_sayap
    
    def suara(self):
        print(f"{self.nama} makan daging")
    
    def bergerak(self):
        print(f"{self.nama} sedang terbang.")
    
    def info(self):
        return f"{self.nama} adalah {self.jenis} dengan rentang sayap {self.rentang_sayap} cm."

class Ikan(Hewan):
    def __init__(self, nama, jenis, jenis_air):
        super().__init__(nama, jenis)
        self.jenis_air = jenis_air
    
    def suara(self):
        print(f"{self.nama} membuat gelembung udara .")
    
    def bergerak(self):
        print(f"{self.nama} sedang mencari anaknya (Finding Nemo).")
    
    def info(self):
        return f"{self.nama} adalah {self.jenis} yang hidup di air {self.jenis_air}."

class Reptil(Hewan):
    def __init__(self, nama, jenis, jenis_sisik):
        super().__init__(nama, jenis)
        self.jenis_sisik = jenis_sisik
    
    def suara(self):
        print(f"{self.nama} mendesis.")
    
    def bergerak(self):
        print(f"{self.nama} sedang merayap.")
    
    def info(self):
        return f"{self.nama} adalah {self.jenis} dengan sisik {self.jenis_sisik}."

class Amfibi(Hewan):
    def __init__(self, nama, jenis, habitat):
        super().__init__(nama, jenis)
        self.habitat = habitat
    
    def suara(self):
        print(f"{self.nama} menguak.")
    
    def bergerak(self):
        print(f"{self.nama} sedang melompat.")
    
    def info(self):
        return f"{self.nama} adalah {self.jenis} yang hidup di {self.habitat}."

# Membuat instance dari setiap kelas turunan
mamalia = Mamalia("Macan", "mamalia karnivora pemakan daging", "belang oren hitam")
burung = Burung("Elang", "unggas terbesar", 200)
ikan = Ikan("Ikan Badut", "Amphiprioninae", "asin")
reptil = Reptil("Ular", "reptil darat berbisa", "bermacam-macam")
amfibi = Amfibi("Katak", "Anura", "dua habitat")

# Menggunakan metode dari setiap instance
for hewan in (mamalia, burung, ikan, reptil, amfibi):
    print(hewan.info())
    hewan.suara()
    hewan.bergerak()
    print()
