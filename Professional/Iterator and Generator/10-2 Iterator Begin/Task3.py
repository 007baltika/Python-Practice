# Реализуйте функцию  get_min_max()  c использованием функции  enumerate() , которая
# принимает один аргумент:
# data  — список произвольных объектов, сравнимых между собой
# Функция должна возвращать кортеж, в котором первым элементом является индекс
# минимального элемента в списке  data , вторым — индекс максимального элемента в
# списке  data . Если список  data  пуст, функция должна вернуть значение  None .

def get_min_max(data):
    
    if bool(data): return((data.index(min(data)), data.index(max(data))))
    return None

# TEST_1:
data = [2, 3, 8, 1, 7]

print(get_min_max(data))
print()
# TEST_2:
data = [1, 1, 2, 3, 8, 8]

print(get_min_max(data))
print()
# TEST_3:
data = [9]

print(get_min_max(data))
print()
# TEST_4:
data = []

print(get_min_max(data))
print()
# TEST_5:
data = [9, 9, 9, 9, 9]

print(get_min_max(data))
print()
# TEST_6:
data = list(range(1, 101))

print(get_min_max(data))
print()
# TEST_7:
data = list(range(1, 101))[::-1]

print(get_min_max(data))
print()
# TEST_8:
data = [-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30]

print(get_min_max(data))
print()
# TEST_9:
data = [-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30, -100, 96, -100, 1, 2, -99, 96]

print(get_min_max(data))