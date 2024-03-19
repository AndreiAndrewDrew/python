user_input = input("Enter any number: ")
any_number = int(user_input)  # inputul la user il convertam in
# tipul 'int', po defaultu e 'str'

any_number_v2 = int(input("Enter any number2: "))
# alta varianta de convertatsie

print(any_number)
print(type(any_number))

base = 2
power = 3
print(pow(base, power))
print(type(pow(base, power)))
one_milion = 1_000_000  # cifrele mari spoate de separat cu '_'
print(one_milion)

number_d = 3_142
print(number_d)

str_temperature = '23.6'
teperature = float(str_temperature)
print(teperature)
print(type(teperature))

average_price = 28.6
print(round(average_price))

rate = 0.79
print(round(rate))
print(type(round(rate)))

complex_a = 3 + 6j
complex_b = 4 + 7j
sum = complex_b + complex_a
dif = complex_a - complex_b
inmul = complex_a * complex_b

print(sum)
print(dif)
print(inmul)
print(type(sum))
