from Logic.Functionalitati import Logic

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
    print('x. Iesire')


def runMenu():
    log = Logic()
    while True:
        prinMenu()
        raspuns = input('Dati optiunea: ')
        if raspuns == '1':
            print(log.asociatie_proprietari.cheltuieli)
        elif raspuns == '2':
            numar_apartament = input('Introduceti numarul apartamentului: ')
            suma = input('Introduceti suma: ')
            tip = input('Introduceti tipul cheltuielii: ')
            data = input('Introduceti data in format DD.MM.YYYY: ')
            log.asociatie_proprietari.adauga_cheltuiala(int(numar_apartament), int(suma), tip, data)
        elif raspuns == '3':
            numar_apartament = input('Introduceti numarul apartamentului: ')
            data = input('Introduceti data in format DD.MM.YYYY: ')
            suma_noua = input('Introduceti noua suma: ')
            tip_nou = input('Introduceti noul tip de cheltuiala: ')
            log.asociatie_proprietari.modifica_cheltuiala(int(numar_apartament), data, int(suma_noua), tip_nou)
        elif raspuns == '4':
            numar_apartament = input('Introduceti numarul apartamentului: ')
            suma = input('Introduceti suma: ')
            tip = input('Introduceti tipul cheltuielii: ')
            data = input('Introduceti data cheltuielii in format DD.MM.YYYY: ')
            log.asociatie_proprietari.sterge_cheltuiala(int(numar_apartament), int(suma), tip, data)
        elif raspuns == '5':
            numar_apartament = input('Introduceti numarul apartamentului: ')
            log.sterge_cheltuieli_apartament(int(numar_apartament))
        elif raspuns == '6':
            data = input('Introduceti data in format DD.MM.YYYY: ')
            log.aduna_toate_cheltuielile(data)
        elif raspuns == '7':
            log.cea_mai_mare_cheltuiala()
        elif raspuns == '8':
            log.sorteaza_cheltuieli()
        elif raspuns == '9':
            luna = input('Dati luna pentru care doriti cheltuielile: ')
            log.afiseaza_cheltuieli_lunare(int(luna))
        elif raspuns == 'x':
            break
