# Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и оценка разделены пробелом). 
# Оценка - целое число от 0 до 100 включительно.

# Напишите программу для добавления 5 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в файл new_scores.txt.


with open('class_scores.txt', 'r') as input_file, open('new_scores.txt', 'w') as output_file:
    mass_lines = input_file.readlines()
    
    input_file.seek(0)
    
    for i in range(0, len(mass_lines)):
        line = input_file.readline().split()
        point = int(line[1]) + 5
        if point > 100:
            print(f'{line[0]} {100}', file = output_file)
        else: print(f'{line[0]} {point}', file = output_file) 