import module_one
import module_one as m_1 # se importeaza modulul cu schimbarea numelui 'm_1'
from module_one import print_name # se importeaza functia 'print_name' din 'module_one'

print(type(module_one))
print(dir(module_one))

module_one.print_name("Andrew hello!")
m_1.print_name("Hello 2")
print_name("hello 3")
