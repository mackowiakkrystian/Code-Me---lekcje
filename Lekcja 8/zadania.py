import sys
lista = ['5', 'jeden', '3', '4', '4.5', 4, 0, ['xxx', 'yyy'], {1, 2, 3}, {'a': 1, 'b': 2}]

for i in lista:
    try:
        dzielenie =  10/int(i)
    except ZeroDivisionError:
        print("Dzielenie przez 0")
    except TypeError:
        print("Błąd typu")
    except ValueError:
        print("Błąd wartosci")
    else:
        print(dzielenie)

print("\n\n")

# ZADANIE 5
import bmi


def fix_units(user_input, unit):
    if unit in user_input:
        container = ''
        for char in user_input:
            if char.isnumeric() or char == '.':
                container += char
        return float(container)
    else:
        return -1


while True:
    weight = input("Podaj wage [kg]:")

    try:
        float(weight)
    except ValueError:
        print('value error')
        w = fix_units(weight, 'kg')

        if w == -1:
            print('Wartosc nieprawidlowa')
        else:
           break
    else:
        w = float(weight)
        break


print(w)


height = input("Podaj wzrost [m]:")

try:
    float(height)
except ValueError as e:
    print(e)
    h = fix_units(height, 'm')

    if h == -1:
        print('Wartosc nieprawidlowa')
else:
    h = float(height)

print(h)


result_bmi = bmi.calculate_bmi(w, h)
state = bmi.get_state(result_bmi)
print(state)

filename = state.lower() + '.txt'
with open(filename) as fopen:
    tip = fopen.read()

print(tip)



#ZADANIE 3
import sys
my_list = [3, '345', {'a': 1}, 0, ['d', 'a']]

try:
    index = float(input('Podaj index:'))
    wynik = my_list[1/index]
except (TypeError, ValueError) as message:
    print('Exception message: ', message)
else:
    print(wynik)

#ZADANIE 9
import webbrowser

def check_sufix(url):
    allowed_suffixes = ('pl', 'com', 'fr')

    valid_url = False
    for sufix in allowed_suffixes:
        if url.endswith(sufix):
            print('Prawidlowa koncówka')
            valid_url = True
            break

    if not valid_url:
        raise TypeError('Twój url nie jest obsługiwany')

def with_prefix(url):
    if url.startswith('https://') or url.startswith('http://'):
        return url
    else:
        return 'http://' + url

user_url = input('Podaj strone www')
user_url = user_url.strip()
user_url = user_url.replace(' ', '')

try:
    check_sufix(user_url)
except TypeError as e:
    print('Wpadł błąd')
    print(e)
else:
    webbrowser.open(with_prefix(user_url))


