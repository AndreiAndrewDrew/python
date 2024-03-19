class ExtendedList(list):
    def print_info_list(self):
        print(f"List has {len(self)} elements")
# Rezulta relatia: 'custom_list' - este subclasa 'ExtendedList'- este subclasa 'list' - este
# subclasa 'object' ('custom_list'-->'ExtendedList'-->'list'-->'object')

custom_list = ExtendedList([1, 2, 4, 5, 231, 2, 12])

custom_list.print_info_list()  # List has 7 elements
