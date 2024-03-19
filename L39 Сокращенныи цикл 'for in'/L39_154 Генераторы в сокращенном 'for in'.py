numbers = (3, 5, 7)  # tuple

squares = (num * num for num in numbers)  # creem generator

squares2 = (num * num for num in range(6))  # creem generator

gen = (num * num for num in range(3))

squares3 = list(gen)  # convertam generatorul in lista

print(numbers)
print(squares)  # primim generator
print(type(squares))  # <class 'generator'>
print(squares2)
print(type(squares2))
for num in squares2:  # Executam iteratsiile
    print(num)

print(squares3)

nums = [2, 3, 4, 4]

generator = (num * num for num in nums)

squares4 = tuple(generator)  # convertam lista in tuple

print(squares4)

print("Prioritatea generatorului--Marimea")
from sys import getsizeof  # functai 'getsizeof' aflam marimea oricarui obiect

squares_gen = (num * num for num in range(1000))

print("Marimea squares_gen:",getsizeof(squares_gen)) # Marimea geneatorului tot timpul e mic

print(type(squares_gen))

squares_list = [num * num for num in range(1000)]

print("Marimea squares_list:",getsizeof(squares_list))

print(type(squares_list))