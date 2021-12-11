from Logic.CRUD import adauga_cheltuiala


def test_undo_redo():
    # 1. lista initiala goala
    lista = []
    undo_list = []
    redo_list = []
    undo_list.append(lista)
    redo_list.clear()
    # 2. adaugam o cheltuiala
    lista = adauga_cheltuiala(12, 50, 'canal', '07.11.2021')
    undo_list.append(lista)
    redo_list.clear()
    assert get_id(lista[0]) == '1'
    assert len(lista) == 1
    # 3. adaugam inco o cheltuiala
    lista = adauga_cheltuiala(13, 51, 'canal', '07.11.2021')
    undo_list.append(lista)
    redo_list.clear()
    assert get_id(lista[0]) == '1'
    assert get_id(lista[1]) == '2'
    assert len(lista) == 2
    # 4. adaugam inca o cheltuiala
    lista = adauga_cheltuiala(16, 80, 'canal', '07.11.2021')
    assert get_id(lista[0]) == '1'
    assert get_id(lista[1]) == '2'
    assert get_id(lista[2]) == '3'
    assert len(lista) == 3
    # 5. undo scoate ultima cheltuiala adaugata
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert get_id(lista[0]) == '1'
    assert get_id(lista[1]) == '2'
    assert len(lista) == 2
    # 6. inca un undo scoate penultimul obiect adaugat
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == '1'
    assert len(lista) == 1
    # 7. inca un undo scoate si primul element bagat
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert len(lista) == 0
    undo_list.append(lista)
    redo_list.clear()
    # 8. inca un undo nu face nimic
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert len(lista) == 0
    # 9. adaugam trei obiecte
    lista = adauga_cheltuiala(18, 120, 'canal', '07.11.2021')
    undo_list.append(lista)
    redo_list.clear()

    lista = adauga_cheltuiala(15, 150, 'canal', '07.11.2021')
    undo_list.append(lista)
    redo_list.clear()

    lista = adauga_cheltuiala(10, 57, 'canal', '07.11.2021')
    # 10. redo nu face nimic
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == '1'
    assert get_id(lista[1]) == '2'
    assert get_id(lista[2]) == '3'
    assert len(lista) == 3
    # 11. undo undo scot ultimele doua obiecte
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == '1'
    assert get_id(lista[1]) == '2'
    assert len(lista) == 2

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == '1'
    assert len(lista) == 1
    # 12. redo redo anuleaza cele doua undo-uri
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == '1'
    assert get_id(lista[1]) == '2'
    assert len(lista) == 2

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == '1'
    assert get_id(lista[1]) == '2'
    assert get_id(lista[2]) == '3'
    assert len(lista) == 3
    # 13. doua undo-uri scot ultimele doua obiecte
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == '1'
    assert get_id(lista[1]) == '2'
    assert len(lista) == 2

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == '1'
    assert len(lista) == 1

    undo_list.append(lista)
    redo_list.clear()
    # 14. adaugam un obiect
    lista = adaugaRezervare('4', 'd', 'economy plus', 20, 'nu', lista)
    # 15. redo nu face nimic
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == '1'
    assert get_id(lista[1]) == '4'
    assert len(lista) == 2
    # 16. undo anuleaza adaugarea obiectului 4
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == '1'
    assert len(lista) == 1
    # 17. undo, lasa lista goala
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert len(lista) == 1
    # 18 redo,redo se anuleaza ultimele doua undo-uri
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert get_id(lista[0]) == '1'
    assert len(lista) == 2

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == '1'
    assert get_id(lista[1]) == '4'
    assert len(lista) == 2
    # 19. redo nu face nimic
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == '1'
    assert get_id(lista[1]) == '4'
    assert len(lista) == 2