print("Exemplu 1a. Cu simplu 'for in'")

all_nums1a = [-3, -4, 7, 1, 2, 0, -3]

absolute_nums1a = []

for num1a in all_nums1a:
    absolute_nums1a.append(abs(num1a))

print(all_nums1a)
print(absolute_nums1a)

print("Exemplu 1b. Cu 'for in' redus")

all_nums1b = [-3, -4, 7, 1, 2, 0, -3]

absolute_nums1b = [abs(num1b) for num1b in all_nums1b]

print(all_nums1b)

print(absolute_nums1b)

print("Exemplu 2a. Cu 'for in' simplu")

all_nums2a = [-3, -4, 7, 1, 2, 0, -3]

positive_num2a = []

for num2a in all_nums2a:
    if num2a > 0:
        positive_num2a.append(num2a)

print(all_nums2a)

print(positive_num2a)

print("Exemplu 2b. Cu 'for in' Redus")

all_nums2b = [-3, -4, 7, 1, 2, 0, -3]

positive_num2b = [num2b for num2b in all_nums2b if num2b > 0]

print(all_nums2b)

print(positive_num2b)
