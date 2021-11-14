from Logic.CRUD import AsociatieProprietari


class Logic:
    def __init__(self):
        self.asociatie_proprietari = AsociatieProprietari()

    def sterge_cheltuieli_apartament(self, nr_apartament: int):
        for cheltuiala in self.asociatie_proprietari.cheltuieli:
            if cheltuiala.numar_apartament == nr_apartament:
                self.asociatie_proprietari.cheltuieli.remove(cheltuiala)

    def aduna_toate_cheltuielile(self, data: str):
        valoare = 0
        for cheltuiala in self.asociatie_proprietari.cheltuieli:
            if cheltuiala.data == data:
                valoare += cheltuiala.suma
        print('Valoarea cheltuielilor este ', valoare, 'lei')

    def cea_mai_mare_cheltuiala(self):
        max_intretinere = 0
        max_canal = 0
        max_alte_cheltuieli = 0
        for cheltuiala in self.asociatie_proprietari.cheltuieli:
            if cheltuiala.tip == 'intretinere' and cheltuiala.suma > max_intretinere:
                max_intretinere = cheltuiala.suma
            elif cheltuiala.tip == 'canal' and cheltuiala.suma > max_canal:
                max_canal = cheltuiala.suma
            elif cheltuiala.tip == 'alte cheltuieli' and cheltuiala.suma > max_alte_cheltuieli:
                max_alte_cheltuieli = cheltuiala.suma
        if max_intretinere != 0:
            print('Cheltuiala maxima la intretinere este de ', max_intretinere, ' lei')
        if max_canal != 0:
            print('Cheltuiala maxima la canal este de ', max_canal, ' lei')
        if max_alte_cheltuieli != 0:
            print('Cheltuiala maxima la alte cheltuieli este de ', max_alte_cheltuieli, ' lei')

    def sorteaza_cheltuieli(self):
        for index_i in range(0, len(self.asociatie_proprietari.cheltuieli) - 1):
            for index_j in range(index_i + 1, len(self.asociatie_proprietari.cheltuieli)):
                if self.asociatie_proprietari.cheltuieli[index_i].suma < self.asociatie_proprietari.cheltuieli[index_j].suma:
                    aux = self.asociatie_proprietari.cheltuieli[index_i]
                    self.asociatie_proprietari.cheltuieli[index_i] = self.asociatie_proprietari.cheltuieli[index_j]
                    self.asociatie_proprietari.cheltuieli[index_j] = aux

    def afiseaza_cheltuieli_lunare(self, luna: int):
        if luna < 10:
            luna_str = '0' + str(luna)
        else:
            luna_str = str(luna)
        cheltuieli_adunate = dict()
        for cheltuiala in self.asociatie_proprietari.cheltuieli:
            if cheltuiala.data.split('.')[1] == luna_str:
                if cheltuiala.numar_apartament not in cheltuieli_adunate:
                    cheltuieli_adunate[cheltuiala.numar_apartament] = cheltuiala.suma
                else:
                    cheltuieli_adunate[cheltuiala.numar_apartament] += cheltuiala.suma
        for apartament, suma in cheltuieli_adunate.items():
            print('Apartament: ', apartament, ',suma:', suma, 'lei')

# log = Logic()
# log.asociatie_proprietari.adauga_cheltuiala(15, 123, 'alte cheltuieli')
# log.asociatie_proprietari.adauga_cheltuiala(15, 116, 'intretinere')
# log.asociatie_proprietari.sterge_cheltuiala(12, 45, 'intretinere', '07.11.2021')
# log.asociatie_proprietari.adauga_cheltuiala(14, 132, 'canal')
# # log.asociatie_proprietari.sterge_cheltuieli_apartament(14)
# # print(log.asociatie_proprietari.cheltuieli)
# # log.asociatie_proprietari.cea_mai_mare_cheltuiala()
# log.sorteaza_cheltuieli()
# print(log.asociatie_proprietari.cheltuieli)
# log.afiseaza_cheltuieli_lunare(11)
