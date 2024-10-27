class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.__nama = nama
        self.__nim = nim
        self.__jurusan = jurusan
    
    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama
    
    def get_nim(self):
        return self.__nim
    
    def set_nim(self, nim):
        self.__nim = nim
    
    def get_jurusan(self):
        return self.__jurusan

    def set_jurusan(self, jurusan):
        self.__jurusan = jurusan

mahasiswa1 = Mahasiswa("", "","")
mahasiswa1.set_nama("Zakki")
mahasiswa1.set_nim(5230411342)
mahasiswa1.set_jurusan("informatika")

print(mahasiswa1.get_nama())
print(mahasiswa1.get_nim())
print(mahasiswa1.get_jurusan())