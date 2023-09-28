#Получаю на вход фаул и вывожу ее предпоследнюю строку

file = input()

my_file = open(file)

a = my_file.readline()
mass_a = []

while a != '':
    line = a.rstrip()
    mass_a.append(line)
    a = my_file.readline()
    
print(mass_a[-2])    

my_file.close()