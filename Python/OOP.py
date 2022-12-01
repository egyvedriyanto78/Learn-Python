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

print(x1.panjang)
print(x2.panjang)

print(x1.lebar)
print(x2.lebar)

print(x1.getKeliling())
print(x2.getKeliling())

print(x1.getLuas())
print(x2.getLuas())

print(x1.getKeliling != x2.getKeliling)
print(x1.getLuas == x2.getLuas)
print(x1 == x2)
        
            