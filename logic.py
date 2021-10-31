import domain

def citeste_cheltuiala():
    cheltuiala = domain.cheltuiala()
    cheltuiala['numar apartament'] = int(input("Numarul apartamentului: "))
    cheltuiala['suma'] = int(input("Suma: "))
    cheltuiala['data'][0] = int(input("Ziua: "))
    cheltuiala['data'][1] = int(input("Luna: "))
    cheltuiala['data'][2] = int(input("Anul: "))
    cheltuiala['tip'] = input("Tipul cheltuielii: ")


def adauga_cheltuiala(cheltuieli, cheltuiala_citita):
    cheltuieli.append(cheltuiala_citita)
    return cheltuieli


def sterge_cheltuiala(cheltuieli, index_cheltuiala):
    l = []
    for i in range(len(cheltuieli)):
        if i != index_cheltuiala:
            l.append(cheltuieli[i])
    return l

def modifica_cheltuiala(cheltuieli, numar_apartament_dat):
    l = []
    for i in range(len(cheltuieli)):
        if cheltuieli[i]['numar apartament'] == numar_apartament_dat:
            l.append((citeste_cheltuiala()))
        else:
            l.append(cheltuieli[i])
    return l




def sterge_cheltuieli_pt_apartament_dat(cheltuieli, numar_apartament_dat):
    l = []
    for i in range(len(cheltuieli)):
        if cheltuieli[i]['numar apartament'] != numar_apartament_dat:
            l.append((cheltuieli[i]))
    return l


def aduna_valoare_dupa_data(cheltuilei, valoare, zi, luna, an):
    for i in range(len(cheltuilei)):
        if cheltuilei[i]['data'][0] == zi and cheltuilei[i]['data'][1] ==  luna and cheltuilei[i]['data'][2] == an:
            cheltuilei[i]['suma'] = cheltuilei[i]['suma'] + valoare
    return cheltuilei

