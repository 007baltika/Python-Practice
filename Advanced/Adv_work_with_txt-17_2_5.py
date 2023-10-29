# Вам доступен текстовый файл nums.txt. В файле записано два целых числа, они могут быть разделены символами пробела и конца строки. 
#  Напишите программу, выводящую на экран сумму этих чисел.
from random import *

my_file = open('22.txt')

a = my_file.read()

num = ''
mass_num = []

for i in range(0, len(a)):
    if a[i] in '0123456789':
        num = num + a[i]
    if a[i] not in '0123456789':
        if len(num) > 0:
            mass_num.append(int(num))
        num = ''
if a[(len(a) - 1)] in '0123456789':
    mass_num.append(int(num))            


print(sum(mass_num))    

my_file.close()