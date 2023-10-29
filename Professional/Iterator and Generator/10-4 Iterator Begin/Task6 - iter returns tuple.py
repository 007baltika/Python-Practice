# Реализуйте класс  DictItemsIterator , порождающий итераторы, конструктор которого
# принимает один аргумент:
# data  — словарь
# Итератор класса  DictItemsIterator  должен генерировать последовательность кортежей,
# представляющих собой пары ключ-значение словаря  data , а затем
# возбуждать исключение  StopIteration .

class DictItemsIterator:
    
    def __init__(self, data):
        self.data = data
        self.list = list(self.data)
        self.start = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < len(self.list):
            stroka = (self.list[self.start], self.data.get(self.list[self.start]))
            self.start += 1
            return stroka
        else: raise StopIteration
    
    
    
# TEST_1:
pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)
print()
# TEST_2:
data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

pairs = DictItemsIterator(data)

print(*pairs)
print()
# TEST_3:
data = {'Arthur': 100, 'Timur': 100, 'Dima': 100,
        'Anri': 101, 'Roma': 99, 'German': 98}

pairs = DictItemsIterator(data)

print(list(pairs))
print()
# TEST_4:
data = {'Arthur': [100, 5], 'Timur': [100, 6], 'Dima': [100, 7, 8], 
        'Anri': [100, 101], 'Roma': [99]}

pairs = DictItemsIterator(data)

print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')
print()
# TEST_5:
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

pairs = DictItemsIterator(data)

print(tuple(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')