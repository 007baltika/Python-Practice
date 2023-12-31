# Формат входных данных
# На вход программе подается натуральное число n, далее следует n строк с фамилией школьника и его оценкой на каждой из них.

# Формат выходных данных
# Программа должна вывести сначала все введённые строки с фамилиями и оценками учеников в том же порядке. Затем следует пустая строка, а затем выводятся строки с фамилиями и оценками хорошистов и отличников (в том же порядке).

# Примечание 1. Оценка ученика – это натуральное число от 1 до 5

# Примечание 2. Гарантируется, что в классе есть хотя бы один хорошист – обладатель оценки 4, или отличник – получивший 5

n = int(input())
mass_name = []
for i in range(n): 
    s = input()
    mass_name.append(s)
print(*mass_name, sep = '\n')
print()
mass_otl = [x.split() for x in mass_name if int(x.split()[1]) > 3]
mass_otl = [' '.join(x) for x in mass_otl]
print(*mass_otl, sep = '\n')    