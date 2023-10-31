# Реализуйте функцию  first_true() , которая принимает два аргумента в следующем порядке:
# iterable  — итерируемый объект
# predicate  — функция-предикат; если имеет значение  None , то работает аналогично
# функции  bool()
# Функция  first_true()  должна возвращать первый по счету элемент итерируемого
# объекта  iterable , для которого функция  predicate  вернула значение  true . Если такого
# элемента нет, функция  first_true()  должна вернуть значение  None .


import itertools as it

def first_true(iterable, predicate = None):
    if predicate == None:
        first = list(filter(lambda x: bool(x) == True, iterable))
        if first != []: return first[0]
    else:
        first = list(filter(predicate, iterable))
        if first != []: return first[0]



# INPUT DATA:

# TEST_1:
numbers = [1, 1, 1, 1, 2, 4, 5, 6]

print(first_true(numbers, lambda num: num % 2 == 0))

# TEST_2:
numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num > 10))

# TEST_3:
numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)

print(first_true(numbers, None))

# TEST_4:
numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 0, 10, 100, 200)
numbers_iter = filter(None, numbers)

print(first_true(numbers_iter, lambda num: num < 0))

# TEST_5:
numbers = [10000]

print(first_true(numbers, lambda num: num % 2 == 0))

# TEST_6:
numbers = [10000]

print(first_true(numbers, lambda num: num % 2 == 1))

# TEST_7:
numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num == 200))

# TEST_8:
numbers = iter([])

print(first_true(numbers, lambda num: num == 200))