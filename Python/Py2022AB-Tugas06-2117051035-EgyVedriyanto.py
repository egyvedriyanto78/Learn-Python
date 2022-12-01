import math

class persegiPanjang:
    def __init__(self, panjang=1, lebar=1):
        self.panjang = panjang
        self.lebar = lebar
        
    def getKeliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def getLuas(self):
        return self.panjang * self.lebar
    
    def getPanjang(self, panjang):
        self.panjang = panjang
    
    def getLebar(self, lebar):
        self.lebar = lebar

x1 = persegiPanjang(7, 8)
x2 = persegiPanjang(7, 8)

print("Panjang x1\t: ", x1.panjang)
print("Lebar x1\t: ", x1.lebar)
print("\n")
print("Panjang x2\t: ", x2.panjang)
print("Lebar x2\t: ", x2.lebar)
print("\n")
print("Keliling x1\t: ", x1.getKeliling())
print("Keliling x2\t: ", x2.getKeliling())
print("\n")
print("Luas x1\t\t: ", x1.getLuas())
print("Luas x2\t\t: ", x2.getLuas())
print("\n")
print("Apakah keliling x1 tidak sama dengaan x2?\n", x1.getKeliling != x2.getKeliling)
print("\n")
print("Apakah keliling x1 sama dengaan x2?\n", x1.getLuas == x2.getLuas)
print("\n")
print("Apakah x1 sama dengan x2?\n", x1 == x2)
        
            