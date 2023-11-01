# Реализуйте функцию  sum_of_digits() , которая принимает один аргумент:
# iterable  — итерируемый объект, элементами которого являются натуральные числа
# Функция должна возвращать единственное число — сумму цифр всех чисел, присутствующих в
# итерируемом объекте  iterable .

import itertools as it
from functools import reduce

def sum_of_digits(iterable):
    summ = 0
    for num in iterable:
        num_str = str(num)
        gener = (int(n) for n in num_str)
        summ += reduce(lambda x, y: y + x, gener, 0)
    return summ    




# TEST_1:
print(sum_of_digits([13, 20, 41, 2, 2, 5]))

# TEST_2:
print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

# TEST_3:
print(sum_of_digits([123456789]))

# TEST_4:
numbers = [10]*100

iterator = iter(numbers)
print(sum_of_digits(iterator))

# TEST_5:
numbers = [100, 20, 30, 400, 500, 5]*100000

print(sum_of_digits(numbers))