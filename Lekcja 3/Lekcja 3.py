# INSTRUKCJE STERUJACE
# ZADANIA Z TABLICY
dish = "gzisk"
if dish == "gzik":
    print("wielkopolskie")

elif dish == "ziemniaki":
    print("mazowieckie")

else:
    print("Podlasie")

#ZADANIE 1
""""
liczba = input("Podaj liczbe ")
if int(liczba) % 3 == 0:
    print("Twoja liczba jest podzielna przez 3!")
"""

#ZADANIE 3
"""
print("Ocen ksiazke! (1-10)")
ocena1 = int(input("Ocena nr 1"))
ocena2 = int(input("Ocena nr 2"))
ocena3 = int(input("Ocena nr 3"))

srednia = (ocena1 + ocena2 + ocena3) / 3
print(srednia)
if srednia > 7:
    print("Ocena to bardzo dobry!")
elif srednia > 5 and srednia <= 7:
    print("Ocena przecietna")
else:
    print("Ocena nie warta uwagi")
"""
#ZADANIE 4
zmienna = "Polaczka"

if len(zmienna) > 5:
    if 'a' in zmienna:
        print("Nowy tekst: " + zmienna.replace('a', 'z'))

print("Stary tekst: " + zmienna + "\n\n")

#ZADANIE 5
"""
password = input("podaj haslo! ")


if len(password) < 8:
    print("Haslo jest za krotkie! Minimum 8 znakow!")
elif not any(char.isdigit() for char in password):
    print('Haslo musi miec co najmniej 1 cyfre')
elif not any(char.isupper() for char in password):
    print('Haslo musi miec co najmniej 1 znak duzy')
else:
    print("Haslo poprawne!")
"""
"""
#ZADANIE 7
wzrost = float(input("Podaj swoj wzrost! "))
waga = int(input("Podaj swaja wage "))
bmi = waga / (wzrost * wzrost)

print("Twoje BMI to: " + str(round(bmi,2)))
if bmi < 19:
    print("Masz niedowage!")
elif bmi >19 and bmi < 25:
    print("Masz prawidlowa wage!")
elif bmi >25 and bmi <30:
    print("Masz nadwage!")
else:
    print("Otylosc!")
"""

"""
# PETLE FOR
letter = "tekscik"
for znak in letter:
    print("-", znak)
"""
"""
lista = ("Krystian", "Ania", "Marek")
for x in lista:
    print(x)
"""


"""
pa = ""
magic = "hokuspokus"
for num in range(1, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)
"""
"""
#ZADANIE 1 PETLE FOR

listaprzedmiotow = ("Latarka", "konserwy", "banan")
for i in listaprzedmiotow:
    print(i)
print("Great, we are ready! \n\n")

#ZADANIE 2 PETLE FOR
skladniki = ("parowka", "bulka", "keczup")
for j in skladniki:
    print("Dodaj: " + j)
print("1. Rozetnij bulke \n2. Wloz parowke \n3. Polej keczupem \n \n")

#ZADANIE 3 PETLE FOR
wynik = 1
zmienna2 = 1
for k in range(2, 11):
    zmienna2 = k + zmienna2
    print(zmienna2)
"""
"""
#ZADANIE 4 PETLE FOR
silnia = input("Podaj silnie! ")
for r in range(1, int(silnia)+1):
    wynik = r * wynik

print("Silnia z " + str(silnia) + " to: " + str(wynik))
"""

"""
#ZADANIE NA TABLICY WHILE
iteracja = 1
szkola = {}

while iteracja < 4:
    subject = input("Przedmiot szkolny: ")
    grade = input("Ocena w skali 1-6: ")
    szkola[subject] = grade
    iteracja = iteracja + 1

for h in szkola:
    ocenki = szkola[h]
    for g in ocenki:
        print(szkola[h])
        
        
"""

#ZADANIE 1 WHILE

ile = 0
while ile < 201:

    wzor = (5/9) * (ile - 32)
    print("C to: "+str(ile)+" Faht to -" + str(wzor))
    ile = ile + 20

#ZADANIE 2 WHILE
print("\n\n")
zagadka = "19"
odpowiedz = input("Podaj liczbe od 1-20. Sprobuj zgadnac!")

while odpowiedz != zagadka:
    print("Zle! Sprobuj jeszcze raz!")
    odpowiedz = input("Podaj jeszcze raz liczbe!")
print("Dobrze, zgadles!")
