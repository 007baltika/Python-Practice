# Реализуйте класс  RandomNumbers , порождающий итераторы, конструктор которого принимает три аргумента

# Итератор класса  RandomNumbers  должен генерировать последовательность из  n  случайных
# чисел от  left  до  right  включительно, а затем возбуждать исключение  StopIteration .


import random

class RandomNumbers:
    
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.start = 0
        self.mass = list(range(self.left, self.right + 1))
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        def random_num():
            return random.choice(self.mass)
        
        if self.start < self.n:
            self.start += 1
            return random_num()
        else: raise StopIteration
        


# TEST_1:
iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print()
# TEST_2:
iterator = RandomNumbers(1, 10, 2)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print()
# TEST_3:
iterator = RandomNumbers(-100, -92, 99)

print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print()
# TEST_4:
iterator = RandomNumbers(5, 5, 98)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print()
# TEST_5:
iterator = RandomNumbers(1000, 1001, 108)

print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print()
# TEST_6:
iterator = RandomNumbers(-100, 99, 100)

print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print()
# TEST_7:
iterator = RandomNumbers(-1000, -900, 1)

print(next(iterator) in range(-1000, -899))

try:
    next(iterator)
except StopIteration:
    print('Error')
print()
# TEST_8:
iterator = RandomNumbers(-1000, -900, 4)

print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))

try:
    next(iterator)
except StopIteration:
    print('Error')
        
           