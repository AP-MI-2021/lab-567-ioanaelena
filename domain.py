def cheltuiala():
    return{
        'numar apartament' : int,
        'suma' : int,
        'data' : [0] * 3,
        'tip' : str
    }


def get_cheltuiala_index(cheltuieli, numar_apartament):
    for i in range(len(cheltuieli)):
        if cheltuieli[i]['numar apartament'] == numar_apartament:
            return i


def get_suma_cheltuiala(cheltuieli, index_cheltuiala):
    return cheltuieli[index_cheltuiala]['suma']

def get_data_cheltuiala(cheltuieli, index_cheltuiala):
    return cheltuieli[index_cheltuiala]['data']

def get_tip_cheltuiala(cheltuieli, index_cheltuiala):
    return cheltuieli[index_cheltuiala]['tip']