# Функция должна возвращать генератор, порождающий последовательность элементов
# итерируемого объекта  iterable  до тех пор, пока не будет достигнут элемент, равный  obj . Если
# итерируемый объект  iterable  не содержит ни одного элемента, равного  obj , генератор
# должен породить все элементы  iterable .


def stop_on(iterable, obj):
    a = iter(iterable)
    def func():
        return next(a)

    return iter(func, obj)


# TEST_1:
numbers = [1, 2, 3, 4, 5]

print(*stop_on(numbers, 4))
print()
# TEST_2:
iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))
print()
# TEST_3:
data = map(abs, range(-100, 100))

iterator = stop_on(data, 76)

print(*iterator)
print()
# TEST_4:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

iterator = stop_on(data, 'o')

print(*iterator)
print()
# TEST_5:
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

iterator = stop_on(data, 'e')

print(*iterator)
print()
# TEST_6:
data = 'g'

iterator = stop_on(data, 'g')

print(*iterator)
print()
# TEST_7:
data = 'eeeeeeeeeeeeee'

iterator = stop_on(data, 'e')

print(*iterator)
print()
# TEST_8:
data = iter('qweretqwewerqweqwerewr')

iterator = stop_on(data, 'H')

print(*iterator)
print()
# TEST_9:
data = iter('beegeek')

iterator = stop_on(data, 'g')

print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print('Error')
print()
# TEST_10:
data = ['bee', 'geek', 'stepik', 'python']

print(*stop_on(data, 'stepik'))
print()
# TEST_11:
data = []

print(list(stop_on(data, 'stepik')))