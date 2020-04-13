import BMI

print(BMI.get_state(26))

w = float(input("Podaj wage"))
h = float(input("Podaj wzrost"))

obliczone = BMI.calculate_bmi(w,h)
state = BMI.get_state(obliczone)
filename = state.lower() + '.txt'
with open(filename, 'r') as fopen:
    tip = fopen.read()

print(tip)

