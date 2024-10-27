class Dosen:
    def __init__(self, nama, nidn, mata_kuliah):
        self.__nama = nama
        self.__nidn = nidn
        self.__mata_kuliah = mata_kuliah
    
    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama
    
    def get_nidn(self):
        return self.__nidn
    
    def set_nidn(self, nidn):
        self.__nidn = nidn
    
    def get_mata_kuliah(self):
        return self.__mata_kuliah

    def set_mata_kuliah(self, mata_kuliah):
        self.__mata_kuliah = mata_kuliah


dosen1 = Dosen("","","")
dosen1.set_nama("Zakki")
dosen1.set_nidn(342)
dosen1.set_mata_kuliah("Pemrograman Berbasis Objek")

print(f"Nama Dosen: {dosen1.get_nama()}")
print(f"NIDN Dosen: {dosen1.get_nidn()}")
print(f"Mata Kuliah Dosen: {dosen1.get_mata_kuliah()}")