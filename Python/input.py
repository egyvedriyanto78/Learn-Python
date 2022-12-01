matriks = []
baris = eval(input("Masukkan jumlah baris: "))
kolom = eval(input("Masukkan jumlah kolom: "))

for i in range(baris):
    matriks.append([])
    for j in range(kolom):
        for a in range(baris):
            for b in range(kolom):
                angka = eval(input("Masukkan angka pada baris ke-",a," kolom ke-",b," : "))
        matriks[i].append(angka)
print()

for i in range(0, len(matriks)):
    for j in range(0, len(matriks[i])):
        print(matriks[i][j], end = "\t")
    print()   
print()

for i in range(0, len(matriks[0])):
    total = 0
    for j in range (0, len(matriks[0])):
        total += matriks [j][i]
    print("Nilai jumlah dari kolom ke-", i+1, " : ", total)