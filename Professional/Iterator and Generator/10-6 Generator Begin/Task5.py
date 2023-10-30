

def interleave(*args):
    for element in args:
        yield from element
    
    
    
# TEST_1:
print(*interleave('bee', '123'))
print()
# TEST_2:
numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]

print(*interleave(numbers, squares, qubes))
print()
# TEST_3:
numbers1 = tuple(range(10))
numbers2 = list(range(10, 20))
numbers3 = tuple(range(20, 30))
numbers4 = tuple(range(30, 40))

print(*interleave(numbers1, numbers2, numbers3, numbers4))
print()
# TEST_4:
string = str(range(10, 50))

print(*interleave(string))
print()
# TEST_5:
numbers1 = tuple(range(38, 99, 7))
numbers2 = tuple(range(65, 114, 6))
string1 = 'BEEGEEKbe'
string2 = 'STEPIKste'
numbers3 = list(range(1, 170, 19))
numbers4 = list(range(2, 175, 20))

print(*interleave(numbers3, string2, numbers4, string1, numbers2, numbers1))    