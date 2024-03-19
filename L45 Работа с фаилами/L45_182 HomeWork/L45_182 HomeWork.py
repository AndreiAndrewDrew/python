from pathlib import Path

print("Afisham calea directoriri unde ne aflam:")
print(Path('.').cwd())  # Afisham calea unde ne aflam

# Sarcinia 1. Creatsi mapa 'files'
dir_files = Path('files')

if not dir_files.exists():  # daca nu exista o creem
    dir_files.mkdir()  # creem mapa

print("Calea mapei 'files':", dir_files)

# Sarina 2. Creatsi 2 fisiere first.txt si second.txt

with open('files/first.txt', 'w') as test_file:  # metoda 'with'
    test_file.write("1.First String to first.txt\n")
    test_file.write("2.Second String to first.txt\n")
    test_file.write("3.Third String to first.txt\n")

with open('files/second.txt', 'w') as test_file:
    test_file.write("1.First String to second.txt\n")
    test_file.write("2.Second String to second.txt\n")

# Sarcina 3. Cititsi toate rindurile din fisiere

with open('files/first.txt') as test_file:
    print("Afisham toate rindurile din fisierul 'first.txt':")
    print(test_file.read())

with open('files/second.txt') as test_file:
    print("Afisham toate rindurile din fisierul 'second.txt':")
    print(test_file.read())

# Sarcina 4. Cititsi rindurile din 'second.txt' rind dupa rind

with open('files/second.txt') as test_file:
    print("Afisham rindurile din 'second.txt' rind dupa rind:")
    while True:  # citirea fisierului cu ajutorul 'while' + 'readline'
        l = test_file.readline()
        if not l:
            break
        print(l)

# # Sarcina 5: Stergetsi abmele fisiere
# print("Stergem abmele fisiere:")
# print(Path('./files/first.txt'))
# print(Path('./files/second.txt'))
#
# if Path('./files/first.txt').exists() and Path('./files/second.txt'):
#     Path('./files/first.txt').unlink()
#     Path('./files/second.txt').unlink()
#
# # Sarcina 6: Stergem mapa 'files'
# print("Stergem mapa 'files':")
#
# print(dir_files)
#
# if dir_files.exists():  # daca exista
#     dir_files.rmdir()  # stergem mapa
