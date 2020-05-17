from abc import ABC, abstractclassmethod
class zwierzeta(ABC):
    @abstractclassmethod
    def set_name(self):
        pass

class ssaki(zwierzeta):
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

class kot(ssaki):
    pass
class czlowiek(ssaki):
    def __init__(self, name):
        super().__init__(name)

class pies(ssaki):
    pass

m = ssaki('Wiesio')
m.show_name()
h = czlowiek('Krystian')