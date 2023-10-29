# Если  count  имеет значение  None , функция должна возвращать генератор, порождающий
# последовательность из максимально допустимого количества дат (тип  date ), начиная с
# даты  start .

# Если  count  имеет в качестве значения натуральное число, функция должна возвращать
# генератор, порождающий последовательность из  count  дат (тип  date ), начиная с даты  start ,
# а затем возбуждающий исключение  StopIteration .

from datetime import timedelta, date

def dates(start, count = None):
    i = 0
    if count == None:
        while True:
            i+=1
            yield (start + timedelta(days=i-1))
    else: 
        while i < count:
            i+=1
            yield (start + timedelta(days=i-1))   
                    
        



# TEST_1:
generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))
print()
# TEST_2:
generator = dates(date(2022, 3, 8), 5)

print(*generator)
print()
# TEST_3:
generator = dates(date(2025, 9, 11), 99)

print(*generator)
print()
# TEST_4:
generator = dates(date(2024, 9, 13), 1)

try:
    d = next(generator)
    print(type(d))
    print(d)
    next(generator)
except StopIteration:
    print('Error')
print()
# TEST_5:
generator = dates(date(2049, 1, 7))

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
print(next(generator))
print()
# TEST_6:
generator = dates(date(9999, 1, 7))

for _ in range(348):
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
print(next(generator))

try:
   print(next(generator))
except StopIteration:
    print('Error')