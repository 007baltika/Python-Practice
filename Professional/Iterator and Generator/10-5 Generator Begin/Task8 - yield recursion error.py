# Реализуйте генераторную функцию  palindromes() , которая не принимает никаких аргументов.
# Функция должна возвращать генератор, порождающий бесконечную последовательность
# натуральных чисел-палиндромов.



def palindromes():
    start = 1
    while True:
        if str(start) == str(start)[::-1]:
            yield start
        start += 1        
    # yield from palindromes(start + 1) - проблемы с рекурсией
    


# TEST_1:
generator = palindromes()

print(next(generator))
print(next(generator))
print(next(generator))
print()
# TEST_2:
generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)
print()
# TEST_3:
generator = palindromes()

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
print()
# TEST_4:
generator = palindromes()

for _ in range(1_000):
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
print()
# TEST_5:
generator = palindromes()

for _ in range(100):
    print(next(generator))