#   Egy Vedriyanto
#   2117051035
#   Kelas B

print("\n--PROGRAM MEMBUAT MATRIKS DAN MENGHITUNG RATA-RATA TIAP KOLOM--\n")
matriks = []
baris = eval(input("Masukkan jumlah baris: "))
kolom = eval(input("Masukkan jumlah kolom: "))
print()

for i in range(baris):
    matriks.append([])
    for j in range(kolom):
        angka = eval(input("Masukkan angka: "))
        matriks[i].append(angka)
print()

for i in range(0, len(matriks)):
    for j in range(0, len(matriks[i])):
        print(matriks[i][j], end = "\t")
    print()   
print()

for i in range(0, len(matriks[0])):
    total = 0
    avg = 0
    for j in range (0, len(matriks[0])):
        total += matriks [j][i]
        avg = total/len(matriks[0])
    print("Nilai rata-rata dari kolom ke-", i+1, " : ", avg)