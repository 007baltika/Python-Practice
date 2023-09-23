#Ищем в файле строку с максимальным количеством элементов, если таких строк несколько, то вывести все

file = open('22.txt', encoding='utf-8')

mass_lines = [line.strip() for line in file.readlines()]

print(mass_lines)
max_lines = []
all_max_lines = []

max_line = max(mass_lines, key = len)
#print(max_line)

for i in range(0, len(mass_lines)):
    if len(mass_lines[i]) == len(max_line):
        all_max_lines.append(mass_lines[i])
        
print(*all_max_lines, sep = '\n')  

file.close()      

#while line != '':
    

