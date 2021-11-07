import datetime


class Cheltuiala:
    numar_apartament: int
    suma: int
    data: str
    tip: str  # poate avea valori din {intretinere, canal, alte cheltuieli}

    def __init__(self, nr_apartament: int, suma: int, tip: str, data: str): #constructor
        self.numar_apartament = nr_apartament
        self.suma = suma
        self.tip = tip
        self.data = data

    def __str__(self): #reprezentare string pentru a printa obiectul
        string_to_show = 'Apartament ' + str(self.numar_apartament) + ': ' + str(self.suma) + ' lei, pentru ' + self.tip + ' ' + self.data
        return string_to_show

    def __repr__(self): #reprezentare string pentru a printa obiectul
        string_to_show = 'Apartament ' + str(self.numar_apartament) + ': ' + str(
            self.suma) + ' lei, pentru ' + self.tip + ' ' + self.data
        return string_to_show

    def get_numar_apartament(self):
        return self.numar_apartament

    def get_suma(self):
        return self.suma

    def get_tip(self):
        return self.tip

    def get_data(self):
        return self.data


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
