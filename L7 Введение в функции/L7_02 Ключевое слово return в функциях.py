def sum_nums(a, b):
    sum = a + b
    print(sum)


sum_nums(10, 5)
sum_nums(50.34, 21)


# Cu ajutorul return

def sum_nums2(a, b):
    sum = a + b
    return sum

first_sum = sum_nums2(10,5)
print(first_sum)
second_sum = sum_nums2(50.22, 11)
print(second_sum)