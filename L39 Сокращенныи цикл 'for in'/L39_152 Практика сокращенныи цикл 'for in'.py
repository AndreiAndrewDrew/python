print("Ex.1. Din 'dict' optinem 'dict, set, list'")
my_scores = {
    'a': 10,
    'b': 20,
    'c': 30
}

new_scores = {}

for key, value in my_scores.items():  # Cu 'for in' obishnuit
    new_scores[key] = value * 2

new_scores2 = {key: value * 2 for key, value in my_scores.items()}  # Cu 'for in' redus

new_scores3 = {value * 2 for key, value in my_scores.items()}  # Daca nu indicam 'key'
# optinem multime Din 'dict' --> 'set'

new_scores4 = [value * 2 for key, value in my_scores.items()]  # Daca inlocuim '{}' cu '[]'
# optinem lista Din 'dict' ==> 'list'

print(my_scores)
print(new_scores)
print(new_scores2)
print(type(new_scores2))
print(new_scores3)
print(type(new_scores3))
print(new_scores4)
print(type(new_scores4))

print("Ex.2. Din 'list' optinem 'dict'")

my_list = [10, 7, 15]

new_dict = {index: elem * 2 for index, elem in enumerate(my_list)}

print(my_list)
print(new_dict)
