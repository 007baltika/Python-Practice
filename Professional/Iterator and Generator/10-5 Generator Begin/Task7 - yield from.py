# генераторная функция  matrix_by_elem() , которая принимает в качестве
# аргумента матрицу произвольной размерности и возвращает генератор, порождающий
# последовательность элементов переданной матрицы.

def matrix_by_elem(matrix):
    for str in matrix:
        yield from str
    
    
    
# TEST_1:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(*matrix_by_elem(matrix))
print()
# TEST_2:
matrix = [[1, 2, 3],
          [4, 5, 6]]

print(list(matrix_by_elem(matrix)))
print()
# TEST_3:
matrix = [[1, 2, 3, 5, 6, 7, 8],
          [9, 10, 11, 12, 13, 14, 15]]

print(list(matrix_by_elem(matrix)))
print()
# TEST_4:
matrix = [[1, 2, 3, 5, 6, 7, 8],
          [9, 10, 11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20, 21, 22]]

print(tuple(matrix_by_elem(matrix)))  