print("Sarcina 1.")
# Creem functia 'dict_to_list' care ne itoarce o lista
# de tuples obtinuta din dictionar, daca keia e numar intreg
# atunci se inmultseste cu 2

my_dict = {
    1: 100,
    2: 200,
    'x': 1920,
    'y': 1080,
    36: 'Andrew'
}


def dict_to_list(dict):
    list = []
    # for item in dict.items():
    #     list.append(item)
    for item in dict.items():
        k, v = item
        if type(k) is int:
            k *= 2
        list.append((k, v))
    return list


new_list = dict_to_list(my_dict)
print(new_list)

print("Sarcina 2. Varianta 1.")
# De creeat o functie 'filter_list' care filtreaza listele dupa
# parametrul ei al doilea (int, float, str, bool, etc...)

my_list = [12, 34, True, False, 'Andrew', 'Good!']


def filter_list(list_to_filter, value_type):
    list_empty = []
    for elem in list_to_filter:
        if type(elem) is value_type:
            list_empty.append(elem)
    return list_empty


f_list = filter_list(my_list, str)
f_list2 = filter_list(['abc', 8, 10, True, 'dsa'], int)
print("my_list", my_list)
print("'my_list' filtrata cu 'filter_list' :", f_list)
print("Lista de la tastatura filtrata cu 'filter_list' :", f_list2)

print("Sarcina 2. Varianta 2. Fara ciclu 'for in' dar cu lambda functie")


def filter_list_lambda(list_to_filter, value_type):
    return list(filter(lambda elem: type(elem) is value_type, list_to_filter))


f_list3 = filter_list_lambda(my_list, str)
print("List filtrata cu 'filter_list_lambda' :", f_list3)
