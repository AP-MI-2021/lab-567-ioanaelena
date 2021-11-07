from Logic import Logic

if __name__ == '__main__':
    log = Logic()
    while True:
        raspuns = input('1. Listeaza cheltuieli \n2. Adauga cheltuiala\n3. Modifica cheltuiala\n4. Sterge cheltuiala\n'
                        '5. Sterge toate cheltuielile pentru un apartament.\n6. Aduna toate cheltuielile pentru o data calendaristica.\n'
                        '7. Determina cele mai mari cheltuieli pentru fiecare tip.\n8. Sorteaza cheltuielile\n'
                        '9. Afiseaza cheltuielile pentru fiecare apartament pentru luna data\n10. Iesire\n')
        if raspuns == '10':
            break
        if raspuns == '1':
            print(log.asociatie_proprietari.cheltuieli)
        if raspuns == '2':
            numar_apartament = input('Introduceti numarul apartamentului: ')
            suma = input('Introduceti suma: ')
            tip = input('Introduceti tipul cheltuielii: ')
            data = input('Introduceti data in format DD.MM.YYYY: ')
            log.asociatie_proprietari.adauga_cheltuiala(int(numar_apartament), int(suma), tip, data)
        if raspuns == '3':
            numar_apartament = input('Introduceti numarul apartamentului: ')
            data = input('Introduceti data in format DD.MM.YYYY: ')
            suma_noua = input('Introduceti noua suma: ')
            tip_nou = input('Introduceti noul tip de cheltuiala: ')
            log.asociatie_proprietari.modifica_cheltuiala(int(numar_apartament), data, int(suma_noua), tip_nou)
        if raspuns == '4':
            numar_apartament = input('Introduceti numarul apartamentului: ')
            suma = input('Introduceti suma: ')
            tip = input('Introduceti tipul cheltuielii: ')
            data = input('Introduceti data cheltuielii in format DD.MM.YYYY: ')
            log.asociatie_proprietari.sterge_cheltuiala(int(numar_apartament), int(suma), tip, data)
        if raspuns == '5':
            numar_apartament = input('Introduceti numarul apartamentului: ')
            log.sterge_cheltuieli_apartament(int(numar_apartament))
        if raspuns == '6':
            data = input('Introduceti data in format DD.MM.YYYY: ')
            log.aduna_toate_cheltuielile(data)
        if raspuns == '7':
            log.cea_mai_mare_cheltuiala()
        if raspuns == '8':
            log.sorteaza_cheltuieli()
        if raspuns == '9':
            luna = input('Dati luna pentru care doriti cheltuielile: ')
            log.afiseaza_cheltuieli_lunare(int(luna))
