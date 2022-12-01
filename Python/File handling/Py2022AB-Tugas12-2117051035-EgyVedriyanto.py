def main():
    while True:
        try:
            file = input("Masukkan nama file: ").strip()
            infile = open(file, "r")
            break
        except IOError:
            print("File (" + file + ") tidak ada. Coba lagi!")
    
    count = 26 * [0]
    for alphabet in infile:
        countLetter(alphabet.lower(), count)
    
    for i in range(len(count)):
        if count[i] != 0:
            print(chr(ord('a') + i) + " muncul " + str(count[i]) + " kali") 
    infile.close()

def countLetter(alphabet, count):
    for ch in alphabet:
        if ch.isalpha():
            count[ord(ch) - ord('a')] += 1

main()