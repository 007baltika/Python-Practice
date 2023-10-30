# Реализуйте генераторную функцию  all_together()  с использованием генераторных
# выражений, которая принимает произвольное количество позиционных аргументов, каждый из
# которых является итерируемым объектом.
# Функция должна возвращать генератор, порождающий каждый элемент всех переданных
# итерируемых объектов: сначала все элементы первого итерируемого объекта, затем второго, и
# так далее.

def all_together(*args):
    for element in args:
        yield from element

    
    
    
# TEST_1:
objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))

# TEST_2:
objects = [[1, 2, 3], [(0, 0), (1, 1)], {'geek': 1}]

print(*all_together(*objects))

# TEST_3:
print(list(all_together()))

# TEST_4:
objects = [iter('bee'), [[1, 2], [3, 4], [5, 6]], {'geek': 1, 'bee': 2}]

print(*all_together(*objects))

# TEST_5:
_map = map(str.upper, 'beegeek')
_filter = filter(str.islower, 'BEEgeek')
_zip = zip('bee', '123')

print(*all_together(_map, _filter, _zip))

# TEST_6:
_map = map(str.upper, 'stepik')
_filter = filter(str.islower, 'beeGEEK')
_zip = zip('zip', '321')
_reversed = reversed([1, 2, 3, 4])
_enumerate = enumerate('bee')

print(*all_together(_map, _filter, _zip, _reversed, _enumerate))    