from Logic.Functionalitati import *
from Domain.cheltuiala import *

def prinMenu():
    print('1. Listeaza cheltuieli')
    print('2. Adauga cheltuiala')
    print('3. Modifica cheltuiala')
    print('4. Sterge cheltuiala')
    print('5. Sterge toate cheltuielile pentru un apartament.')
    print('6. Aduna toate cheltuielile pentru o data calendaristica.')
    print('7. Determina cele mai mari cheltuieli pentru fiecare tip.')
    print('8. Sorteaza cheltuielile')
    print('9. Afiseaza cheltuielile pentru fiecare apartament pentru luna data')
    print('10. Undo')
    print('x. Iesire')


def list_cheltuieli_ui(lista_cheltuieli):
    for cheltuiala in lista_cheltuieli:
        print(to_str(cheltuiala))

def adauga_cheltuiala_ui(lista_cheltuieli):
    numar_apartament = input('Introduceti numarul apartamentului: ')
    suma = input('Introduceti suma: ')
    tip = input('Introduceti tipul cheltuielii: ')
    data = input('Introduceti data in format DD.MM.YYYY: ')
    cheltuiala = create_cheltuiala(numar_apartament, suma, tip, data)
    adauga_cheltuiala(lista_cheltuieli, cheltuiala)

def modifica_cheltuiala_ui(lista_cheltuieli):
    numar_apartament = int(input('Introduceti numarul apartamentului: '))
    data = input('Introduceti data in format DD.MM.YYYY: ')
    suma_noua = int(input('Introduceti noua suma: '))
    tip_nou = input('Introduceti noul tip de cheltuiala: ')
    poz = -1
    for i in range(len(lista_cheltuieli)):
        if get_numar_apartament(lista_cheltuieli[i]) == numar_apartament and get_data(lista_cheltuieli[i]) == data:
            poz = i
    if poz>= 0:
        modifica_cheltuiala(lista_cheltuieli, poz, suma_noua, tip_nou)

def sterge_cheltuiala_ui(lista_cheltuieli):
    numar_apartament = int(input('Introduceti numarul apartamentului: '))
    suma = int(input('Introduceti suma: '))
    tip = input('Introduceti tipul cheltuielii: ')
    data = input('Introduceti data cheltuielii in format DD.MM.YYYY: ')
    poz = -1
    for i in range(len(lista_cheltuieli)):
        if get_numar_apartament(lista_cheltuieli[i]) == numar_apartament and get_data(lista_cheltuieli[i]) == data and get_suma(lista_cheltuieli[i]) == suma and get_tip(lista_cheltuieli[i]) == tip:
            poz = i
    if poz >= 0:
        sterge_cheltuiala(lista_cheltuieli, poz)

def sterge_chelt_ap_ui(lista_cheltuieli):
    numar_apartament = input('Introduceti numarul apartamentului: ')
    sterge_cheltuieli_apartament(lista_cheltuieli, numar_apartament)

def aduna_chelt_ui(lista_cheltuieli):
    data = input('Introduceti data in format DD.MM.YYYY: ')
    val = aduna_toate_cheltuielile(lista_cheltuieli, data)
    print('Valoarea cheltuielilor este ', val, 'lei')

def max_ui(lista_cheltuieli):
    max_intretinere, max_canal, max_alte_cheltuieli = cea_mai_mare_cheltuiala(lista_cheltuieli)
    if max_intretinere != 0:
        print('Cheltuiala maxima la intretinere este de ', max_intretinere, ' lei')
    if max_canal != 0:
        print('Cheltuiala maxima la canal este de ', max_canal, ' lei')
    if max_alte_cheltuieli != 0:
        print('Cheltuiala maxima la alte cheltuieli este de ', max_alte_cheltuieli, ' lei')


def sorteaza_ui(lista_cheltuieli):
    sorteaza_cheltuieli(lista_cheltuieli)
    list_cheltuieli_ui(lista_cheltuieli)

def afiseaza_chelt_lunare_ui(lista_cheltuieli):
    luna = input('Dati luna pentru care doriti cheltuielile: ')
    if luna < 10:
        luna_str = '0' + str(luna)
    else:
        luna_str = str(luna)
    cheltuieli_adunate = dict()
    for cheltuiala in lista_cheltuieli:
        if get_data(cheltuiala).split('.')[1] == luna_str:
            if get_numar_apartament(cheltuiala) not in cheltuieli_adunate:
                cheltuieli_adunate[get_numar_apartament(cheltuiala)] = get_suma(cheltuiala)
            else:
                cheltuieli_adunate[get_numar_apartament(cheltuiala)] += get_suma(cheltuiala)
    for apartament, suma in cheltuieli_adunate.items():
        print('Apartament: ', apartament, ',suma:', suma, 'lei')


def undoCommand(history):
    new_list = history.pop(-1)
    return new_list



def runMenu():
    history = []
    lista_cheltuieli = []
    cheltuiala_1 = create_cheltuiala(12, 45, 'intretinere', '07.11.2021')
    cheltuiala_2 = create_cheltuiala(14, 50, 'canal', '07.11.2021')
    lista_cheltuieli.append(cheltuiala_1)
    lista_cheltuieli.append(cheltuiala_2)

    while True:
        prinMenu()
        raspuns = input('Dati optiunea: ')
        if raspuns == '1':
            list_cheltuieli_ui(lista_cheltuieli)
        elif raspuns == '2':
            history.append([])
            for cheltuiala in lista_cheltuieli:
                history[-1].append(cheltuiala.copy())

            adauga_cheltuiala_ui(lista_cheltuieli)

        elif raspuns == '3':
            history.append([])
            for cheltuiala in lista_cheltuieli:
                history[-1].append(cheltuiala.copy())

            modifica_cheltuiala_ui(lista_cheltuieli)


        elif raspuns == '4':
            history.append([])
            for cheltuiala in lista_cheltuieli:
                history[-1].append(cheltuiala.copy())

            sterge_cheltuiala_ui(lista_cheltuieli)


        elif raspuns == '5':
            history.append([])
            for cheltuiala in lista_cheltuieli:
                history[-1].append(cheltuiala.copy())

            sterge_chelt_ap_ui(lista_cheltuieli)


        elif raspuns == '6':
            aduna_chelt_ui(lista_cheltuieli)

        elif raspuns == '7':
            max_ui(lista_cheltuieli)
        elif raspuns == '8':
            sorteaza_ui(lista_cheltuieli)
        elif raspuns == '9':
            afiseaza_chelt_lunare_ui(lista_cheltuieli)


        elif raspuns == '10':
            if len(history) == 0:
                print('Nu mai sunt operatii Undo de efectuat.')
            else:
                new_list = undoCommand(history)
                lista_cheltuieli = new_list.copy()

        elif raspuns == 'x':
            break
