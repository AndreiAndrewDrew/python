int_num = 3
float_num = 4.3
print(int_num + float_num)
print(type(int_num + float_num))
print(float_num + int_num)
print(type(float_num + int_num))

bool_value = True
int_value = 7
print(bool_value + int_value)  # rez este 8 valoarea True este 1
# respectiv 1 +7 = 8
print(type(bool_value + int_value))
print(int_value + bool_value) # la fel 8

str_value = 'abc'
print(int_value * str_value)
print(type(int_value * str_value))
print(str_value * int_value)

#print(float_num * str_value)# Eroare cu float string nu se imnulteste