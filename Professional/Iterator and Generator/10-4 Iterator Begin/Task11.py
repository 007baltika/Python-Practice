# Реализуйте класс  Xrange , порождающий итераторы, конструктор которого принимает три
# аргумента в следующем порядке:
# start  — целое или вещественное число
# end  — целое или вещественное число
# step  — целое или вещественное число, по умолчанию имеет значение 1
# Итератор класса  Xrange  должен генерировать последовательность членов арифметической
# прогрессии от  start  до  end , включая  start  и не включая  end , с шагом  step , а затем
# возбуждать исключение  StopIteration .

class Xrange:
    
    def __init__(self, start, end, step = 1):
        self.start = start
        self.end = end
        self.step = step
        self.a = self.end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.start == self.end: raise StopIteration
        else: 
            a = self.start
            self.start += self.step
            return a 
        
        
# TEST_1:
evens = Xrange(0, 10, 2)

print(*evens)
print()
# TEST_2:
xrange = Xrange(0, 3, 0.5)

print(*xrange, sep='; ')
print()
# TEST_3:
xrange = Xrange(10, 1, -1)

print(*xrange)
print()
# TEST_4:
xrange = Xrange(5, 10)

print(*xrange)
print()
# TEST_5:
xrange = Xrange(-20, 12, 4)

print(*xrange)
print()
# TEST_6:
xrange = Xrange(-50, -10, 5)

print(*xrange)
print()
# TEST_7:
xrange = Xrange(-50, -49)

print(*xrange)
print()
# TEST_8:
xrange = Xrange(-50, -48, 2)

print(*xrange)
print()
# TEST_9:
xrange = Xrange(100, 101)

print(*xrange)
print()
# TEST_10:
xrange = Xrange(0, 1)

print(*xrange)
print()
# TEST_11:
xrange = Xrange(-1, 0)

print(*xrange)
print()
# TEST_12:
xrange = Xrange(200, 202, 2)

print(*xrange)
print()
# TEST_13:
xrange = Xrange(24, 89, 13)

print(list(xrange))
print()
# TEST_14:
xrange = Xrange(100, 10, -1)

print(list(xrange))
print()
