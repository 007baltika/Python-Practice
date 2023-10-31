

import itertools as it

def alnum_sequence():
    mass_num = list(num for num in range(1, 27))
    mass_word = list(chr(word_num) for word_num in range(65, 91))
    # for i, j in zip(mass_num, mass_word, it.count(1)):
    #     yield (i, j)
    
    cycle_mass = it.cycle(zip(mass_num, mass_word))
    for element in cycle_mass:
        yield from element





# TEST_1:
alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))
print()
# TEST_2:
alnum = alnum_sequence()

print(*(next(alnum) for _ in range(100)))
print()
# TEST_3:
alnum = alnum_sequence()

print(next(alnum))
print(next(alnum))
print(next(alnum))
print(next(alnum))
print()
# TEST_4:
alnum = alnum_sequence()

for _ in range(10_000):
    next(alnum)

print(next(alnum))
print(next(alnum))
print(next(alnum))
print(next(alnum))
print()
# TEST_5:
alnum = alnum_sequence()

for _ in range(100_000):
    next(alnum)

print(next(alnum))
print(next(alnum))
print(next(alnum))
print(next(alnum))