# Итератор класса  PowerOf  должен генерировать бесконечную последовательность целых
# неотрицательных степеней числа  number  в порядке возрастания, начиная с нулевой степени.

class PowerOf:
    
    def __init__(self, number):
        self.number = number
        self.stepen = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.stepen += 1
        return pow(self.number, self.stepen-1)
    
# TEST_1:
power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print()
# TEST_2:
power_of_two = PowerOf(1)

for _ in range(55):
    print(next(power_of_two))
print()
# TEST_3:
power_of_two = PowerOf(3)

for _ in range(10):
    print(next(power_of_two))
print()
# TEST_4:
power_of_two = PowerOf(11)

for _ in range(11):
    print(next(power_of_two))
print()
# TEST_5:
power_of_two = PowerOf(100)

for _ in range(20):
    next(power_of_two)

print(next(power_of_two))           
        