from array import array

my_int_array = array('i', [4, 1, 4, 56, 8])  # 'i' - numai elemente de type integer

print(my_int_array)
print(type(my_int_array))  # <class 'array.array'>

my_int_array.append(15)  # adugam un element nou in tabel
print(my_int_array)

print(my_int_array.count(4))  # NUmaram de cite ori in tabel se repta elementul '4'

my_int_array.pop()  # metoda 'pop()' sterge ultimul element din masiv
print(my_int_array)
print("Lungimea Tabeluli:", len(my_int_array))  # 5 ==lungimea tabelului

my_int_array.append(22)
my_int_array.append(33)
print(my_int_array)
# facem iteratii pe masiv
for el in my_int_array:  # Iteratie simpla
    print(el)

i = 1
while i <= len(my_int_array):  # Iteratie by Andrew, cu atribuirea nr de ordinea a lementului din tabel
    for element in my_int_array:
        print(f"Elemtul {i} = {element}")
        i += 1
print("primul element: ", my_int_array[0])

with open('my_array.bin', 'wb') as my_file:  # creem un fisier 'my_array.bin'
    my_int_array.tofile(my_file)  # cu 'tofile()' inscriem masivul nostru in fisier 'my_array.bin'
    print("Datele s-au Inscris!")

imported_array = array('i')  # masiv care va fi impotrat din 'my_array.bin'
with open('my_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 4)  # vrem sa importam primele 4 elemente
    print(imported_array)

imported_array.reverse()  # metoda de a intorce invers masivul
print(imported_array)
