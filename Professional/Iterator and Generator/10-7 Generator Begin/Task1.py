# Назовем диапазоном запись двух натуральных чисел через дефис  a-b , где  a  — левая граница
# диапазона,  b  — правая граница диапазона, причем  a <= b . Диапазон содержит в себе все
# числа от  a  до  b  включительно. Например, диапазон  1-4  содержит числа 1, 2, 3 и 4.
# Реализуйте генераторную функцию  parse_ranges() , которая принимает один аргумент:
# ranges  — строка, в которой через запятую указаны диапазоны чисел
# Функция должна возвращать генератор, порождающий последовательность чисел,
# содержащихся в диапазонах  ranges .

def parse_ranges(ranges):
    ranges_list = ranges.split(',')
    for range_elem in ranges_list:
        # print(range)
        left, right = (int(num) for num in range_elem.split('-'))
        # print(left, right)
        yield from range(left, right+1)
        
        
        
# TEST_1:
print(*parse_ranges('1-2,4-4,8-10'))
print()
# TEST_2:
print(*parse_ranges('1-10,2-10'))
print()
# TEST_3:
print(*parse_ranges('7-32'))
print()
# TEST_4:
print(*parse_ranges('8-8,8-8,8-8,8-8,8-8'))
print()
# TEST_5:
print(*parse_ranges('10-10,11-11,12-12'))
print()
# TEST_6:
print(*parse_ranges('10-15,1-4,4-5,5-5,1-10,1-15'))
print()
# TEST_7:
numbers = parse_ranges('1-3')

print(next(numbers))
print(next(numbers))
print(next(numbers))
print()
# TEST_8:
numbers = parse_ranges('1-3,4-5,10-32,32-32,32-40,1-2,2-32,10-11,67-199')

print(*numbers)