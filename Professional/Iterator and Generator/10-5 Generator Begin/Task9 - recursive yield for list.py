# Реализуйте генераторную функцию  flatten() , которая принимает один аргумент:
# nested_list  — список, элементами которого являются целые числа или списки,
# элементами которых, в свою очередь, также являются либо целые числа, либо списки;
# вложенность может быть произвольной

# Функция должна возвращать генератор, порождающий все числа, содержащиеся
# в  nested_list , включая все числа из всех вложенных списков, а затем возбуждает
# исключение  StopIteration .

def flatten(nested_list):
    for num in nested_list:
        if isinstance(num, list):
            yield from flatten(num)
        else: yield num    

#Рекурсивно высвобождаем элементы в бесконечном количестве списков



# TEST_1:
generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)
print()
# TEST_2:
generator = flatten([1, 2, 3, 4, 5, 6, 7])

print(*generator)
print()
# TEST_3:
generator = flatten([3, [4], [5, [6, [7, 8]]]])

print(*generator)
print()
# TEST_4:
generator = flatten([10, 20, 30, 40, 50])

print(*generator)
print()
# TEST_5:
generator = flatten([[1], [2], [3], [4, 5], 6, 7])

print(*generator)
print()
# TEST_6:
generator = flatten([[1], [2], [3], [4], [5], [6], [7]])

print(*generator)
print()
# TEST_7:
generator = flatten([[123], 23, 43, 65, 754, 3, 1, 2])

print(*generator)
print()
# TEST_8:
generator = flatten([3123, 424, 5343, 11, 1, 23, 43, 65, 754, 3, 1, [2]])

print(*generator)
print()
# TEST_9:
generator = flatten([[3, 2, 5345, 65, 7, 777, 0, 43, 65, 754, 3, 1, 2]])

print(*generator)
print()
# TEST_10:
generator = flatten([34534, [656, [7867, [[234, [123, 34534, [758, 978]]]], 667, [4546]]], [2324, [234234, [7656]], 9879, 55]])

print(*generator)
print()
# TEST_11:
generator = flatten([12, [13, [53, [632, [6, [2342341, [98, [3123], [2432], [4324]]]]]]]])

print(*generator)