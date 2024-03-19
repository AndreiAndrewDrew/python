from pathlib import Path  # obiect- orientat padhod

file_path = Path('test.txt')

print([m for m in dir(file_path)
       if not m.startswith('_')])  # '_' excludem metodele
print(Path.cwd())  # Calea spre directoria curenta

print(Path('C:/').joinpath('Users').joinpath('andrew'))  # CREAREA MANUALA a caii in windows
print(Path('C:/') / 'Users' / 'andrew')  # la fel

print(Path('L45_176 Работа с фаилами (os vs pathlib).py').exists())
print(Path('/1.PhytonProjects (2023)[Udemy]/python/L45 Работа с фаилами').exists())
print(Path('other.py').exists())

print(Path('L45_176 Работа с фаилами (os vs pathlib).py').is_file())
print(Path('../L45 Работа с фаилами').is_dir())
print(Path('../L45 Работа с фаилами').is_file())

print("Afisham toate fisierele care sunt in mapa de lucru:")
for f in Path('.').iterdir():
    print(f)
