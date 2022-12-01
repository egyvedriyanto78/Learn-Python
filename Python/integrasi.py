import math as p
import numpy as ny

a = 0
b = 1
nilai = int(input())
pembagian = (b - a) / (nilai - 1)
x = ny.linspace(a, b, nilai)
fungsi = 1/(1-(p.e**x))
ReimannL = pembagian * sum(fungsi[:nilai-1])
Error_ReimannL = 2 - ReimannL
ReimannR = pembagian * sum(fungsi[1::])
Error_ReimannR = 2 - ReimannR
I_mid = h * sum(ny.sin((x[:nilai-1] + x[1:])/2))
err_mid = 2 - I_mid
printf(ReimannL)
printf(Error_ReimannL)
printf(ReimannR)
printf(Error_ReimannR)
printf(I_mid)
printf(err_mid)