
# Реализуйте функцию  is_rising() , которая принимает один аргумент:
# iterable  — итерируемый объект, элементами которого являются числа
# Функция должна возвращать  true , если элементы итерируемого объекта расположены строго
# по возрастанию, или  false  в противном случае.


import itertools as it
import copy

def is_rising(iterable):
    a=copy.deepcopy(iterable)
    return list(it.pairwise(a)) == list(it.takewhile(lambda tuple: tuple[0] < tuple[1], it.pairwise(iterable)))



# TEST_1:
print(is_rising([1, 2, 3, 4, 5]))

# TEST_2:
iterator = iter([1, 1, 1, 2, 3, 4])

print(is_rising(iterator))

# TEST_3:
iterator = iter(list(range(100, 200)))

print(is_rising(iterator))

# TEST_4:
iterator = iter(list(range(200, 100, -1)))

print(is_rising(iterator))

# TEST_5:
iterator = iter(list(range(100, 201)) + [200])

print(is_rising(iterator))

# TEST_6:
iterator = iter([10]*50)

print(is_rising(iterator))