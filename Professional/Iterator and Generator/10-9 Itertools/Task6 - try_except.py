# Реализуйте функцию  first_largest() , которая принимает два аргумента в следующем
# порядке:
# iterable  — итерируемый объект, элементами которого являются целые числа
# number  — произвольное число
# Функция должна возвращать индекс первого элемента итерируемого объекта  iterable ,
# который больше  number . Если таких элементов нет, функция должна вернуть число −1.


import itertools as it

def first_largest(iterable, number):
    mass = list(map(lambda x: x < number, iterable))
    try:
        return mass.index(False)
    except ValueError:
        return -1



# INPUT DATA:

# TEST_1:
numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))

# TEST_2:
iterator = iter([-1, -2, -3, -4, -5])

print(first_largest(iterator, 10))

# TEST_3:
iterator = iter([18, 21, 14, 72, 73, 18, 20])

print(first_largest(iterator, 10))

# TEST_4:
iterator = iter([18, 21, 14, 72, 73, 18, 20, 101, 102, 110])

print(first_largest(iterator, 105))

# TEST_5:
iterator = iter([123, 423, 224, 722, 713, 158, 230, 1101, 1022, 1210, 222, 333, 334])

print(first_largest(iterator, 105))

# TEST_6:
iterator = iter([2, 3, 4, 5, 6, 7, 8, 999])

print(first_largest(iterator, 105))

# TEST_7:
iterator = iter([999])

print(first_largest(iterator, 105))

# TEST_8:
iterator = iter([998])

print(first_largest(iterator, 999))

# TEST_9:
iterator = iter([4, 100, 102, 334, 5])

print(first_largest(iterator, 101))

# TEST_10:
print(first_largest([], 7))

# TEST_11:
iterator = iter([-400, -100, -102, -334, -5])

print(first_largest(iterator, -6))