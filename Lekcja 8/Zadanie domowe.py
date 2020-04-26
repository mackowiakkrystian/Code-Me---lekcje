#ZADANIE 2
# liczby = ("1", "2", "4", "8")
# wybor = input("Podaj indeks krotki do podmianki")
# podmianka = input("Podaj nowa wartosc")
# try:
#     liczby[wybor] = str(podmianka)
#     print(liczby[2])
# except TypeError as blad:
#     print("blad przypisania wartosci do krotki: ", blad)


#ZADANIE 4
# lista = []
# nowa = input("Podaj pare liczb do tablicy aby wyliczyc srednia oddzielajac wszystko przecinkiem! ")
#
# lista = nowa.split(",")
# print(lista)
#
#
# suma = 0
# for i in range(0, len(lista)):
#     try:
#         suma = suma + int(lista[i])
#     except ValueError as val:
#         with open("Errors.txt", "w") as text_file:
#             text_file.write(str(val))
#
# srednia = suma / len(lista)
# print("Srednia to: " + str(srednia))

#ZADANIE 6
# try:
#     with open("Errors2.txt", "r") as text_file:
#         tresc = text_file.read()
# except FileNotFoundError as file1:
#     print("Blad typu: " + str(file1))
#
# import io
# try:
#     with open("Errors.txt", "w") as text_file:
#         tresc = text_file.read()
# except io.UnsupportedOperation as file2:
#     print("Blad typu: " + str(file2))
#
# try:
#     with open("Errors.txt", "x") as text_file:
#         tresc = text_file.read()
# except FileExistsError as file3:
#     print("Blad typu: " + str(file3))

#ZADANIE 8 - MOJ PRZYKLAD Z HACKATONU

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
            try:
                print("Uzytkownik: "+ dodajimie.capitalize() + " zostal dodany do ksiazki adresowej z numerem telefonu: " +dodajtelefon + " \n ===================")
                nextitem = len(ksiazka) + 1
                ksiazka[nextitem] = {dodajimie: dodajtelefon}
            except:
                print("wystapil wyjatek!")
        else:
            print("W polu nr telefonu mogą byc tylko znaki o dlugosci 9 cyfr!  \n ===================")

    elif menu == "2":
        print("Ponizej wszystkie adresy w ksiazce. Wybierz element do skasowania podany w nawiasie: \n")
        for i, v in ksiazka.items():
            numer = i
            for key in v:
                print("[" + str(numer) +"]. " + key + ": " + v[key])
        try:
            doskasowania = int(input(""))
            pytanie = input("Na pewno chcesz skasowac element >>" + str(ksiazka[doskasowania]) + "? T/N ")
            if pytanie == "T" or "t":
                del ksiazka[doskasowania]
                print("Skasowano wpis! \n ===================")
            else:
                print("Przerwano proces kasowania! \n ===================")
        except:
            print("Wystapil wyjatek!")
    elif menu == "3":
        print("Ponizej wszystkie adresy w ksiazce: ")
        for i, v in ksiazka.items():
            numer = i
            for key in v:
                print("[" + str(numer) + "]. " + key + ": " + v[key])
        print(" \n ===================")
    elif menu == "Q" or "q":
        quit = True