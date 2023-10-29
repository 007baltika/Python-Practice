# Функция должна возвращать генератор, порождающий элементы
# последовательности  sequence  в обратном порядке, а затем возбуждающий
# исключение  StopIteration .

def reverse(sequence):
    for num in sequence[::-1]:
        yield num
       
       
        
# TEST_1:
print(*reverse([1, 2, 3, 4, 5]))
print()
# TEST_2:
generator = reverse('beegeek')

print(type(generator))
print(*generator)
print()
# TEST_3:
generator = reverse('stepik')

print(type(generator))

try:
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')
print()
# TEST_4:
generator = reverse(list(range(123, 5453, 3)))

print(type(generator))
print(*generator)
print()
# TEST_5:
generator = reverse(tuple('HFJDHFjdhfjhfdJSHFJDHF'))

print(type(generator))

try:
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')
print()
# TEST_6:
generator = reverse(list('HFJDHFjd23423i942313223hfjhfdJSHFJD656754964HF'))

print(type(generator))
print(*generator)
print()
# TEST_7:
generator = reverse([1])

print(type(generator))
print(*generator)
print()
# TEST_8:
print(list(reverse([])))     