class Ssaki:
    pija_mleko = True
    kregoslup = True
    zmienno_cieplne = False

    def __init__(self):
        print('ssak ma cycki')

    def pij_mleko(self):
        print('mmmm')

    def jest_zimno(self, temp):
        print('jest mi zimno', temp)


class Czlowiek(Ssaki):
    def __init__(self, imie, wiek, aktywny):
        self.imie = imie
        self.wiek = wiek
        self.aktywny = aktywny

    def pij_mleko(self):
        # super().pija_mleko()
        super().jest_zimno(self.wiek)
        print('pije mleko jako dziecko')

c = Czlowiek('Adam', 30, True)
print(c.imie)

s = Ssaki()
# s.pij_mleko()
s.jest_zimno(-5)
c.pij_mleko()