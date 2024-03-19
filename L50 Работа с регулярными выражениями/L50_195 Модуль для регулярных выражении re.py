import re

my_string = "My name is Andrew"

res = re.search('Andrew', my_string)
res2 = re.search('A....w', my_string)
res3 = re.search('A....w$', my_string)  # Simbol de sfirsit de rind
res4 = re.search('^M.', my_string)  # Simbol de inceput de rind

print(res)  # <re.Match object; span=(11, 17), match='Andrew'>
print(res2)  # rezultatul este la fel
print(res3)
print(res4)

print(res.span())  # (11, 17) inceputul si sfirsitul elementului
print(res.start())
print(res.end())