from sys import getsizeof  # functai 'getsizeof' aflam marimea oricarui obiect

squares_gen = (num * num for num in range(1_000_000))

print("Marimea squares_gen in byte:",getsizeof(squares_gen)) # Marimea geneatorului tot timpul e mic

print(type(squares_gen))

for elem in squares_gen:
    print(elem)
    if elem == 100:
        break

squares_list = [num * num for num in range(1_000_000)]

print("Marimea squares_list in byte:",getsizeof(squares_list))

print(type(squares_list))