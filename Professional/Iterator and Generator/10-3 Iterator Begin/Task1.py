# Функция должна возвращать  true , если объект  obj  является итерируемым объектом,
# или  false  в противном случае.

def is_iterable(obj):
    
    return hasattr(obj, '__iter__')  


# TEST_1:
print(is_iterable(18731))
print()
# TEST_2:
print(is_iterable('18731'))
print()
# TEST_3:
objects = [(1, 13), 7.0004, [1, 2, 3]]

for obj in objects:
    print(is_iterable(obj))
print()
# TEST_4:
for element in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:
    print(element, 'iterable: ', is_iterable(element))