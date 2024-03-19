my_fruits = ['apple', 'banana', 'lime']

my_apple = my_fruits[0]  # metoda clasa de atribuire
my_banana = my_fruits[1]
my_lime = my_fruits[2]

print(my_apple)
print(my_banana)
print(my_lime)

my_list = [1, 2, 3]

first, second, third = my_list

print(first)
print(second)
print(third)

my_fruits_t = ('apple', 'banana', 'lime')  # deja nu lista dar tuple

my_apple_t, my_banana_t, my_lime_t = my_fruits_t

print(my_apple_t)
print(my_banana_t)
print(my_lime_t)

my_fruits = ['apple', 'banana', 'lime']

my_apple, *remaning_fruits = my_fruits

print(my_apple)
print(remaning_fruits)

print(type(remaning_fruits))