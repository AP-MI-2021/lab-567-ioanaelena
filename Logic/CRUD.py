import datetime

from Domain.cheltuiala import Cheltuiala


class AsociatieProprietari:
    def __init__(self):
        self.cheltuieli = list()
        cheltuiala_1 = Cheltuiala(12, 45, 'intretinere', '07.11.2021')
        cheltuiala_2 = Cheltuiala(14, 50, 'canal', '07.11.2021')
        self.cheltuieli.append(cheltuiala_1)
        self.cheltuieli.append(cheltuiala_2)

    def adauga_cheltuiala(self, numar_apartament: int, suma: int, tip: str, data: str):
        cheltuiala_noua = Cheltuiala(numar_apartament, suma, tip, data)
        self.cheltuieli.append(cheltuiala_noua)

    def sterge_cheltuiala(self, numar_apartament: int, suma: int, tip: str, data: str):
        for element in self.cheltuieli:
            if element.get_numar_apartament() == numar_apartament and element.get_suma() == suma and element.get_tip() == tip and element.get_data() == data:
                self.cheltuieli.remove(element)

    def modifica_cheltuiala(self, nr_apartament: int, data: str, suma_noua: int, tip_nou: str):
        for cheltuiala in self.cheltuieli:
            if cheltuiala.get_numar_apartament() == nr_apartament and cheltuiala.get_data() == data:
                cheltuiala.suma = suma_noua
                cheltuiala.tip = tip_nou
                cheltuiala.data = datetime.datetime.now().strftime('%d.%m.%Y')

    def get_cheltuieli(self):
        return self.cheltuieli
