from Domain.cheltuiala import *


def test_get_suma():
    cheltuiala = create_cheltuiala(12, 50, 'canal', '07.11.2021')
    assert get_suma(cheltuiala) == 50

def test_get_numar_apartament():
    cheltuiala = create_cheltuiala(12, 50, 'canal', '07.11.2021')
    assert get_numar_apartament(cheltuiala) == 12

def test_get_tip():
    cheltuiala = create_cheltuiala(12, 50, 'canal', '07.11.2021')
    assert get_tip(cheltuiala) == 'canal'

# def test_get_data():
    # cheltuiala.get_data()






def testAll():
    test_get_suma()
    test_get_numar_apartament()
    test_get_tip()
    test_undo()