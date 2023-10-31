# Функция должна возвращать итератор, генерирующий последовательность из  n  чисел, каждое
# из которых является факториалом очередного натурального числа.

import itertools as it
import operator

def factorials(n):
    mass = list(num for num in range(1, n+1))
    yield from it.accumulate(mass, operator.mul)



# TEST_1:
numbers = factorials(6)

print(*numbers)
print()
# TEST_2:
numbers = factorials(2)

print(next(numbers))
print(next(numbers))
print()
# TEST_3:
numbers = factorials(100)

print(*numbers)
print()
# TEST_4:
numbers = factorials(1001)

for _ in range(1000):
    next(numbers)

print(next(numbers))