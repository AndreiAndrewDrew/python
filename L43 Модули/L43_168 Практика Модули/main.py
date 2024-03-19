# import other as other_module # importeaza cu redenumire
#
# print(other_module)
# print(type(other_module))
# print(dir(other_module))
#
# other_module.print_sum(3,4)
# other_module.print_sum(3.45,4.54543)
#
# print(other_module.my_name)

# from other import my_name, print_sum # importeaza anumite variabile
from other import *  # '*' importeaza toate variabilele din module

print(my_name)
print_sum(3, 8)
