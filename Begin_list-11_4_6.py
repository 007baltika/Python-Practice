# На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем 

# k строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются одновременно все поисковые запросы.

# put your python code here
n = int(input())
stroki = []
zaprosi = []
otvet = []
c = 0

for l in range(1, n+1):
    stroka = input()
    stroki.append(stroka)
#print(stroki)

c_zaprosov = int(input())

for k in range(1, c_zaprosov + 1):
    zapros = input()
    zaprosi.append(zapros)
#print(zaprosi)    

#print(len(stroki)) = 5
#вверху вроде все верно
#вроде правильная длина
for i in range(0, len(stroki)): 
    for j in range(0, len(zaprosi)):
        if zaprosi[j].lower() in stroki[i].lower():
            c = c + 1
    if c == len(zaprosi):
        otvet.append(stroki[i])
    c = 0    

#        else: del stroki[i]            
print(*otvet, sep = '\n')    