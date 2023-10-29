#Существует фаул из нескольких строк, необходимо вывести случайную строку из этого файла
from random import *
file = input()

my_file = open(file)

a = my_file.readline()
mass_a = []

while a != '':
    line = a.rstrip()
    mass_a.append(line)
    a = my_file.readline()
    
print(choice(mass_a))    

my_file.close()