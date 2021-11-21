import datetime
from Domain.cheltuiala import get_numar_apartament, get_suma, get_tip, get_data, set_suma, set_tip


def adauga_cheltuiala(lista_cheltuieli, cheltuiala):
    lista_cheltuieli.append(cheltuiala)

def sterge_cheltuiala(lista_cheltuieli, pozitie):
    lista_cheltuieli.pop(pozitie)

def modifica_cheltuiala(lista_cheltuieli, pozitie, suma_noua, tip_nou):
    set_suma(lista_cheltuieli[pozitie], suma_noua)
    set_tip(lista_cheltuieli[pozitie], tip_nou)