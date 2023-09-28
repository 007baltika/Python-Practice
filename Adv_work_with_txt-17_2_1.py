#Существует какой-то txt файл и я построчно считываю его, выводя данные в консоль

file = input()

my_file = open(file)

line = my_file.readline()

while line != '':
    print(line.rstrip())
    line = my_file.readline()
    
my_file.close()