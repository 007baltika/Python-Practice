# Реализуйте функцию  get_min_max() , которая принимает один аргумент:
# iterable  — итерируемый объект, элементы которого сравнимы между собой
# Функция должна возвращать кортеж, в котором первым элементом является минимальный
# элемент итерируемого объекта  iterable , вторым — максимальный элемент итерируемого
# объекта  iterable . Если итерируемый объект  iterable  пуст, функция должна вернуть
# значение  None .

def get_min_max(iterable):
    a = list(iterable)
    if bool(a): return (min(a), (max(a)))
    return None
    
    
# TEST_1:
iterable = iter(range(10))

print(get_min_max(iterable))
print()
# TEST_2:
iterable = [6, 4, 2, 33, 19, 1]

print(get_min_max(iterable))
print()
# TEST_3:
iterable = iter([])

print(get_min_max(iterable))
print()
# TEST_4:
data = iter((9, 9, 9, 9, 9))

print(get_min_max(data))
print()
# TEST_5:
data = iter(range(1, 101))

print(get_min_max(data))
print()
# TEST_6:
data = list(range(1, 101))[::-1]

print(get_min_max(data))
print()
# TEST_7:
data = iter([-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30])

print(get_min_max(data))
print()
# TEST_8:
data = iter([-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30, -100, 96, -100, 1, 2, -99, 96])

print(get_min_max(data))
print()
# TEST_9:
iterable = []

print(get_min_max(iterable))
print()
# TEST_10:
iterable = [69]

print(get_min_max(iterable))
print()
# TEST_11:
data = iter(range(100_000_000))

print(get_min_max(data))
print()
# TEST_12:
data = iter(['a', 'b', 'c', 'aaa', 'abc', 'cbc', 'bbb'])

print(get_min_max(data))
print()
# TEST_13:
data = iter(['bbb'])

print(get_min_max(data))