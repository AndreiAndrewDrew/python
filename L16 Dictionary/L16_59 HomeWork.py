hw_cars = {}

key_name1 = input("Enter key_name1: ")
value1 = input("Enter value1: ")
hw_cars[key_name1] = value1
print(hw_cars)

key_name2 = input("Enter key_name2: ")
value2 = input("Enter value2: ")
hw_cars[key_name2] = float(value2)
print(hw_cars)

key_name3 = input("Enter key_name3: ")
value3 = input("Enter value3: ")
hw_cars[key_name3] = int(value3)
print(hw_cars)

hw_cars['add1key'] = 'sdkjfsjkda'  # aduagam o keie noua cu valoare
print(hw_cars)

del hw_cars['add1key']
del hw_cars[key_name3]
print(hw_cars)
