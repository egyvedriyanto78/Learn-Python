from Kendaraan import Kendaraan

class Mobil(Kendaraan):
    roda = 4
    
    def __init__ (self, merk, roda, tahun, penumpang):
        super().__init__(merk, roda, tahun)
        self.penumpang = penumpang
    
    def printMobil(self):
        print("Kendaraan mobil beroda",self.roda,"bermerk",self.merk,"tahun",self.tahun,"dengan muatan",self.penumpang,"penumpang")