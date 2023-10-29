# Функция  starmap()  должна работать аналогично функции  map() , то есть возвращать итератор,
# элементами которого являются элементы итерируемого объекта  iterable , к которым была
# применена функция  func , с единственным отличием:  func  должна принимать не один
# аргумент — коллекцию (элемент  iterable ), а каждый элемент этой коллекции в качестве
# самостоятельного аргумента.

# persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]
# full_names = starmap(lambda name, surname: f'{name} {surname}', persons)

# pairs = [(1, 3), (2, 5), (6, 4)]
# print(*starmap(lambda a, b: a + b, pairs))



def starmap(func, iterable):
    otvet = []
    for element in iterable:
        otvet.append(func(*element))
    return otvet




# TEST_1:
pairs = [(1, 3), (2, 5), (6, 4)]

print(*starmap(lambda a, b: a + b, pairs))
print()
# TEST_2:
points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]

print(*starmap(lambda x, y, z: x * y * z, points))
print()
# TEST_3:
points = [(1, 1, 1, 0), (1, 1, 2, 0), (2, 2, 3, 10)]

print(*starmap(lambda x, y, z, t: x + y + z + t, points))
print()
# TEST_4:
points = [[10], [-9], [2]]

print(*starmap(lambda x: x ** 2, points))
print()
# TEST_5:
points = [(1, 1, 1, 0, 90),
          (1, 1, 2, 0, 67),
          (2, 2, 3, 10, -56),
          (5, 21, 3, 10, -56),
          (6, 24, 35, 100, 36),
          (8, 34, 3, 10, 56)]

print(*starmap(lambda x, y, z, t, w: x + y * z + t + w ** 6, points))