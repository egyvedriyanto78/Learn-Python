def mutu():
    nama = input("Masukkan nama\t: ")
    npm = input("Masukkan NPM\t: ")
    nilai = eval(input("Masukkan nilai\t: "))

    if nilai <= 100 and nilai >= 76:
        output = 'A'
    elif nilai < 76 and nilai >= 71:
        output = 'B+'
    elif nilai < 71 and nilai >= 66:
        output = 'B'
    elif nilai < 66 and nilai >= 61:
        output = 'C+'
    elif nilai < 61 and nilai >= 56:
        output = 'C'
    elif nilai < 56 and nilai >= 51:
        output = 'D'
    elif nilai < 51 and nilai >= 0:
        output = 'E'
    else:
        output = 'Nilai invalid!'
    
    print("\nNama\t: ",nama)
    print("NPM\t: ",npm)
    print("NIlai\t: ",output)

mutu()

