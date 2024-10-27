class Mobil:
    jumlah_mobil = 0
    def __init__(self, merek, model):
        self.merek = merek
        self.model = model
        Mobil.jumlah_mobil += 1


    def info(self):
        return f"Mobil: {self.merek} model: {self.model}"
    
    

mobil1 = Mobil("Toyota", "Corolla")
print(f"Jumlah mobil sekarang adalah: {Mobil.jumlah_mobil}")
print("")
print(mobil1.info())

# init == constructor
# self merujuk pada objet saat ini