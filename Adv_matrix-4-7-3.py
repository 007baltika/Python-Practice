# Напишите программу, которая возводит квадратную матрицу в m-ую степень.
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы, затем натуральное число m.

import copy
n = int(input())

matrix = []

for matr in range(n):
    matr_string = [int(num) for num in input().split()]
    matrix.append(matr_string)
        
matr_2 = [[0] * n for _ in range(n)]
m = int(input())    

matrix_num = 0

matrix_umnozhennaya = copy.deepcopy(matrix)

for iter_nums in range(m-1):
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                matr_mult = matrix_umnozhennaya[i][k] * matrix[k][j]
                matrix_num = matrix_num + matr_mult 
            matr_2[i][j] = copy.deepcopy(matrix_num)
            matrix_num = 0
    matrix_umnozhennaya = copy.deepcopy(matr_2)            

for matrix_lines in range(0, len(matrix_umnozhennaya)):
    print(*matrix_umnozhennaya[matrix_lines])