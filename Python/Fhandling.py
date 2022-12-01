# file = open('data.txt', mode='w', encoding='utf-8')



# Close File
# file.close()

# Cara simpel open dan close
with open('test.txt', mode='r', encoding='utf-8') as file:
    # File kondisi open
    # file.write('Halo')
    # print(file.read()) # Baca sampai EoF
    # print(file.read(8)) # Baca sejumlah 8 karakter
    # print(file.readline()) # Baca 1 baris sampai endline (\n)
    x = file.readlines()

    # print(x[1])
    x = map(lambda i : i.replace('\n', ''), x)
    # for i in range(len(x)):
    #     x[i] = x[i].replace('\n', 'X')

    for kata in x:
        print(kata)

# file sudah diclose