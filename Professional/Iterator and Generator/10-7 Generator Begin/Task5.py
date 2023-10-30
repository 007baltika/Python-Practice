# Реализуйте генераторную функцию, которая принимает один аргумент:
# iterable  — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность элементов

def unique(iterable):
    mass_uniq = []
    for num in iterable:
        if num not in mass_uniq:
            mass_uniq.append(num)
    yield from mass_uniq     
    
       

# TEST_1:
numbers = [1, 2, 2, 3, 4, 5, 5, 5]

print(*unique(numbers))
print()
# TEST_2:
iterator = iter('111222333')
uniques = unique(iterator)

print(next(uniques))
print(next(uniques))
print(next(uniques))
print()
# TEST_3:
data = map(abs, range(-100, 100))

print(*unique(data))
print()
# TEST_4:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*unique(data))
print()
# TEST_5:
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

print(*unique(data))
print()
# TEST_6:
data = map(str.lower, 'STEPIK')

print(*unique(data))
print()
# TEST_7:
data = map(str.lower, 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')

print(*unique(data))
print()
# TEST_8:
data = ['bee', 'geek', 'stepik', 'python']

print(*unique(data))
print()
# TEST_9:
print(list(unique([])))