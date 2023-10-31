# Реализуйте функцию  drop_while_negative() , которая принимает один аргумент:
# iterable  — итерируемый объект, элементами которого являются целые числа
# Функция должна возвращать итератор, генерирующий все числа итерируемого
# объекта  iterable , начиная с первого неотрицательного числа.

import itertools as it
def drop_while_negative(iterable):
    yield from it.dropwhile(lambda x: x < 0, iterable)





# TEST_1:
numbers = [-3, -2, -1, 0, 1, 2, 3]

print(*drop_while_negative(numbers))

# TEST_2:
iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])

print(*drop_while_negative(iterator))

# TEST_3:
iterator = iter([-3, -2, -1, -4, -5, -6])

print(list(drop_while_negative(iterator)))

# TEST_4:
iterator = iter([0, 1, 2, 3, 4, 5, 6, 7])

print(list(drop_while_negative(iterator)))

# TEST_5:
iterator = iter([-1, -2, -3, -4, -5, -6, 7])

print(*drop_while_negative(iterator))

# TEST_6:
iterator = iter([-1, 2, 3, 4, 5, 6, 7, 8])

print(*drop_while_negative(iterator))

# TEST_7:
iterator = iter([1])

print(*drop_while_negative(iterator))

# TEST_8:
iterator = iter([-1])

print(list(drop_while_negative(iterator)))

# TEST_9:
iterator = iter([])

print(list(drop_while_negative(iterator)))