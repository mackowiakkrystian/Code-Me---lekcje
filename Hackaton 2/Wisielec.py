
slowo_do_odgadniecia = "slowos123"

lista_slowo = list(slowo_do_odgadniecia)
dlugosc = len(slowo_do_odgadniecia)
uzyte = []
ukryte_slowo = []
ukryte_slowo.extend(slowo_do_odgadniecia)

for i in range(len(ukryte_slowo)):
    ukryte_slowo[i] = "_"

ileprob = 1
blad = 0
wynik = False

while ileprob <= dlugosc or blad < 9:
    odpowiedz = input("=======================================================\nWykorzystales nastepujace znaki: " + str(uzyte) + " ||\nZostalo Ci " + str(8-blad) +" szans. Podaj znak: ")
    while odpowiedz in uzyte:
        print("Juz uzyles tego znaku, uzyj innego!")
        odpowiedz = input("Podaj znak: ")
    for k in range(len(lista_slowo)):
        if lista_slowo[k] == odpowiedz:
            ukryte_slowo[k] = odpowiedz
            wynik = True
    if wynik == False:
        blad += 1
    wynik = False
    ileprob += 1
    uzyte.append(odpowiedz)
    print(' '.join(ukryte_slowo))

    if blad == 1:
        print("\n" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n")
    elif blad == 2:
        print("\n=====================" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n")
    elif blad == 3:
        print("\n=====================" + "\n|                   |" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n")
    elif blad == 4:
        print("\n=====================" + "\n|                   |" + "\n|                  O" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n")
    elif blad == 5:
        print("\n=====================" + "\n|                   |" + "\n|                  O" + "\n|                   |" + "\n|" + "\n|" + "\n|_______________________\n")
    elif blad == 6:
        print("\n=====================" + "\n|                   |" + "\n|                  O" + "\n|               ---|" + "\n|" + "\n|" + "\n|_______________________\n")
    elif blad == 7:
        print("\n=====================" + "\n|                   |" + "\n|                  O" + "\n|               ---|---" + "\n|" + "\n|" + "\n|_______________________\n")
    elif blad == 8:
        print("\n=====================" + "\n|                   |" + "\n|                  O" + "\n|               ---|---" + "\n|                  /" + "\n|                /" + "\n|_______________________\n")
    else:
        blad == 9

else:
    print('\n=====================" + "\n|                   |" + "\n|                  O" + "\n|               ---|---" + "\n|                  /\\" + "\n|                /    \\" + "\n|_______________________')