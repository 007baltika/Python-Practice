# Реализуйте функцию  random_numbers() , которая принимает два аргумента:
# left  — целое число
# right  — целое число
# Функция должна возвращать итератор, генерирующий бесконечную последовательность
# случайных целых чисел в диапазоне от  left  до  right  включительно.

import random

def random_numbers(left, right):
    
    def test_iter():
        values = list(range(left, right + 1))
        return random.choice(values)
    
    return iter(test_iter, left-1) 


# TEST_1:
iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))
print()
# TEST_2:
iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print()
# TEST_3:
iterator = random_numbers(-100, -92)

print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print()
# TEST_4:
iterator = random_numbers(5, 5)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print()
# TEST_5:
iterator = random_numbers(1000, 1001)

print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print()
# TEST_6:
iterator = random_numbers(-100, 99)

print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))