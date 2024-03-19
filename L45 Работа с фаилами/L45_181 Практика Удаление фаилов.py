from pathlib import Path

file = open('test1.txt', 'w') # creem fisierul din nou
file.close()

my_file = Path('test1.txt')

if my_file.exists():
    my_file.unlink()
