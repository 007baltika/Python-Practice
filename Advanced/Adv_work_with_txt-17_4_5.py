# Однажды Жака Фреско спросили:
# "Если ты такой умный, почему не богатый?"
# Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:
# "Были разноцветные козлы. Сколько?"
# "Сколько чего?"
# "Сколько из них составляет более 7% от общего количества козлов?"
# Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех возможных цветов козлов. 
# Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.
# Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки от Жака Фреско.

with open('33.txt', 'r') as input_file, open('output.txt', 'w') as output_file: 
    
    mass_colors = []
    goat_colors = []
    mass_goats_color = []
    mass_passed_7percent = []
    count_colors = 0
    mass_for_len = input_file.readlines()
    input_file.seek(0)
    line = input_file.readline()

    #Записал массив всех цветов - работает
    
    for i in range (0, len(mass_for_len)):
        line = input_file.readline().split()
        if line[0].lower() == 'goats': 
            break
        mass_colors.append(line[0].lower())
        mass_goats_color.append(' '.join(line))   
    
    #Сейчас нахожусь в начале массива козлов
    #Хочу чтобы я разбил козлов по количеству цветов
    #Получил количество цветов исходя из id [0, 0, 2, 0, 0, 2, 1, 0, 2, 2, 0, 0, 2, 2, 0] - goat_colors
    
    for j in range(i + 1, len(mass_for_len)):
        current_goat = input_file.readline()
        #print(current_goat)
        for k in range(0, len(mass_colors)):
            #print(mass_colors[k])
            if mass_colors[k].lower() in current_goat.lower():
                goat_colors.append(k)
        k = 0
    
    # Посчитал количество козлов по цветам
    # Количество pink = 8
    # Количество green = 1
    # Количество black = 6
    # Прошелся по цветам и проверил что количество козла определенного цвета больше 7% от общего числа, записал козла в массив и отсортировал
    
    for m in range(0, len(mass_colors)):
        for n in range(0, len(goat_colors)):
            if m == goat_colors[n]:
                count_colors += 1
        if ((count_colors / (len(mass_for_len) - 2)) * 100) > 7:
            mass_passed_7percent.append(mass_goats_color[m])
        count_colors = 0 
                  
    mass_passed_7percent.sort()        
    print(*mass_passed_7percent, sep = '\n', file = output_file)               