# Реализуйте класс  Fibonacci , порождающий итераторы, конструктор которого не принимает
# никаких аргументов.
# Итератор класса  Fibonacci  должен генерировать бесконечную последовательность
# чисел Фибоначчи, начиная с 1.
# Примечание 1. Последовательность Фибоначчи – последовательность натуральных чисел, где
# каждое последующее число является суммой двух предыдущих:
# 1, 1, 2, 3, 5, 8, 13, 21, 34

class Fibonacci:
    
    def __init__(self):
        self.start = 0
        self.n = 0
        self.a = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start == 0:
            self.start += 1
            return 1
        self.last_start = self.start
        self.a = self.start + self.n
        self.start = self.a
        self.n = self.last_start
        return self.a
    
    
    
# TEST_1:
fibonacci = Fibonacci()

print(next(fibonacci))
print()
# TEST_2:
fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print()
# TEST_3:
fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print()
# TEST_4:
fibonacci = Fibonacci()

for _ in range(50):
    print(next(fibonacci))
print()
# TEST_5:
fibonacci = Fibonacci()

for _ in range(100):
    next(fibonacci)

print(next(fibonacci))
print()
# TEST_6:
fibonacci = Fibonacci()

for _ in range(76):
    next(fibonacci)

next(fibonacci)
next(fibonacci)
next(fibonacci)
next(fibonacci)

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))