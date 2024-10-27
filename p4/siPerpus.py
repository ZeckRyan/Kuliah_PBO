class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self._pengarang = pengarang
        self.__tahun_terbit = tahun_terbit

    def get_judul(self):
        return self.judul
    
    def set_judul(self, judul):
        self.judul = judul
    
    def get_pengarang(self):
        return self._pengarang
    
    def set_pengarang(self, pengarang):
        self._pengarang = pengarang
    
    def get_tahun_terbit(self):
        return self.__tahun_terbit

    def set_tahun_terbit(self, tahun_terbit):
        self.__tahun_terbit = tahun_terbit


buku1 = Buku("Jambi Bercerita", "Fadly Nugraha", 2024)
# print(buku1.judul) #bisa diakses diluar kelas (dimana saja)
print(buku1._pengarang) #harusnya hanya bisa digunakan di class itu sendiri dan inheriancetnya (hanya di c#) penanda antar programer lainnya
print(buku1.__tahun_terbit) #hanya bisa digunakan di class itu sendiri (bisa dipanggil menggunakan get/set)
