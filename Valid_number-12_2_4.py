# На вход программе подается строка текста. Напишите программу, которая определяет, является ли введенная строка корректным телефонным номером. 
# Строка текста является корректным телефонным номером, если она имеет формат:

# abc-def-hijk или 7-abc-def-hijk
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9

# put your python code here
s = input()

cifri = s.split()
#print(cifri) - строка - теперь массив
countcifr = 0
check1 = 0
check2 = 0
check3 = 0
check4 = 0
check5 = 0
check2_1 = 0
check2_2 = 0
check2_3 = 0
check2_4 = 0
check2_5 = 0
check2_6 = 0
check2_7 = 0
prov = 0
for i in range(0, len(s)):
    if s[i] in '0123456789-':
        countcifr = countcifr + 1
        
#if countcifr == len(s): print('YES')  - проверка что все индексы - и цифры

#для певрого номера
if countcifr == len(s):
    for i in range(0, 3): 
        if s[i] in '0123456789': 
            check1 = check1 + 1
    if s[3] == '-': check2 = 3
    for j in range(4, 7): 
        if s[j] in '0123456789': 
            check3 = check3 + 1
    if s[7] == '-': check4 = 3
    for k in range(8, len(s)): 
        if s[k] in '0123456789': 
            check5 = check5 + 1          
    if (check1 + check2 + check3 + check4 + check5) == 16: prov = 1
#для второго номера    
if countcifr == len(s) and prov == 0:
    if s[0] == '7' : check2_1 = 3
    if s[1] == '-': check2_2 = 3
    for l in range(2, 5): 
        if s[l] in '0123456789': 
            check2_3 = check2_3 + 1
    if s[5] == '-': check2_4 = 3
    for m in range(6, 9): 
        if s[m] in '0123456789': 
            check2_5 = check2_5 + 1
    if s[9] == '-': check2_6 = 3
    for n in range(10, len(s)): 
        if s[n] in '0123456789': 
            check2_7 = check2_7 + 1   
#print(check2_7)            
if (check1 + check2 + check3 + check4 + check5) == 16: print("YES")
elif (check2_1 + check2_2 + check2_3 + check2_4 + check2_5 + check2_6 + check2_7) == 22: print("YES")
else: print("NO")    