def merge_lists_to_dict(list_a, list_b):
    zip_list_a_list_b = zip(list_a, list_b)
    dict_list_a_list_b = dict(zip_list_a_list_b)
    return dict_list_a_list_b


fruits = ['apple', 'banana', 'orange']
quantities = [100, 80, 20]
aviability = [True, False, False]

fruits_quantities_dict = merge_lists_to_dict(fruits, quantities)
print(fruits_quantities_dict)

quantities_aviability_dict = merge_lists_to_dict(quantities, aviability)
print(quantities_aviability_dict)

fruits_aviability_dict = merge_lists_to_dict(fruits, aviability)
print(fruits_aviability_dict)
