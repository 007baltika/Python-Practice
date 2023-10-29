# Если  count  имеет значение  None , функция должна возвращать генератор, порождающий
# бесконечный знакочередующийся ряд натуральных чисел.
# 1, −2, 3, −4, 5, −6, 7, −8, 9, −10, ...
# Если  count  имеет в качестве значения натуральное число, функция должна возвращать
# генератор, порождающий первые  count  чисел знакочередующегося ряда натуральных чисел, а
# затем возбуждающий исключение  StopIteration .

def alternating_sequence(count = None):
    i = 0
    if count == None:
        while True:
            i+=1 
            if i % 2 == 0:
                yield -i
            else: 
                yield i
    else:
        while i < count:
            i+=1 
            if i % 2 == 0:
                yield -i
            else: 
                yield i    
            


# TEST_1:
generator = alternating_sequence()

print(next(generator))
print(next(generator))
print()
# TEST_2:
generator = alternating_sequence(10)

print(*generator)
print()
# TEST_3:
generator = alternating_sequence(100)

print(*generator)
print()
# TEST_4:
generator = alternating_sequence(50)

for _ in generator:
    pass

try:
    next(generator)
except StopIteration:
    print('Error')
print()
# TEST_5:
generator = alternating_sequence()

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print()
# TEST_6:
generator = alternating_sequence()

for _ in range(10_124_421):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print()
# TEST_7:
generator = alternating_sequence(1)

try:
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')