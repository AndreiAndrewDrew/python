print("Ex.1")
my_dict = {
    'x': 10,
    'y': True
}

for item in my_dict.items():
    print(item)  # Obtinem 2 Tuple

for item in my_dict.items():
    k, v = item  # Raspakovka Tuple 'item'
    print(k, v)

print("Ex.2")
my_dict = {
    'x': 10,
    'y': True
}

for k, v in my_dict.items(): # Raspakovka deodata in rinidul 'for in'
    print(k, v)
