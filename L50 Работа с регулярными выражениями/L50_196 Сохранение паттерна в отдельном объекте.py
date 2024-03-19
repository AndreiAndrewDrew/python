import re

my_string = "My name is Andrew."
other_string = "My name is Andrew!"

res = re.search(r'A....w\.$', my_string)

my_pattern = re.compile(r'A....w\.$')  # creem pattern
my_pattern2 = re.compile(r'^My.*\.$')

print(res)

print(my_pattern)

print(my_pattern.search(my_string))  # <re.Match object; span=(11, 18), match='Andrew.'>
print(my_pattern2.match(my_string))  # <re.Match object; span=(0, 18), match='My name is Andrew.'>
print(my_pattern2.match(other_string))  # None - nu corespunde cu expresia din pattern

my_string3 = "My name is Andrew. Aoooow is student"
my_pattern3 = re.compile(r'A....w')

print(my_pattern3.findall(my_string3))

