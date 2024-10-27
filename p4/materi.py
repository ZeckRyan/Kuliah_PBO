class Mobil:
    # def __init__(self, merek):
    #     self.merek = merek #Atribut Publik
    
    # protected attribut dan metode yang bersifat diilindungi
    # def __init__(self, merek):
    #     self._merek = merek #Atribut dilindungi 
    

    def __init__(self, merek):
        self.__merek = merek #Private atribute
    
    def get_merek(self):
        return self.__merek

mobil1 = Mobil("Anto")
print(mobil1.get_merek())


