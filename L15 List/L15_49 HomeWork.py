# 1 Creati o lista cu 5 elemente de diferite tipuri
home_list = [True, 'Hi!', ':D', 10.5, 100]
# 2 stergetsi elemtul al 3-lea
del home_list[2]
print(home_list)
# 3 Afishazi lungeamea lsitei
print(len(home_list))
# 4 Schimbatsi ordinea in lista
del home_list[0]
print(home_list)
home_list[0] = 101.1
print(home_list)
home_list.sort()
print(home_list)
# 5 Creati inca o lista cu 2 elemente
other_home_list = [23, 56.8]
# 6 extindeti prima lista cu elematele din a 2 lista
home_list.extend(other_home_list)
# 7 afishatsi in terminal
print(home_list)