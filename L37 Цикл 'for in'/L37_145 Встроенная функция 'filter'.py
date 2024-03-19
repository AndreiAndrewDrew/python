# print(isinstance(True, bool))  # True - True face parte din 'bool'
# print(isinstance(True, int))  # True - din 'int'
# print(isinstance(True, object))  # True - si din 'object'
# print(int.__subclasses__())  # [<class 'bool'>] - asta inseamna ca 'bool'- este subclasa clasei 'int'


# Varianta 1 de functie
def filter_list(list_to_filter, value_type):
    def check_element_type(elem):
        return isinstance(elem, value_type)  # controlam daca elementul corespunde valorii clasei respective

    return list(filter(check_element_type, list_to_filter))


# Varianta 2 fara 'isinstance'
def filter_list2(list_to_filter, value_type):
    def check_element_type(elem):
        return type(elem) is value_type  # controlam daca elementul corespunde valorii clasei respective

    return list(filter(check_element_type, list_to_filter))


# Varianta 3 cu lambda
def filter_list3(list_to_filter, value_type):
    return list(filter(lambda elem: type(elem) is value_type, list_to_filter))


f_list = filter_list([2, 3, 4.5, True, 'asd'], int)  # [2, 3, True]
f_list2 = filter_list2([2, 3, 4.5, True, 'asd'], int)  # [2, 3]
f_list3 = filter_list3([2, 3, 4.5, True, 'asd'], int)  # [2, 3]

print(f_list)
print(f_list2)
print(f_list3)