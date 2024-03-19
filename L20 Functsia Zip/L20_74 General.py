fruits = ['apple', 'banana', 'orange']
quantities = [100, 80, 24]
avaibility = [True, False, False]

fruits_quantities_zip = zip(fruits, quantities, avaibility)  # unim cu Zip
print("Am unit listele in 'fruits_quantities_zip':",fruits_quantities_zip)
fruits_quantities_zip = list(fruits_quantities_zip)
print("Am convertat Zipul in lista din tupluri:", fruits_quantities_zip)
