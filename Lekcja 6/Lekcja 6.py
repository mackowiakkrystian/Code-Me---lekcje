"""
with open('test.txt', 'r') as fopen:
    content = fopen.read()
    print(content)
"""
"""

with open('test.txt', 'r') as fopen:
  while True:
    current_line = fopen.readline()
    # aktualna linia jest pusta
    if current_line == '':
      # dotarlismy do konca
      break
    print(current_line)


with open('save.txt', 'w') as f:
  f.write('Line 1')
  f.write('Line 2')
  f.write('Line 3')
  f.write('Line 4')




sweets_list = ['chocolate', 'lollipop', 'cookie', 'candy']

with open('save.txt', 'w') as f:
    f.write('\n'.join(sweets_list))

print("\n\n")
import os.path

if os.path.isfile('save.txt'):
    print ("File exist")
else:
    print ("File not exist")


with open('shakespeare.txt', 'w') as fopen:
  message = 'Be or Not To Be'
  print(message) # wyswietli na standardowe wyjście
  print(message, file = fopen) # zapis do pliku
  # Można ustawić zarówno parametr file i wyświetlić wartość na ekrani
  # potrzebujemy przekazać wartość None, bezpośrednio lub za pomocą zmiennej
  nofile = None
  print(message, file = nofile) # wyswietli na standardowe wyjście
  print(message, file = None)

"""
"""
import random

plik = input("Podaj nazwe pliku z cytatami")
with open(str(plik)+'.txt', 'r') as fopen:
  lines = fopen.readlines()
  losowana_liczba = random.randint(1, len(lines))

autor = lines[losowana_liczba-1].split(".")

print('*' *70)
print(autor[0] + "\n" + autor[1])
print('*' *70)
"""
"""

with open('pantadeusz.txt', 'r') as fopen:
  lines = fopen.read()

max = ''
slowo = lines.split()

for i in slowo:
    if len(i) > len(max):
        max = i
print(slowo)
print(max)


"""
"""

def is_card_number(number):
    return number.isdecimal() and len(number) in [13, 15, 17]

def starts_with_correct_digits(number):
    if 51 <= int(number[0:2]) <= 55:
        return True
    elif 2221 <= int(number[0:4]) <= 2720:
        return True
    else:
        return False

def show_card_type(number):
    if len(number) in [13, 17] and number[0] == '4':
        print("To jest VISA")

    elif len(number) == 16 and starts_with_correct_digits(number):
        print("To jest MasterCard")

    elif len(number) == 15 and (number[0:2] in ['34', '37']):
        print("To jest AMEX")
    else:
        print("Nie znam typu karty")

with open('cards.txt') as fopen:
    cards = fopen.read()
    cards = cards.split()



nr_card = '43234243233733333'
if is_card_number(nr_card):
    show_card_type(nr_card)
else:
    print('to nie jest nr karty')

"""

# # ZADANIE NR 7 WISIELEC - NIE DZIALA POPRAWNIE, UTKNALEM.
# # ZLE POKAZUJE ILOSC KRESEK JESLI SLOWO MA 2 LUB WIECEJ TAKICH SAMYCH ZNAKOW ORAZ SLOWO NIE KONCZY SIE NA TEN ZNAK
# # NP DLA SLOWA "ANANAS" TAKIE ZNAKI WYKRZACZAJA PROGRAM: "A" LUB "N"

# from random import randint
#
# with open('wisielec.txt', 'r') as fopen:
#     content = fopen.read().splitlines()
#
#     start = 1
#     kategorie = ''
#
#     slownik = {}
#     kategorie = {}
#
#
#
#     for i in content:
#         if i.find(".") == 0:
#             slownik[i] = {}
#             start = 1
#             nazwakategorii = i
#
#         else:
#             slownik[nazwakategorii][start] = i
#             start = start + 1
#
#     print(slownik)
#
#     for k, w in slownik.items():
#         print(k)
#         for s in w:
#             print(w[s])
#
#     print("#######################")
#
#
#     kategoria = input("Podaj kategorie: zwierzeta albo owoce ")
#
#     losowanie = randint(1, len(slownik['.' + str(kategoria)]))
#     wylosowane_slowo = slownik['.' + kategoria][losowanie]
#
#     wisielec = ''
#     ilerazy = 0
#     napotkal = 0
#     odznaku = 0
#
#     len(wylosowane_slowo)
#     print(wylosowane_slowo)
#     proba = input("Podaj znak! ")
#     if proba in wylosowane_slowo:
#         gdzie = [pos for pos, char in enumerate(wylosowane_slowo) if char == proba]
#         print(gdzie)
#
#         for iteracja in range(1, len(wylosowane_slowo)+1):
#             napotkal = 0
#             ilerazy = 1
#             for ile in range(odznaku, len(gdzie)):
#                 pozycjaznaku = gdzie[ile]
#                 pozycjaznakuostateczna = pozycjaznaku + 1
#
#                 if len(gdzie) > 1:
#                     if pozycjaznakuostateczna == iteracja:
#                         if ilerazy != 1 or napotkal == 1:
#                             break
#                         else:
#                             wisielec = wisielec + proba
#                             ilerazy = ilerazy
#                             napotkal = 1
#                             odznaku = odznaku + 1
#                             break
#                     else:
#                         if ilerazy != 1 or napotkal == 1:
#                             break
#                         else:
#                             wisielec = wisielec + " _ "
#                             ilerazy = ilerazy + 1
#                 else:
#                     if pozycjaznakuostateczna == iteracja:
#                         if ilerazy != 1:
#                             break
#                         else:
#                             wisielec = wisielec + proba
#                             ilerazy = ilerazy + 1
#                             if len(gdzie) != 1:
#                                 break
#                     else:
#                         if ilerazy != 1:
#                             break
#                         else:
#                             wisielec = wisielec + " _ "
#                             ilerazy = ilerazy + 1
#
#     else:
#         print("brak")
#     print(wisielec)



#ZADANIE 8 - GENERATOR PASKA TVP INFO
# import csv
# import random
# zdanie = ''
#
# with open('zadanie8.csv', 'r') as fopen:
#     content = csv.reader(fopen)
#     for row in content:
#         zdanie = zdanie + " " + random.choice(row)
#
# print("\n generator paskow tvp info")
# print(45*"#")
# print(zdanie)
# print(45*"#")

#ZADANIE 9 - ASCII
tekstodszyfrowany = ''
tekstzaszyfrowany = ''
tekstdozaszyfrowania = input("Podaj tekst do zaszyfrowania!")
print("")
for i in tekstdozaszyfrowania:
    tekstzaszyfrowany = str(ord(i)) + "," + tekstzaszyfrowany

print("Haslo zostalo wpisane do pliku tekstowego. Postac zaszyfrowana to:")
print(tekstzaszyfrowany)
print("")

with open('zadanie9.txt', 'w') as f:
    f.write(''.join(tekstzaszyfrowany))



with open('zadanie9.txt', 'r') as fopen:
    danezpliku = fopen.readlines()


zaszyfrowany_array = tekstzaszyfrowany.split(',')
zaszyfrowany_array = list(filter(None, zaszyfrowany_array))
for k in zaszyfrowany_array:
    tekstodszyfrowany = str(chr(int(k))) + tekstodszyfrowany

print("Tekst zaszyfrowany zostal odkodowany z pliku tekstowego. Haslo to:")
print(tekstodszyfrowany)