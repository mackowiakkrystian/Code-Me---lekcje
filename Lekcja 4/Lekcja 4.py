veggies  = ['carrot', 'aale', 'peas']
nowa = veggies.copy()
ile = veggies.count('carrot')

print(ile)
# DEEP COPY, SHADOW COPY - porownac

tablica_wielowymiarowa =  [[1, 0, 3],
                            [3, 2, 1],
                            [4, 6, 4]]

print(tablica_wielowymiarowa)
print(tablica_wielowymiarowa[2])

print("\n >>Zadanie nr 1")

rzeczy = []
rzeczy.append('jedzenie')
rzeczy.append('latarka')
rzeczy.append('kompas')

print(rzeczy)
posortowane = sorted(rzeczy)
print(posortowane)
"""
print(">> Zadanie 3")

i=1
lista = []
for i in range(5):
   answer = lista.append(input("podaj nazwe: "))

if lista[0] == lista[len(lista)-1]:
    print("to samo")
else:
    print("inne liczby")
"""
"""
ALBO
if lista[0] = lista[-1]... """

print("\n \n>> ZADANIE 5")

osoby = [['Dorota', 'Adam', 'Robert', 'Krystyna'],
        ['Wellman', 'Malysz', 'Lewandowski', 'Janda'],
        ['dziennikarka', 'sportowiec', 'pilkarz', 'aktorka']]
print(osoby[0][2] + " " + osoby[1][2])

for row in osoby:
    print(osoby[1])
print("\n")

for row in osoby:
    print(f"{row[0]} {row[1]} - {row[2]}")

print("\n")

for row in osoby:
    print(" * ".join(row))

print("\n >> Zadanie 4")
my_tuple = ('a', 3.4, 77)
# usuwanie krotek? Nie mozna, ale mozna zamienic na liste, a to mozna usunac
temp_list = list(my_tuple)
temp_list.remove(77)
my_tuple = tuple(temp_list)

print("\n >> ZESTAWY")
my_set = {1,2,3,1}

my_set.discard(5) #usuwa element, ale nie wywala bledu jesli nie ma klucza
print(my_set)

print("\n >> ZADANIE 3")
krotka1 = ('polska', 'niemcy', 'Portugalia')
krotka2 = ('poznan', 'berlin', 'Lizbona')

rezultat = krotka1[::2] + krotka2[1::2]
print(set(rezultat))

print("\n >> ZADANIE 1 Słowniki")
list_to_dict = [['Niemcy', 'Polska'], ['Berlin', 'Warszawa']]
zamianka = dict(list_to_dict)
print(zamianka)

print("\n >> ZADANIE 5")
zdanie = """Szybko, zbudź się, szybko, wstawaj
            Szybko, szybko, stygnie kawa
            Szybko, zęby myj i ręce"""

""" ZROBIC!!!
1. replace przecinki
2. wszystko do malych
3. dzielenie na podstawie spacji i wrzucenie do listy
"""