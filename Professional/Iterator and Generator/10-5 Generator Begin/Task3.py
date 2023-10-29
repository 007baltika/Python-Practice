# Функция должна возвращать генератор, порождающий последовательность простых чисел
# от  left  до  right  включительно, а затем возбуждающий исключение  StopIteration .

def primes(left, right):
    c = 0
    for num in range(left, right+1):
        for delit in range(1, num+1):
            if num % delit == 0:
                c += 1
        if c == 2:
            c = 0 
            yield num      
        else: c = 0      



# TEST_1:
generator = primes(1, 15)

print(*generator)
print()
# TEST_2:
generator = primes(6, 36)

print(next(generator))
print(next(generator))
print()
# TEST_3:
generator = primes(37, 37)

try:
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')
print()
# TEST_4:
generator = primes(39, 83)

print(*generator)
print()
# TEST_5:
generator = primes(43, 79)

print(*generator)
print()
# TEST_6:
generator = primes(43, 72)

print(*generator)
print()
# TEST_7:
generator = primes(1000, 2000)

print(*generator)
print()
# TEST_8:
generator = primes(2000, 100000)

for _ in range(1000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))