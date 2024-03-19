# ----Mtoda 1---
# test_file = open('test.txt', 'w')  # creeem fisierul 'test.txt' pentru inscriere
#
# print(test_file)
# print(type(test_file))
#
# test_file.write("1.First String\n")
# test_file.write("2.Second String\n")
#
# test_file.close()  # inchidem fisierul
# =====Sfirshit Metoda 1------

# ----Metoda 2 cu 'with'-----
with open('test.txt', 'w') as test_file:  # metoda 'with'
    test_file.write("1.First String\n")
    test_file.write("2.Second String\n")
    test_file.write("3.Third String\n")  # aici metoda 'close()' se cheama automat
# ----Sfisrtsit de Metoda 2------

with open('test.txt') as test_file:  # metoda 'with'
    print(test_file.read())  # citim din fisier tot

with open('test.txt') as test_file:
    # lines = test_file.readlines()  # citim cu adugare in lista
    # for l in lines: # cu ciclu 'for in ' optinem 3 rinduri
    #     print(l)

    for l in test_file:  # la fel ca primul ciclu 'for in' nunmai optimizat
        print(l)

with open('test.txt') as test_file:
    print(test_file.readline())  # cu 'readline' se citeste numai un rind
    print(test_file.readline())  # citeste inca un rind
    print(test_file.readline())
    print(test_file.readline())

    while True: # citirea fisierului cu ajutorul 'while' + 'readline'
        l = test_file.readline()
        if not l:
            break
        print(l)

