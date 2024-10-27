class Hero:
    # Class Variable
    jumlah_hero = 0

    def __init__(self, name, health, attackPower, armor):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor
        Hero.jumlah_hero += 1
    
    # Method tanpa return // void function jika di bahasa pemrograman yang lain 
    def heroSiapa(self):
        print("Hallo nama saya " + self.name)
    
    # 
    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attackPower)
        

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + " diserang " + lawan.name)
        serangan_diterima = attackPower_lawan/self.armor
        self.health -= serangan_diterima 
        print(lawan.name + " menyerang dengan jumlah damage " + str(serangan_diterima))
        print("Jumlah darah " + self.name +" tersisa adalah " + str(self.health ))  
    
    # Method dengan argumen
    def regeneration(self, up):
        self.health += up
        print(f"Health Hero {self.name} telah meningkat menjadi {self.health}")

    # Method dengan return 
    def getHealth(self):
        return self.health
    
    def flicker():
        pass

hero1 = Hero("grock", 100, 20, 10)
hero2 = Hero("atlas", 100, 30, 20)
hero3 = Hero("kaja", 100, 10, 10)
print("")
hero1.serang(hero2)
