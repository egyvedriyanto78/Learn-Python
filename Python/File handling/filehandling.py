def main():
    choose = input("Menu File\na : create\nb : read\nc : insert\n\n  Pilih : ")
    if choose == 'a':
        nama_file = input("Masukkan nama file: ")
        isi = input("Masukkan teks: ")
        outfile = open(nama_file, "w")
        outfile.write(isi)
        outfile.close()
    elif choose == 'b':
        nama_file = input("Masukkan nama file: ")
        infile = open(nama_file, "r")
        print(infile.read())
        infile.close()
    elif choose == 'c':
        nama_file = input("Masukkan nama file: ")
        isi = input("Masukkan teks tambahan: ")
        outfile = open(nama_file, "a")
        outfile.write("\n")
        outfile.write(isi)
        outfile.close()
main()