from Kendaraan import Kendaraan

class Motor(Kendaraan):
    roda = 2
    
    def __init__ (self, merk, roda, tahun, tipe):
        super().__init__(merk, roda, tahun)
        self.tipe = tipe
    
    def printMotor(self):
        print("Kendaraan mobil beroda",self.roda,"bermerk",self.merk,"tahun",self.tahun,"dengan tipe",self.tipe)