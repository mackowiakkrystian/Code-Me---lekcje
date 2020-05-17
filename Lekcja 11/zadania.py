import random
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def meow(self):
        print('meow')

    def __str__(self):
        return f"kot : {self.name} ma lat {self.age}"

def generate_cats():
    names = ['mruczek', 'wieslaw', 'filemon', 'w butach', 'reksio']
    for name in names:
        tmp = random.randint(2, 10)
        cat = Cat(name, tmp)
        print(cat)

kotek1 = Cat('Stefan', '5')

kotek1.meow()

generate_cats()
