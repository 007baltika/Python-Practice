# Реализуйте генераторную функцию  years_days() , которая принимает один аргумент:
# year  — натуральное число
# Функция должна возвращать генератор, порождающий последовательность всех дат
# (тип  date ) в году  year .


from datetime import timedelta, date

def years_days(years):
    start_date = date(years, 1, 1)
    i = 0
    while start_date.year < years + 1:
        start_date = start_date + timedelta(days=1)
        yield start_date - timedelta(days=1)
        



# TEST_1:
dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))
print()
# TEST_2:
dates = years_days(2077)

print(*dates)
print()
# TEST_3:
dates = years_days(2000)

print(*dates)
print()
# TEST_4:
dates = years_days(1900)

print(*dates)
