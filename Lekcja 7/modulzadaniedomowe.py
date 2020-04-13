from math import sqrt
def rozwiazdelte(a, b, c):
    print("Rowanie kwardatowe \nax^2+bx+c")

    if a == b == c == 0:
        print("a, b, c = 0 - brak rownania")
    else:
        print("Sprawdzam parametr a")
        if a > 0 or a < 0:
            print("> 0\nRownanie typu ax^2+bx+c")
            delta = b**2-(4*a*c)
            print("Delta = %d" % (delta))
            if delta == 0:
                x0=(b*b/4*a)
                print("Delta=0, obliczam x=%d" % (x0))
            elif delta > 0:
                x1=(b*b-sqrt(delta)/4*a)
                x2=(b*b+sqrt(delta)/4*a)
                print("Obliczam x1,x2: x1=%d ; x2=%d" % (x1, x2))
            elif delta < 0:
                print("Delta<0 brak piewriastkow")
        elif a == 0:
            print(" = 0 \n Rownanie typu bx+c")
            x=(-c/b)
            print("Wynik x=-%d/%d" % (c, b))
    print("Koniec")

##########
##########
from random import randint
import random



def zadanie6(jakdlugie):
    ciagznakow = ''

    for i in range(jakdlugie):
        if jakdlugie < 10:
            if i == jakdlugie-1:
                ciagznakow += ciagznakow[:1]
            else:
                ciagznakow += str(randint(0, 9))
        else:
            ciagznakow += str(randint(0, 9))

    print(ciagznakow)

###########################
def zadanie6b():
    znaki = []
    koniec = "no"

    print("\n\nWpisz 'koniec' aby zakonczyc dodawanie znakow:")
    while koniec == "no":
        wprowadzone = input("Podaj znak do generatora: ")
        if wprowadzone != "koniec":
            znaki.append(wprowadzone)
        else:
            koniec = "yes"

    ileznakow = int(input("Jak dlugi ma byc ciag? "))
    polaczoneslowo = ''
    for n in range(ileznakow):
        losowe = random.choice(znaki)
        polaczoneslowo += losowe

    print("Wygenerowany ciag o dlugosci {} znakow: {}".format(ileznakow, polaczoneslowo))

#############
# ZADANIE 7 #
#############

def zadanie7():
    ciag = int(input("Podaj wartosc n: "))
    poprzedni = '1'
    poprzedni2 = '0'
    if ciag == "0":
        wynik = '0'
        print("Wynik to {} przy podanej wartosci n: {}.".format(wynik, ciag))
    elif ciag == "1":
        wynik = '1'
        print("Wynik to {} przy podanej wartosci n: {}.".format(wynik, ciag))
    else:
        for i in range(0, ciag - 1):
            wynik = int(poprzedni) + int(poprzedni2)
            poprzedni2 = poprzedni
            poprzedni = wynik

        print("Wynik to {} przy podanej wartosci n: {}.".format(wynik, ciag))