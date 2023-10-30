# Реализуйте генераторную функцию, которая принимает один аргумент:
# iterable  — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность кортежей, каждый
# из которых содержит очередной элемент итерируемого объекта  iterable , а также
# предшествующий ему элемент:
# (<очередной элемент>, <предыдущий элемент>)
# Для первого элемента предыдущим считается значение  None .



def with_previous(iterable):
    with_none = list(iterable)
    with_none.insert(0, None)
    return (  (with_none[i], with_none[i-1]) for i in range(1, len(with_none)) )




# TEST_1:
numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))
print()
# TEST_2:
iterator = iter('stepik')

print(*with_previous(iterator))
print()
# TEST_3:
print(*with_previous(map(abs, range(-100, 100))))
print()
# TEST_4:
print(*with_previous(map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')))
print()
# TEST_5:
print(*with_previous('JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'))
print()
# TEST_6:
print(*with_previous('A'))
print()
# TEST_7:
print(*with_previous('AB'))
print()
# TEST_8:
gen = with_previous(['bee', 'geek', 'stepik', 'python'])

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print()
# TEST_9:
print(list(with_previous('')))