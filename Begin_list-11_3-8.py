# На вход программе подается натуральное число n и n строк, а затем число k. 

# Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.

# put your python code here
n = int(input())
strings = []
strokatek = []
simbols = []
simvol = ''
o = ''
for i in range(1, n+1):
    nums = input()
    strings.append(nums)

k = int(input())
tek_k = k - 1
#все что выше работает - получили массив и к
for i in range(0, n):
    strokatek = strings[i]
    if len(strokatek) > tek_k:
        simvol = strokatek[tek_k]
        simbols.append(simvol)
#print(simbols)
#получил массив из 4х символов - все работает
for i in range(0, len(simbols)):
    o = o + simbols[i]
print(o)    
#превращаю массив в строку