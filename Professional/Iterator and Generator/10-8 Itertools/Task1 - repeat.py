# Функция  tabulate()  должна возвращать итератор, генерирующий бесконечную
# последовательность возвращаемых значений функции  func  сначала с аргументом 1, затем 2,
# затем 3, и так далее.


import itertools as it

def tabulate(func):
    for a in map(func, it.count(1)):
        yield a




# TEST_1:
func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))
print()
# TEST_2:
func = lambda x: x + 10
values = tabulate(func)

print(next(values))
print(next(values))
print(next(values))
print()
# TEST_3:
func = lambda x: x ** 2
values = tabulate(func)

for _ in range(100):
    print(next(values))
print()
# TEST_4:
def func(n):
    return 'beegeek' * n

values = tabulate(func)

for _ in range(10):
    print(next(values))