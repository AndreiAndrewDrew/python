print("Varianta 1")

info = {
    'name': 'Bogdan',
    'is_instructor': True
}

info_copy = info.copy()  # Folosim metoda 'copy()'
info_copy['keie_noua'] = 5
print("Dict 'info':", info)
print("Dict 'info_copy':", info_copy)  # Modifcarile sau produs numai in inf0_copy
print("Id dict 'info':", id(info))
print("Id dict 'info_copy':", id(info_copy))  # Respectiv au id diferite

print("Varianta 2")

info2 = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': []
}

info_copy2 = info2.copy()
info_copy2['reviews'].append('Great course!')

print(info2)  # se modifica si originalul de oarece contine cimp
print(info_copy2)  # cu keie de tip obiect care se modifica

print(id(info2))
print(id(info_copy2))  # dar id-rile sunt diferite!!!

print("Varianta 3")
from copy import deepcopy

info3 = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': []
}

info_copy3 = deepcopy(info3)  # varianta 3 pentru a crea copie unicale
info_copy3['reviews'].append('Great course!')

print(info3)
print(info_copy3)

print(id(info3))
print(id(info_copy3))
