# Реализуйте генераторную функцию, которая принимает один аргумент:
# iterable  — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность кортежей, каждый
# из которых содержит очередной элемент итерируемого объекта  iterable , а также следующий
# за ним элемент:
# (<очередной элемент>, <следующий элемент>)
# Для последнего элемента следующим считается значение  None .


def pairwise(a):
    iterable = list(a)
    iterable.insert(len(iterable), None)
    return (  (iterable[i], iterable[i+1]) for i in range(0, len(iterable) - 1) )




# TEST_1:
numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))
print()
# TEST_2:
iterator = iter('stepik')

print(*pairwise(iterator))
print()
# TEST_3:
print(list(pairwise([])))
print()
# TEST_4:
data = map(abs, range(-100, 100))

print(*pairwise(data))
print()
# TEST_5:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*pairwise(data))
print()
# TEST_6:
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

print(*pairwise(data))
print()
# TEST_7:
iterator = pairwise('A')

print(next(iterator))
print()
# TEST_8:
data = ['bee', 'geek', 'stepik', 'python']

print(*pairwise(data))