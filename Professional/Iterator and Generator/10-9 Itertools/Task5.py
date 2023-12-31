# Реализуйте функцию  take_nth() , которая принимает два аргумента в следующем порядке:
# iterable  — итерируемый объект
# n  — натуральное число
# Функция должна возвращать  n -ый по счету элемент итерируемого объекта  iterable . Если
# итерируемый объект  iterable  содержит менее  n  элементов, функция должна вернуть
# значение  None .



import itertools as it

def take_nth(iterable, n):
    a = list(iterable)
    if n <= len(a):
        mass = list(it.islice(a, n))
        return mass[-1]
    else: return None




# INPUT DATA:

# TEST_1:
numbers = [11, 22, 33, 44, 55]

print(take_nth(numbers, 3))

# TEST_2:
iterator = iter('beegeek')

print(take_nth(iterator, 4))

# TEST_3:
iterator = iter('beegeek')

print(take_nth(iterator, 10))

# TEST_4:
iterator = iter('beegeek')

print(take_nth(iterator, 1))

# TEST_5:
iterator = tuple('stepik')

print(take_nth(iterator, 6))

# TEST_6:
iterator = iter('p')

print(take_nth(iterator, 1))

# TEST_7:
iterator = iter('p')

print(take_nth(iterator, 2))

# TEST_8:
iterator = iter('beegeek')

print(take_nth(iterator, 7))

# TEST_9:
iterator = iter('beegeek')

print(take_nth(iterator, 8))

# TEST_10:
print(take_nth([], 4))