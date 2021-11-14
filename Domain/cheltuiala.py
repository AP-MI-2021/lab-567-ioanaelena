
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

