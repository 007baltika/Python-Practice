

def cubes_of_odds(iterable):
    return (pow(num, 3) for num in iterable if num  % 2 != 0)


# TEST_1:
print(*cubes_of_odds([1, 2, 3, 4, 5]))
print()
# TEST_2:
evens = [2, 4, 6, 8, 10]

print(list(cubes_of_odds(evens)))
print()
# TEST_3:
data = tuple(range(432, 3845, 17))

print(*cubes_of_odds(data))
print()
# TEST_4:
data = map(abs, range(-200, 400, 11))

print(*cubes_of_odds(data))
print()
# TEST_5:
data = filter(lambda x: x % 13, range(101, 982))

print(*cubes_of_odds(data))