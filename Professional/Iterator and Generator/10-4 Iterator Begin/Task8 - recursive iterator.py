# Реализуйте класс  Cycle , порождающий итераторы, конструктор которого принимает один
# аргумент:
# iterable  — итерируемый объект
# Итератор класса  Cycle  должен циклично генерировать последовательность элементов
# итерируемого объекта  iterable .

class Cycle:
    
    def __init__(self, iterable):
        self.safe = iterable
        self.object = iterable
        self.len = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.len < len(self.object):
            self.len += 1
            return self.object[self.len - 1]
        else:
            self.len = 0
            return self.__next__()
            # или
            # self.len = 0
            # self.len += 1
            # return self.object[self.len - 1]
            
            
# TEST_1:
cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print()
# TEST_2:
cycle = Cycle([1])

print(next(cycle) + next(cycle) + next(cycle))
print()
# TEST_3:
cycle = Cycle(range(100_000_000))

print(next(cycle))
print(next(cycle))
print()
# TEST_4:
cycle = Cycle(range(10_000_000))

for _ in range(1000):
    next(cycle)

print(next(cycle))
print()
# TEST_5:
cycle = Cycle('beegeek')

for _ in range(1000):
    next(cycle)

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print()
# TEST_6:
cycle = Cycle((0, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 0, 9, 8, 87, 5666666))

for _ in range(2000):
    next(cycle)

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print()
# TEST_7:
cycle = Cycle((0,))

for _ in range(2000):
    next(cycle)

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print()
# TEST_8:
cycle = Cycle('B')

for _ in range(500):
    next(cycle)

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print()
# TEST_9:
cycle = Cycle('AJFHKJSDHFWIEFJIOFKDKSVNCVNJVDJSFNdfkdsjfiwej943257438j2j123')

for _ in range(666):
    next(cycle)

print(next(cycle))
print()
# TEST_10:
cycle = Cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for _ in range(100):
    print(next(cycle))       