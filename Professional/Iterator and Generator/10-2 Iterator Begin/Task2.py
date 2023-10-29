# Реализуйте функцию  transpose()  с использованием функции  zip() , которая принимает один
# аргумент:
# matrix  — матрица произвольной размерности
# Функция должна возвращать транспонированную матрицу  matrix .

def transpose(matrix):
    new_matrix = zip(*matrix)
    mastr = []
    for stroka in new_matrix:
        mastr.append(list(stroka))
    return mastr
    
    

# TEST_1:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in transpose(matrix):
    print(row)
print()
# TEST_2:
matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10]]

for row in transpose(matrix):
    print(row)
print()
# TEST_3:
matrix = [[1, 2, 3, 4, 5]]

for row in transpose(matrix):
    print(row)
print()
# TEST_4:
matrix = [[69]]

for row in transpose(matrix):
    print(row)
print()
# TEST_5:
matrix = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']]

print(*transpose(matrix))
print()
# TEST_6:
matrix = [['1', '2'],
          ['4', '5'],
          ['7', '8'],
          ['3', 4],
          [True, None],
          [9, 80],
          [1, -1]]

print(transpose(matrix))  