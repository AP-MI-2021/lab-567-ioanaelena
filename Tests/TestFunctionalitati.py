from Domain.cheltuiala import Cheltuiala


def test_get_suma():
    cheltuiala = Cheltuiala(12, 50, 'canal', '07.11.2021')
    assert cheltuiala.get_suma() == 50

def test_get_numar_apartament():
    cheltuiala = Cheltuiala(12, 50, 'canal', '07.11.2021')
    assert cheltuiala.get_numar_apartament() == 12

def test_get_tip():
    cheltuiala = Cheltuiala(12, 50, 'canal', '07.11.2021')
    assert cheltuiala.get_tip() == 'canal'

# def test_get_data():
    # cheltuiala.get_data()



def testAll():
    test_get_suma()
    test_get_numar_apartament()
    test_get_tip()
