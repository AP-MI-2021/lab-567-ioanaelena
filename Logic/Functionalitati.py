from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
from Domain.cheltuiala import *


def sterge_cheltuieli_apartament(lista_cheltuieli, nr_apartament):
    i=0
    while i < len(lista_cheltuieli):
        if get_numar_apartament(lista_cheltuieli[i]) == int(nr_apartament):
            sterge_cheltuiala(lista_cheltuieli, i)
        else:
            i = i+1

def aduna_toate_cheltuielile(lista_cheltuieli, data):
    valoare = 0
    for cheltuiala in lista_cheltuieli:
        if get_data(cheltuiala) == data:
            valoare += get_suma(cheltuiala)

    return valoare
    #print('Valoarea cheltuielilor este ', valoare, 'lei')

def cea_mai_mare_cheltuiala(lista_cheltuieli):
    max_intretinere = 0
    max_canal = 0
    max_alte_cheltuieli = 0
    for cheltuiala in lista_cheltuieli:
        if get_tip(cheltuiala) == 'intretinere' and get_suma(cheltuiala) > max_intretinere:
            max_intretinere = get_suma(cheltuiala)
        elif get_tip(cheltuiala) == 'canal' and get_suma(cheltuiala) > max_canal:
            max_canal = get_suma(cheltuiala)
        elif get_tip(cheltuiala) == 'alte cheltuieli' and get_suma(cheltuiala) > max_alte_cheltuieli:
            max_alte_cheltuieli = get_suma(cheltuiala)

    return max_intretinere, max_canal, max_alte_cheltuieli


def sorteaza_cheltuieli(lista_cheltuieli):
    for index_i in range(0, len(lista_cheltuieli) - 1):
        for index_j in range(index_i + 1, len(lista_cheltuieli)):
            if get_suma(lista_cheltuieli[index_i]) < get_suma(lista_cheltuieli[index_j]):
                aux = lista_cheltuieli[index_i]
                lista_cheltuieli[index_i] = lista_cheltuieli[index_j]
                lista_cheltuieli[index_j] = aux

