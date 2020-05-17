#ZADANIE 1
class dog:
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed

    def sound(self):
        print('Hau Hau')

obj_dog = dog('dyzio', 'grey', 'jamnik')
print(obj_dog.name)
obj_dog.sound()

#ZADANIE 3
class Queue:
    def __init__(self, queue_list):
        self.queue_list = queue_list

        #metoda czy jest pusta
    def is_empty(self):
        if len(self.queue_list) == 0:
            return print("jest")
        else:
            return print("nie")

        #metoda dodaj (put)
    def put(self, elem):
        self.queue_list.append(elem)
        print(f"{elem} is added to queue")

        #meoda zdejmij (get)
    def get(self):
        return self.queue_list.pop(0)

    def show(self):
        print(self.queue_list)

lista_elementow = ['1', '2', 'trzy', 4.0]
kolejka = Queue(lista_elementow)
kolejka.show()
kolejka.is_empty()

#ZADANIE 5
# class sklep:
#     def __init__(self, zegarek, koszula, buty):
#         self.zegarek = zegarek
#         self.koszula = koszula
#         self.buty = buty
#
#     def przymierz(self, co):
#         print('Przymierzam ' + str(co))
#
#     def zobacz(self, co):
#         print('Ogladam ' + str(co))
#
#     def kup(self, co):
#         print('Kupione ' + str(co))
#
#     def zwroc(self, co):
#         print('Zwrocone ' + str(co))
#
# obj_sklep = sklep('zegarek_bransoleta', 'koszula_w_paski', 'buty_wizytowe')
# print(obj_sklep.zegarek)
# co = input("Co chcesz przymierzyc? zegarek, koszula czy buty?")
# obj_sklep.przymierz(co)
#
# co = input("Co chcesz obejrzec? zegarek, koszula czy buty?")
# obj_sklep.zobacz(co)
#
# co = input("Co chcesz kupic? zegarek, koszula czy buty?")
# obj_sklep.kup(co)
#
# co = input("Co chcesz zwrocic? zegarek, koszula czy buty?")
# obj_sklep.zwroc(co)

#ZADANIE 6 do domu
class Employee:
  def __init__(self, name, lastname, position, salary, exp, student):
    self.name = name
    self.lastname = lastname
    self.position = position
    self.salary = salary
    self.exp = exp
    self.student = student

  def show(self):
    print(f"{self.name} {self.lastname} | {self.position }")
    print(f"{self.salary} PLN - exp: {self.exp} years")
    podatek = self.salary * 0.19
    if self.student == True:
        skladka = 0
    else:
        skladka = self.salary * 0.05
    print(f"Skladka zdrowotna : {skladka}, podatek: {podatek}")
    spolg = "bcdfghjklmnpqrstvwxyz"
    email = ''
    czlon = self.name.lower() + self.lastname.lower()
    for i in czlon:
        if i in spolg:
            email += i
    print(f"Email: {email}@pythonlovers.com")

  def salary_bump(self):
    self.salary = self.salary * 1.11
    print('New salary: ', self.salary)

p1 = Employee('Jan', 'Kowalski', 'QA', 4500, 1.5, False)
p1.show()
print("------ bump ------")
p1.salary_bump()
p1.show()

