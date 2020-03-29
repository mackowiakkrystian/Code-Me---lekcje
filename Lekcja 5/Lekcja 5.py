"""
def mood():
    print("How are you")

mood()
"""

""""

def add_books_to_library():
    books = []
    for k in range(counter):
        title = input("Podaj tytul ksiazki")
        grade = int(input("Podaj ocene ksiazki 1-10"))
        books.append((title, grade))
        print('------------')

    return books

def show_book(books):
    nr = int(input("Podaj nr ksiazki do wyswietlenia "))
    index = nr -1
    if index >= len(books):
        print("nie ma tyle ksiazek")
    else:
        print(f"Twoja ksiazka to {library[index]}")

counter = int(input("Ile ksiazek chcesz podac"))
library = add_books_to_library()
print(library)
show_book(library)
"""
"""
def bmi(height, weight):
    bmi = int(weight)/(float(height*height))

    if bmi <= 18.5:
        print('Your BMI is', bmi,'which means you are underweight.')

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'which means you are normal.')

    elif bmi > 25 and bmi < 30:
        print('Your BMI is', bmi,'which means you are overweight')

    elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')

    else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')

waga = int(input("Podaj wage"))
wzrost = float(input("Podaj wzrost"))
bmi(wzrost, waga)
"""

"""
def max_of2(a, b):
    if a > b:
        return a
    else:
        return b

def maximum_of(a, b, c):
    result = max_of2(a, b)
    max_num = max_of2(c, result)
    return max_num

n1, n2, n3 = 3, 5, 6
print(maximum_of(n1, n2, n3))
"""
"""
def karta(numer):
    if numer[0] == '4':
        if str(len(numer)) == '16':
            print("Vista nowa karta")
        elif str(len(numer)) == '13':
            print("Visa stara karta")
    elif numer[:2] > '50' and numer[:2] < '57' and str(len(numer)) == '16':
        print("Master Card")
    if numer[:4] > '2220' and numer[:4] < '2721' and str(len(numer)) == '16':
            print("Master Card 1")
    elif numer[:2] == '34' or numer[:2] < '37' and str(len(numer)) == '15':
        print("To AMEX")

numer = 2472000000000000

print(karta(str(numer)))
"""


"""
# ZADANIE DOMOWE NR 2
liczba = int(input("Podaj liczbe do sprawdzenia! "))
def sprawdz_czy_liczba_parzysta(liczba):
    if liczba % 2 == 0:
        print("Liczba parzysta")
        return
    else:
        print("Liczba nie jest parzysta")
        return

print(sprawdz_czy_liczba_parzysta(liczba))
"""

"""

#ZADANIE DOMOWE NR 4
liczba = int(input("Podaj liczbe do sprawdzenia! "))

def sprawdz_czy_liczba_parzysta(liczba):
    for i in range(1, liczba):
        if i % 2 == 0:
            print(str(i) + " to liczba parzysta")
        else:
            print(str(i) + " to liczba nie jest parzysta")


print(sprawdz_czy_liczba_parzysta(liczba))
"""

#ZADANIE 6
import random
wyborusera = input("Wybierz papier (1) / kamien (2) / nozyce (3): ")
wyborkomputera = random.choice(['papier', 'kamien', 'nozyce'])

def papierkamiennozyce(wyborusera):
    if (wyborusera.isnumeric() == True) and int(wyborusera) < 4 and wyborusera == '3':
        wyborusera = "nozyce"
    elif wyborusera == '2':
        wyborusera = "kamien"
    elif wyborusera == '3':
        wyborusera = "papier"


    if wyborkomputera == 'papier':
        if wyborusera == 'nozyce':
            print(wyborkomputera + " vs " + wyborusera + ": wygrana usera")
        elif wyborusera == 'kamien':
            print(wyborkomputera + " vs " + wyborusera + ": wygrana komputera")
        else:
            print("REMIS!")
    if wyborkomputera == 'nozyce':
        if wyborusera == 'kamien':
            print(wyborkomputera + " vs " + wyborusera + ": wygrana usera")
        elif wyborusera == 'papier':
            print(wyborkomputera + " vs " + wyborusera + ": wygrana komputera")
        else:
            print("REMIS!")
    if wyborkomputera == 'kamien':
        if wyborusera == 'nozyce':
            print(wyborkomputera + " vs " + wyborusera + ": wygrana komputera")
        elif wyborusera == 'papier':
            print(wyborkomputera + " vs " + wyborusera + ": wygrana usera")
        else:
            print("REMIS!")


print(papierkamiennozyce(wyborusera))