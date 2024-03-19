from copy import deepcopy

info_practica = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': []
}

info_copy_practica = deepcopy(info_practica)  # varianta 3 pentru a crea copie unicale
info_copy_practica['reviews'].append('Great course!')
info_copy_practica['reviews'].append('Super!')
info_practica['reviews'].append('Super2!')

print(info_practica)
print(info_copy_practica)

print(id(info_practica))
print(id(info_copy_practica))
