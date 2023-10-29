# Реализуйте функцию  is_iterator() , которая принимает один аргумент:
# obj  — произвольный объект
# Функция должна возвращать  true , если объект  obj  является итератором, или  false  в
# противном случае. 

def is_iterator(obj):
    
    return hasattr(obj, '__next__')  


# TEST_1:
print(is_iterator([1, 2, 3, 4, 5]))
print()
# TEST_2:
beegeek = map(str.upper, 'beegeek')

print(is_iterator(beegeek))
print()
# TEST_3:
beegeek = filter(None, [0, 0, 1, 1, 0, 1])

print(is_iterator(beegeek))
print()
# TEST_4:
beegeek = zip([1, 2, 3], [3, 4, 5])

print(is_iterator(beegeek))
print()
# TEST_5:
beegeek = enumerate('beegeek', start=1)

print(is_iterator(beegeek))
print()
# TEST_6:
beegeek = 'beegeek'

print(is_iterator(beegeek))
print()
# TEST_7:
beegeek = 199999111199991919191

print(is_iterator(beegeek))
print()
# TEST_8:
beegeek = iter('199999111199991919191')

print(is_iterator(beegeek))