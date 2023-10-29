

class Repeater:
    
    def __init__(self, obj):
        self.obj = obj
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.obj    
    
# TEST_1:
bee = Repeater('bee')

print(next(bee))
print()
# TEST_2:
geek = Repeater('geek')

print(next(geek))
print(next(geek))
print(next(geek))
print()
# TEST_3:
repeater = Repeater(1234)

for _ in range(100):
    print(next(repeater))
print()
# TEST_4:
repeater = Repeater((1, 2, 3, 4))

for _ in range(55):
    print(next(repeater))
print()
# TEST_5:
repeater = Repeater(['bee', 'geek'])

for _ in range(22):
    print(next(repeater))  