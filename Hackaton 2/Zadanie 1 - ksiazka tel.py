# ZADANIE KSIAZKA ADRESOWA
import json
lista_numerow = []


def nowywpis():
    koniec = False
    odpowiedz = "t"
    while odpowiedz == "t":
        newname = input("Podaj imie: ")
        newtel = input("Podaj nr telefonu: ")
        if (newtel.isnumeric() == True) and (len(newtel) == 9):
            lista = {"imie" : newname,
                     "numer" : newtel}
            filename = 'ksiazka_numerow.json'

            with open(filename, 'r+') as f:
                data = json.load(f)
                data.append(lista)
                f.seek(0)
                json.dump(data, f)

            odpowiedz = input("Wczytac kolejny wpis? t/n: ")
            while odpowiedz != 't' and odpowiedz != 'n':
                odpowiedz = input("Wczytac kolejny wpis? t/n: ")
        else:
            print("W polu nr telefonu mogą byc tylko znaki o dlugosci 9 cyfr!  \n ===================")

def wczytaj_liste_wpisow():
    filename = 'ksiazka_numerow.json'
    with open(filename, 'r') as f:
        data = json.load(f)
        iloscwpisow = len(data)
        return data

if __name__ == '__main__':
    print(wczytaj_liste_wpisow())
    nowywpis()
    print(wczytaj_liste_wpisow())

