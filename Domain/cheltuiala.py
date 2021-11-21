

def create_cheltuiala(nr_apartament, suma, tip, data):
    return {'nr_apartament': nr_apartament, 'suma': suma, 'tip': tip, 'data': data}

def get_numar_apartament(cheltuiala):
    return int(cheltuiala['nr_apartament'])

def get_suma(cheltuiala):
    return int(cheltuiala['suma'])

def get_tip(cheltuiala):
    return cheltuiala['tip']

def get_data(cheltuiala):
    return cheltuiala['data']

def set_suma(cheltuiala, suma_noua):
    cheltuiala['suma'] = suma_noua

def set_tip(cheltuiala, tip_nou):
    cheltuiala['tip'] = tip_nou


def to_str(cheltuiala):  # reprezentare string pentru a printa cheltuiala
    string_to_show = 'Apartament ' + str(get_numar_apartament(cheltuiala)) + ': ' + str(
        get_suma(cheltuiala)) + ' lei, pentru ' + get_tip(cheltuiala) + ' , data: ' + get_data(cheltuiala)
    return string_to_show