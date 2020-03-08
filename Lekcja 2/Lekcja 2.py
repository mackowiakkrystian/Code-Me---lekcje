dystans = 120
spalanie = 6.4
pb95 = 5.04

koszt = (dystans * 0.01) * spalanie * pb95

print("Koszt wyprawy to " + str(koszt) + '\n')



"""" ZADANIE NR 2
dystans2 = int(input("wprowadz dystans!"))
spalanie2 = float(input("wprowadz spalanie"))
pb952 = float(input("wprowadz koszt benzyny"))

koszt2 = (dystans2 * 0.01) * spalanie2 * pb952
print("Koszt wyprawy to " + str(koszt2))
"""
# ZADANIE NR 3
txt = "wwewWewewe"
print(txt[-1])
print(txt[0:3])
print(txt[2:4])
print(len(txt))
print(txt[3:])
print(txt[3::2])
print(txt.islower())

print("KOLEJNE ZADANIA" + '\n')
text = "teest"
print(text.isnumeric())
text.rstrip()
print(text.count("te"))
print(text.rstrip("t"))
print(not text.islower())

print(text.center(10, "%"))
#ZADANIE 2
ciag = "dwunastka"
ile = len(ciag)
oblicz = ile // 2

print(ciag[oblicz-1:oblicz+2])

#ZADANIE 3
quoute = "Honesty is the first chapter in the book of wisdom."
print(len(quoute))
print(quoute[-7:-1])
polowa = len(quoute) // 2

print(quoute[0:polowa])
print(quoute[-1])
print(quoute[polowa::3])
print(quoute[0::2])
print(quoute[::-1])

print(quoute.replace("wisdom", "friendship"))
""""" ZADANIE 4
tytul = input("Podaj tytul ")
nazwisko = input("Podaj nazwisko autora ")
ilosc_stron = input("Podaj ilosc stron ")
print("Czy tytul nie ma znakow?")
print(not tytul.isnumeric())
print("Czy ilosc stron to cyfry?")
print(not ilosc_stron.isnumeric())
nowytytul = tytul.title()
nowenazwisko = nazwisko.title()
print(nowytytul + " " + nowenazwisko + " " + str(ilosc_stron))
print(len("book"))
"""

""""
#ZADANIE 5
text2 = input("podaj tekst do sprawdzenia czy to palidrom")
text3 = text2.lower()
text = text3.replace(" ", "")
dl = len(text) // 2
lewy = text[0:dl+1]
prawy = text[dl:len(text)]
prawy_konwert = prawy[::-1]
print(lewy == prawy_konwert)
"""

#ZADANIE 6
zmienna = """"
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
print("Policz wystapienia slowa better:")
print(zmienna.count("better"))
print(zmienna.replace("*", ""))
print("zamien jedno wystapienie explain na understand:")
print(zmienna.replace("explain", "understand", 1))
print(zmienna.replace(" ", "-"))

#ZADANIE 7
print("Zjadlem {} zestawow {}".format(5,'obiadowych'))