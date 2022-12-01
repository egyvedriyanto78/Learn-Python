def elim(n):
    list = []
    for number in n:
        if number not in list:
            list.append(number)
    return list

angka = input('Masukkan angka : ')
value = [int(num) for num in angka.split(' ') if len(num) > 0]
print('Angka yang berbeda adalah : ', (elim(value)))