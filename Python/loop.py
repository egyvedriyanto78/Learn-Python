import math

average = 101/2
print("average : ", average)
x = 0
i = 1

for i in range(1, 101):
    var = (i - average)**2
    i += 1
    x += var

result = x/(100-1)
print("Variance S^2 : ", result)