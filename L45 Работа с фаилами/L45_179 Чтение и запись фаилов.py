print("Citirea din fisier:")
with open('test.txt') as test_file:
    print(test_file.read())  # citim tot din 'test.txt'

with open('test.txt') as test_file:
    print(test_file.readlines(), '\n')  # citim toate rindurile si le introducem intro lista

print("Inscrierea in fisier:")
with open('new.txt', 'w') as new_file:  # 'w' - regim de reinscriere, pierdem inscriptile vechi in fisier
    new_file.write("1 First line writeded with coding!\n")

with open('new.txt') as new_file:  # Citim fisierul 'new.txt'
    print(new_file.read())

with open('new.txt', 'a') as new_file:  # 'a'- regim de adugarea a inscriptsiei, nu pierdem cele vechi
    new_file.write("2 Second line writeded with coding!\n")

with open('new.txt') as new_file:  # Citim fisierul 'new.txt'
    print(new_file.read())

print("Shtergerea fisierilor:")

from pathlib import Path

print(Path('new.txt').exists())  # Controlom daca exista asa fisier
Path('new.txt').unlink()  # stergem asa fisier
print(Path('new.txt').exists())  # din nou controlm daca exista asa fisier dupa stergere
