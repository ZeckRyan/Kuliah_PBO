class Pasien:
    def __init__(self, nama, id_pasien, penyakit):
        self.__nama = nama
        self.__id_pasien = id_pasien
        self.__penyakit = penyakit
    
    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama
    
    def get_id(self):
        return self.__id_pasien
    
    def set_id_pasien(self, id):
        self.__id_pasien = id
    
    def get_penyakit(self):
        return self.__penyakit

    def set_penyakit(self, penyakit):
        self.__penyakit = penyakit


pasien1 = Pasien("","","")
pasien1.set_nama("Zakki")
pasien1.set_id_pasien(342)
pasien1.set_penyakit("Sariawan")

print(f"Nama Pasien: {pasien1.get_nama()}")
print(f"ID Pasien: {pasien1.get_id()}")
print(f"Penyakit Pasien: {pasien1.get_penyakit()}")