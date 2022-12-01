import os

def trend():
    os.system('cls')
    mangas= ["01. One Piece",
             "02. Chainsaw man",
             "03. One Punch Man",
             "04. Black Clover",
             "05. Spy x Family",
             "06. Kakkou no Iinazuke",
             "07. Yofukashi no Uta",
             "08. Jujutsu Kaisen",
             "09. Demon Slayer",
             "10. Yakusoku no Neverland"]
    print('\nTOP 10 Manga on the week')
    for i in range(10):
        print(mangas[i])
    print("="*25)    
    detail = input("\ninfo detail nomor : ")
    if detail == '1':
        os.system('cls')
        print("One Piece\n")
        print("Genre\t\t: Adventure, Fantasy, Shounen.\n"+
              "Tahun\t\t: 1997\n"+
              "Pengarang\t: Eiichiro Oda\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 1055\n"+
              "Link\t\t: https://mangaplus.shueisha.co.jp/titles/100140\n")
    elif detail == '2':
        os.system('cls')
        print("Chainsaw man\n")
        print("Genre\t\t: Action, Horror comedy, Dark Fantasy.\n"+
              "Tahun\t\t: 2018\n"+
              "Pengarang\t: Tatsuki Fujimoto\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 107\n"+
              "Link\t\t: https://mangaplus.shueisha.co.jp/titles/100037\n")
    elif detail == '3':
        os.system('cls')
        print("One Punch Man\n")
        print("Genre\t\t: Action, Comedy, Superhero, Fiction.\n"+
              "Tahun\t\t: 2009\n"+
              "Pengarang\t: Yusuke Murata\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 221\n"+
              "Link\t\t: https://mangadex.org/title/d8a959f7-648e-4c8d-8f23-f1f3f8e129f3/one-punch-man\n")
    elif detail == '4':
        os.system('cls')
        print("Black Clover\n")
        print("Genre\t\t: Action, Adventure, Comedy, Fantasy, Shounen.\n"+
              "Tahun\t\t: 2015\n"+
              "Pengarang\t: Yuki Tabata\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 341\n"+
              "Link\t\t: https://mangaplus.shueisha.co.jp/titles/100141\n")
    elif detail == '5':
        os.system('cls')
        print("Spy x Family\n")
        print("Genre\t\t: Action, Comedy, Fiction, Spy.\n"+
              "Tahun\t\t: 2019\n"+
              "Pengarang\t: Tatsuya Endou\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 68\n"+
              "Link\t\t: https://mangaplus.shueisha.co.jp/titles/100143\n")
    elif detail == '6':
        os.system('cls')
        print("Kakkou no Iinazuke\n")
        print("Genre\t\t: Harem, Romance, Comedy.\n"+
              "Tahun\t\t: 2020\n"+
              "Pengarang\t: Miki Yoshikawa\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 130\n"+
              "Link\t\t: https://mangadex.org/title/4e7a4a0f-8391-4069-839b-de2352297dab/a-couple-of-cuckoos\n")
    elif detail == '7':
        os.system('cls')
        print("Yofukashi no Uta\n")
        print("Genre\t\t: Romance, Comedy, Supernatural, Fiction.\n"+
              "Tahun\t\t: 2019\n"+
              "Pengarang\t: Kotoyama\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 145\n"+
              "Link\t\t: https://mangadex.org/title/259dfd8a-f06a-4825-8fa6-a2dcd7274230/yofukashi-no-uta\n")
    elif detail == '8':
        os.system('cls')
        print("Jujutsu Kaisen\n")
        print("Genre\t\t: Adventure, Fiction, Dark Fantasy, Supranatural.\n"+
              "Tahun\t\t: 2018\n"+
              "Pengarang\t: Gege Akutami\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 201\n"+
              "Link\t\t: https://mangaplus.shueisha.co.jp/titles/100034\n")
    elif detail == '9':
        os.system('cls')
        print("Demon Slayer\n")
        print("Genre\t\t: Adventure, Fiction, Dark Fiction, Martial arts.\n"+
              "Tahun\t\t: 2016\n"+
              "Pengarang\t: Koyoharu Gatouge\n"+
              "Status\t\t: Completed\n"+
              "Chapter\t\t: 205\n"+
              "Link\t\t: https://mangaplus.shueisha.co.jp/titles/100009\n")
    elif detail == '10':
        os.system('cls')
        print("Yakusoku no Neverland\n")
        print("Genre\t\t: Horror, Mystery, Psychological, Shounen, Supernatural.\n"+
              "Tahun\t\t: 2016\n"+
              "Pengarang\t: Kaiu Shirai\n"+
              "Status\t\t: Completed\n"+
              "Chapter\t\t: 183\n"+
              "Link\t\t: https://mangadex.org/title/46e9cae5-4407-4576-9b9e-4c517ae9298e/yakusoku-no-neverland?tab=chapters&page=3\n")
    else:
        os.system('cls')
        trend()
    
    balik = input("\nBack to menu? ")
    if balik == 'y' or 'Y':
        os.system('cls')
        main_menu()

def search():
    os.system('cls')
    komik = ["One Piece",
             "Chainsaw man",
             "One Punch Man",
             "Black Clover",
             "Spy x Family",
             "Kakkou no Iinazuke",
             "Yofukashi no Uta",
             "Jujutsu Kaisen",
             "Demon Slayer",
             "Yakusoku no Neverland"]
    
    print('\n-- Search manga by genre --\n')
    genre= ["1. Action",
            "2. Fantasy",
            "3. Romance",
            "4. Comedy"]
    
    #a = [1,2,3,4,7]
    #b = [0,1,3,7]
    #c = [5,6]
    #d = [0,2,3,4,5,6]
    
    for i in range(4):
        print(genre[i])
    
    choose = input("\npilih : ")
    if choose == '1':
        os.system('cls')
        print("Action--")
        print(komik[1]+'\n'+komik[2]+'\n'+komik[3]+'\n'+komik[4]+'\n'+komik[7])
        b = input('\nback? ')
        if b == 'y' and 'Y':
            os.system('cls')
            main_menu()
    elif choose == '2':
        os.system('cls')
        print("Fantasy--")
        print(komik[0]+'\n'+komik[1]+'\n'+komik[3]+'\n'+komik[7])
        b = input('\nback? ')
        if b == 'y' and 'Y':
            os.system('cls')
            main_menu()
    elif choose == '3':
        os.system('cls')
        print("Romance--")
        print(komik[5]+'\n'+komik[6])
        b = input('\nback? ')
        if b == 'y' and 'Y':
            os.system('cls')
            main_menu()
    elif choose == '4':
        os.system('cls')
        print("Comedy--")
        print(komik[0]+'\n'+komik[2]+'\n'+komik[3]+'\n'+komik[4]+'\n'+komik[5]+'\n'+komik[6])
        b = input('\nback? ')
        if b == 'y' and 'Y':
            os.system('cls')
            main_menu()
    else:
        os.system('cls')
        search()
   
def main_menu():
    # membuat daftar menu
    print('=' * 40)
    print('Welcome to Anaconda Manga Corner')
    print('=' * 40)
    print('1. Trending Manga')
    print('2. Search Manga')
    print('3. Exit')
 
    # input pilihan
    pilihan = input('\npilih menu: ')
 
    # pilihan menu
    if pilihan == '1':
        trend()
    elif pilihan == '2':
        search()
    elif pilihan == '3':
        print('Program EXIT')
        exit()
    else:
        os.system('cls')
        main_menu()

# fungsi login
def get_login():
    while True:
        try:
            print('=' * 40)
            print('Login Anaconda Account')
            username = (input('username : ')).upper()
            password = int(input('password : '))
            os.system('cls')
            if username == 'ANACONDA' and password == 117013:
                break
        except:
            os.system('cls')
    os.system('cls')
    main_menu()

# main program
if __name__=='__main__':
    get_login()