# Реализуйте генераторную функцию, которая принимает один аргумент:
# iterable  — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность кортежей, каждый
# из которых содержит очередной элемент итерируемого объекта  iterable , а также предыдущий
# и следующий за ним элементы:
# (<предыдущий элемент>, <очередной элемент>, <следующий элемент>)
# Для первого элемента предыдущим считается значение  None , для последнего элемента
# следующим считается так же значение  None .


def around(a):
    iterable = list(a)
    iterable.insert(len(iterable), None)
    iterable.insert(0, None)
    return (  (iterable[i], iterable[i+1], iterable[i+2]) for i in range(0, len(iterable) - 2) )



# TEST_1:
numbers = [1, 2, 3, 4, 5]

print(*around(numbers))
print()
# TEST_2:
iterator = iter('hey')

print(*around(iterator))
print()
# TEST_3:
iterator = around(iter('beegeek'))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print()
# TEST_4:
data = map(abs, range(-100, 100))

print(*around(data))
print()
# TEST_5:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*around(data))
print()
# TEST_6:
data = map(str.upper, 'y')

iterator = around(data)

print(next(iterator))
print()
# TEST_7:
data = map(str.upper, 'yt')

print(*around(data))
print()
# TEST_8:
data = map(str.upper, 'ytu')

print(*around(data))
print()
# TEST_9:
data = ['bee', 'geek', 'stepik', 'python']

print(*around(data))
print()
# TEST_10:
print(list(around([])))