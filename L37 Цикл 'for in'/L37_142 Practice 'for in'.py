print("Ex.1 list")
for el in [1, 'abc', True]:
    print(type(el))
    print(el)

print(el)  # True -Se afisheaza ultima valoare din ultima iteratie

print("Ex.2 dict")
my_dict = {'id': 123, 'title': 'sdfsad'}

for key in my_dict:
    print(type(key))
    print(key, my_dict[key])
