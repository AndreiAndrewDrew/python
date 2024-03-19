class ExtendedList(list):
    def print_info_list(self):
        print(f"List has {len(self)} elements")


custom_list = ExtendedList([1, 2, 4, 5, 231, 2, 12])

custom_list.append(777)

print(custom_list)
custom_list.print_info_list()

custom_list.remove(777)

print(custom_list)
custom_list.print_info_list()  # List has 7 elements

print(custom_list.__dict__)  # {} atribute proprii nu are exemplearu 'custom_list'

print(ExtendedList.__dict__)
print(list.__dict__)
print(object.__dict__)

print(list.__subclasses__())  # [<class '__main__.ExtendedList'>]
                              # Are o singura subclasa 'ExtendedList'
print(object.__subclasses__())


class MyExtendedList(ExtendedList): # Creeem clasa 'MyExtendedList' care este subclasa 'ExtendedList'
    def print_info_list(self):
        print(f"List has {len(self)} elements")

print(list.__subclasses__())  # [<class '__main__.ExtendedList'>]
                              # Are o singura subclasa 'ExtendedList'
print(ExtendedList.__subclasses__()) # [<class '__main__.MyExtendedList'>]
                                     # Are o singura subclasa 'MyExtendedList'