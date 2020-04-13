def calculate_bmi(weight, height):
    return weight / height ** 2

def get_state(bmi):
    if bmi < 18:
        return "niedowaga"
    elif bmi >= 18 and bmi < 25:
        return "normalna"
    elif bmi >= 25 and bmi < 30:
        return "nadwaga"
    else:
        return "otylosc"


