class Dosen:
    def __init__(self, nama, nip, mata_kuliah):
        self.nama = nama
        self.nip = nip
        self.mata_kuliah = mata_kuliah

    def detail(self):
        print(f"Nama Dosen: {self.nama}, NIP Dosen: {self.nip}, Mata Kuliah: {self.mata_kuliah}")

class Matakuliah:
    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks
    
    def info_kuliah(self):
        print(f"Nama mata kuliah: {self.nama}, dengan SKS: {self.sks}")

dosen1 = Dosen("Fadly", 85266230000, "Bullying" )

matakuliah1 = Matakuliah("Bullying", 5)

dosen1.detail()
print("")
matakuliah1.info_kuliah()

