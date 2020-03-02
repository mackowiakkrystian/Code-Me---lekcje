# zadanie 1
iloscminut = 7 * 24 * 60
print("1. Liczba minut w ciagu 7 dni to: " + str(iloscminut) + '\n')

# zadanie 2
iledni = 75 // 2
iletygodni = iledni // 7
print("2. ile tygodni mi zajmie nauka przy poswieceniu 2h dziennie: " +str(iletygodni) + '\n')


# zadanie 3 - BMI kalkulator
wzrost = 1.74
waga = 62

BMI = waga / (wzrost**2)
print("3. Moje BMI to " + str(round(BMI, 2)) +'\n')

# zadanie 4 - zmienna input
wzrost2 = input("Podaj Twoj wzrost!" + '\n')
waga2 = input("Podaj Twoja wage!" + '\n')

BMI2 = float(waga2) / (float(wzrost2)**2)
print("4. Twoje BMI przy wzroscie " + str(wzrost2) + " oraz wadze: " + str(waga2) + " wynosi: " + str(round(BMI2, 2)))