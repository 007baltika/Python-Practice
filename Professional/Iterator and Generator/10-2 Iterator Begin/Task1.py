# Реализуйте функцию  filterfalse()  с использованием функции  filter() , которая принимает
# два аргумента:
# predicate  — функция-предикат; если имеет значение  None , то работает аналогично
# функции  bool()
# iterable  — итерируемый объект
# Функция должна работать противоположно функции  filter() , то есть возвращать итератор,
# элементами которого являются элементы итерируемого объекта  iterable , для которых
# функция  predicate  вернула значение  false .

def filterfalse(predicate, iterable):
    otvet = []
    if predicate != None:
        for num in iterable:
            if predicate(num) == False:
                otvet.append(num)   
        return otvet     
    else: 
        for num in iterable:
            if bool(num) == False:
                otvet.append(num)   
        return otvet    
    
# TEST_1:
objects = [0, 1, True, False, 17, []]

print(*filterfalse(None, objects))
print()
# TEST_2:
numbers = (1, 2, 3, 4, 5)

print(*filterfalse(lambda x: x % 2 == 0, numbers))
print()
# TEST_3:
numbers = [1, 2, 3, 4, 5]

print(*filterfalse(lambda x: x >= 3, numbers))
print()
# TEST_4:
numbers = range(1, 150, 8)
result = filterfalse(lambda num: num % 8 == 3, numbers)
print(*result)
print()
# TEST_5:
import string
letters = string.ascii_letters
result = filterfalse(lambda char: ord(char) > 75, letters)
print(*result, sep=',')
print()
# TEST_6:
objects = [0, 0, 0, True, False, 1788, [], {}, set(), (), '', 0.0, None, 'stepik', dict()]

print(*filterfalse(None, objects))