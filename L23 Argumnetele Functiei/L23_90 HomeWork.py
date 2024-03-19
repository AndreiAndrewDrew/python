print("Sarcina 1")


def merge_lists_to_dict(list_a, list_b):
    zip_list_a_list_b = zip(list_a, list_b)
    dict_list_a_list_b = dict(zip_list_a_list_b)
    return dict_list_a_list_b


fruits = ['apple', 'banana', 'orange']
quantities = [100, 80, 20]
aviability = [True, False, False]

fruits_quantities_dict = merge_lists_to_dict(list_a=fruits, list_b=quantities)
print(fruits_quantities_dict)

fruits_quantities_dict = merge_lists_to_dict(fruits, list_b=quantities)
print(fruits_quantities_dict)

print("Sarcina 2")


def update_car_info(**car):
    print("Afisham Dict:", car)
    print("Tipul", type(car))
    car = {
        'brand': '',
        'price': 1,
        'is_avaible': True
    }
    return car


update_car_info(brand='opel', price=7000)
