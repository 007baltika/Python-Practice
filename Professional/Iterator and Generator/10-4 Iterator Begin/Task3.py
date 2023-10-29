# Реализуйте класс  Square , порождающий итераторы, конструктор которого принимает один
# аргумент:
# n  — натуральное число,
# Итератор класса  Square  должен генерировать последовательность из  n  чисел, каждое из
# которых является квадратом очередного натурального числа, а затем
# возбуждать исключение  StopIteration .

class Square:
    
    def __init__(self, n):
        self.n = n
        self.start = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.n:
            self.start += 1
            return pow(self.start-1, 2)
        else: raise StopIteration 
        
        
# TEST_1:
squares = Square(2)

print(next(squares))
print(next(squares))
print()
# TEST_2:
squares = Square(10)

print(list(squares))
print()
# TEST_3:
squares = Square(1)

print(list(squares))
print()
# TEST_4:
squares = Square(5)

next(squares)
next(squares)
next(squares)
next(squares)
next(squares)

try:
    next(squares)
except StopIteration:
    print('Error')
print()
# TEST_5:
squares = Square(9)

print(*squares)
print()
# TEST_6:
squares = Square(2)

try:
    print(next(squares))
    print(next(squares))
    print(next(squares))
except:
    print('Error')  