print("Ex.1 Afisham elementele List")

my_list = [True, 10, 'abc', {}]

for elem in my_list:  # afisham fiecare element din lista
    print(elem)

print("Ex.2 Afisham elementele Tuple")

video_info = ('1920x1080', True, 24)

for elem in video_info:
    print(elem)

print("Ex.3 Afisham elementele Dict")

my_dict = {
    'x': 10,
    'y': True,
    'z': 'abc'
}

for key in my_dict:
    print(key, my_dict[key])
