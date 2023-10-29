# Функция должна возвращать генератор, порождающий бесконечную возрастающую
# последовательность натуральных чисел, в которой каждое число встречается столько раз,
# каково оно:

def simple_sequence():
    start = 1
    while 1 != 2:
        for i in range(1, start + 1):
            yield start
        start += 1
        

# TEST_1:
generator = simple_sequence()

print(next(generator))
print(next(generator))
print()
# TEST_2:
generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]

print(*numbers)
print()
# TEST_3:
generator = simple_sequence()

for _ in range(100):
    print(next(generator))
print()
# TEST_4:
generator = simple_sequence()

for _ in range(1000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print()
# TEST_5:
generator = simple_sequence()

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print()
# TEST_6:
generator = simple_sequence()

for _ in range(10_000_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))