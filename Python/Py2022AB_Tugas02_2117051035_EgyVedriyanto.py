from cmath import sqrt
import math

r = float(input("Masukkan jari-jari : "))
s = 2*r*math.sin(math.pi/5)
pentagon = float(round((3*math.sqrt(3)/2*s*s),2))

print("Area pentagon adalah ", pentagon)