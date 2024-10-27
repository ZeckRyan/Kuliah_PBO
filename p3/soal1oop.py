class Mahasiswa:
    def __init__(self, nama, nim, program_studi):
        self.nama = nama
        self.nim = nim
        self.program_studi = program_studi
    
    def info(self):
        print(f"Nama Mahasiswa: {self.nama}, NIM Mahasiswa: {self.nim}, Program Studi: {self.program_studi}")

mahasiswa1 = Mahasiswa("Zakki Farian", 5230411342, "Informatika")
mahasiswa1.info()