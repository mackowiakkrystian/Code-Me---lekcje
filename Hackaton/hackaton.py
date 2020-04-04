# ZADANIE KSIAZKA ADRESOWA
ksiazka = {}
ksiazka = {1: {'Jurek': '603258222'}}
ksiazka[2] = {'Marek': '333333333'}
quit = False
while quit == False:
    menu = input("Wybierz zadanie:\n (1) Dodawanie nowego wpisu \n (2) Usuwanie wpisu \n (3) Wyswietl wszystko \n (Q) Zakoncz program \n")
    if menu == "1":
        dodajimie = input("Podaj nazwe imie: ")
        dodajtelefon = input("Podaj numer telefonu: ")
        if (dodajtelefon.isnumeric() == True) and (len(dodajtelefon) == 9):
            print("Uzytkownik: "+ dodajimie.capitalize() + " zostal dodany do ksiazki adresowej z numerem telefonu: " +dodajtelefon + " \n ===================")
            nextitem = len(ksiazka) + 1
            ksiazka[nextitem] = {dodajimie: dodajtelefon}
        else:
            print("W polu nr telefonu mogą byc tylko znaki o dlugosci 9 cyfr!  \n ===================")

    elif menu == "2":
        print("Ponizej wszystkie adresy w ksiazce. Wybierz element do skasowania podany w nawiasie: \n")
        for i, v in ksiazka.items():
            numer = i
            for key in v:
                print("[" + str(numer) +"]. " + key + ": " + v[key])
        doskasowania = int(input(""))
        pytanie = input("Na pewno chcesz skasowac element >>" + str(ksiazka[doskasowania]) + "? T/N ")
        if pytanie == "T" or "t":
            del ksiazka[doskasowania]
            print("Skasowano wpis! \n ===================")
        else:
            print("Przerwano proces kasowania! \n ===================")

    elif menu == "3":
        print("Ponizej wszystkie adresy w ksiazce: ")
        for i, v in ksiazka.items():
            numer = i
            for key in v:
                print("[" + str(numer) + "]. " + key + ": " + v[key])
        print(" \n ===================")
    elif menu == "Q" or "q":
        quit = True


# ZADANIE WOJNA
from random import randint
talia_kart = [2,3,4,5,6,7,8,9,10,11,12,13,14]
talia_komputera = []
talia_uzytkownika = []


for i in range(0, len(talia_kart)):
    los = randint(0, len(talia_kart)-1)
    talia_komputera.append(talia_kart[los])
    talia_kart.pop(los)
    if(len(talia_kart) != 0 ):
        los = randint(0, len(talia_kart)-1)
        talia_uzytkownika.append(talia_kart[los])
        talia_kart.pop(los)
    else:
        break

nrrundy = 1
scorecomputer = 0
scoreuser = 0
trybgry = input("Ktory tryb gry chcesz zagrac? \n (1) Karty beda odkladane na koniec stosu gracza \n (2) Karty sa odkladane nie wykorzystywane wiecej razy \n ########################### \n")
if trybgry == "1":
    for k in range(0, 10):
        if (len(talia_uzytkownika) != 0) and (len(talia_komputera) != 0):
            print("Runda nr: " + str(nrrundy) + ": Komputer ma karte: " + str(talia_komputera[0]) + " Uzytkownik ma karte: " + str(talia_uzytkownika[0]))
            if talia_komputera[0] > talia_uzytkownika[0]:
                scorecomputer = scorecomputer + 1
                talia_komputera.insert(len(talia_komputera), talia_uzytkownika[0])
                talia_komputera.insert(len(talia_komputera), talia_komputera[0])
                talia_komputera.pop(0)
                talia_uzytkownika.pop(0)
            else:
                talia_uzytkownika.insert(len(talia_uzytkownika), talia_uzytkownika[0])
                talia_uzytkownika.insert(len(talia_uzytkownika), talia_komputera[0])
                scoreuser = scoreuser + 1
                talia_komputera.pop(0)
                talia_uzytkownika.pop(0)
            print("Komputer - " + str(scorecomputer) + " : " + str(scoreuser) + " - User ")
        else:
            break
        nrrundy = nrrundy+1

    print("")
    print("Karty ktore zostaly komputerowi: " +str(talia_komputera))
    print("Karty ktore zostaly uzytkownikowi: " + str(talia_uzytkownika))

elif trybgry == "2":
    for k in range(0, 10):
        if (len(talia_uzytkownika) != 0) and (len(talia_komputera) != 0):
            print("Runda nr: " + str(nrrundy) + ": Komputer ma karte: " + str(
                talia_komputera[0]) + " Uzytkownik ma karte: " + str(talia_uzytkownika[0]))
            if talia_komputera[0] > talia_uzytkownika[0]:
                scorecomputer = scorecomputer + 1
                talia_komputera.pop(0)
                talia_uzytkownika.pop(0)
            else:
                scoreuser = scoreuser + 1
                talia_komputera.pop(0)
                talia_uzytkownika.pop(0)
            print("Komputer - " + str(scorecomputer) + " : " + str(scoreuser) + " - User ")
        else:
            break
        nrrundy = nrrundy + 1

    print("")
    print("Karty ktore zostaly komputerowi: " + str(talia_komputera))
    print("Karty ktore zostaly uzytkownikowi: " + str(talia_uzytkownika))
else:
    print("Wybrano nieprawidlowy tryb gry!")


# Historyjka RPG - NIE MAM POMYSLU NA NAZWY, DLATEGO ZROBIE GENERATOR WYPOWIEDZI JANUSZA KORWINA MIKKE'GO
from random import randint
jeden = ['Ja chce powiedziec jedna rzecz', 'Trzeba powiedziec jasno:', 'Jak powiedzial wybitny krakowianin Stanislaw Lem', 'Prosze mnie dobrze zrozumiec:', 'Ja chcialem Panstwu przypomniec, ze', 'Niech panstwo nie maja zludzen', 'Powiedzmy to wyraznie:']
dwa = ['przedstawiciele czerwonej holoty', 'ci wszyscy (tfu!) geje', 'funkcjonariusze rezimowej telewizji', 'tak zwani ekolodzy', 'ci wszyscy (tfu!) demokracji', 'agenci bezpieki', 'feminazistki']
trzy = ['zupelnie bezkarnie', 'calkowicie bezczelnie', 'o pogladach na lewo od komunizmu', 'celowo i swiadomie', 'z premedytacja', 'od czasow Okraglego stolu', 'w ramach postepu']
cztery = ['nawoluja do podniesienia podatkow', 'probuja wyrzucic kierowcow z miast', 'probuja sklocic Polske z Rosja', 'glosza brednie o globalnym ociepleniu', ' zakazuja posiadania broni', 'nie dopuszczaja prawicy do wladzy', 'ucza dzieci homoseksualizmu']
piec = ['bo dzieki temu moga krasc', 'bo dostaja za to pieniadze', 'bo tak sie uczy w panstwowej szkole', 'bo bez tego (tfu!) demokracja nie moze istniec', 'bo glupich jest wiecej niz madrych', 'bo chca tworzyc raj na ziemi', 'bo chca niszczyc cywilizacje bialego czlowieka']
szesc = ['przez kolejne kadencje.', 'o czym sie nie mowi.', 'i wlasnie dlatego Europa umiera.', 'ale przyjda muzulmanie i zrobia porzadek.', '- tak samo zreszta jak za czasow Hitlera.', '- prosze zobaczyc co sie dzieje na Zachodzie, jesli mi panstwo nie wierza.', 'co lat temu sto nikomu nie przyloby nawet do glowy.']

print("#### GENERATOR WYPOWIEDZI Janusza Korwina Mikke ####")
print(jeden[randint(0, len(jeden)-1)] + " " + dwa[randint(0, len(dwa)-1)] + " " + trzy[randint(0, len(trzy)-1)] + " " + cztery[randint(0, len(cztery)-1)] + " " + piec[randint(0, len(piec)-1)] + " " + szesc[randint(0, len(szesc)-1)])

# GENERATOR IMIENIA RPG
from random import randint
samogloski = ['a','e','i','o','u','y']
spolgloski = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','w','z']
liczebniki = ['I', 'II', 'III', 'IV', 'V']
przydomki = ['Wielki', 'Maly', 'Niemrawy', 'Bojazliwy', 'Smialy', 'Chorobliwy']

nazwa = ''
licznik = 1
dlugosc = input("Podaj dlugosc imienia!: ")
for i in range(int(dlugosc)):
    losuj_samo = randint(0, len(samogloski)-1)
    losuj_spol = randint(0, len(spolgloski)-1)
    if int(dlugosc) % 2 == 0:
        if licznik == 1:
            nazwa = samogloski[losuj_samo] + nazwa
            licznik = licznik + 1
        else:
            nazwa = spolgloski[losuj_spol] + nazwa
            licznik = 1
    else:
        if licznik == 1:
            nazwa = spolgloski[losuj_spol] + nazwa
            licznik = licznik + 1
        else:
            nazwa = samogloski[losuj_samo] + nazwa
            licznik = 1

print("Wygenerowana nazwa: " + nazwa.capitalize() + " " + liczebniki[randint(0, len(liczebniki)-1)] + " " + przydomki[randint(0, len(przydomki) - 1)])

#ZADANIE QUIZ - NIE JEST DOKONCZONE
#
# pytanie = {}
# pytanie = {'Biologia': {'Co to jest dab?': {'1': 'Roslina', '2': 'zwierze'}},
#            'Biologia': {'Ile nog ma pies?': {'1': 'Cztery', '2': 'Piec'}},
#            'Ekonomia': {'Co to PKB?': {'1': 'Polska Kraina Bezrobocia', '2': 'Produkt Krajowy Brutto'}}}
# poprawneodpowiedzi = ['1', '1', '2']
#
# category = input("Wybierz kategorie:")
#
# for i, e in pytanie.items():
#     for k, m in e.items():
#         print(category)
# print(pytanie['Biologia'])
#
# # for i, e in pytanie.items():
# #     print(i)
# #     for k, m in e.items():
# #         print("Kategoria: " + str(k))
# #         for w, x in m.items():
# #             print("Pytanie: " +str(w))
# #             for j in x:
# #                 print("Nr odpowiedzi:" + str(j))
# #                 print("Odpowiedz: " + str(x[j]))




