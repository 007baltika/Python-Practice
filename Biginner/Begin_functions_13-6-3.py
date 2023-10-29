# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты квадратного уравнения 
# и возвращает его корни в порядке возрастания.

# объявление функции
from math import *
def solve(a, b, c):
    d = pow(b, 2) - 4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
    if d == 0:
        x1 = -b / (2 * a)
        x2 = -b / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
        
    return x1, x2
# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)