# Функция должна возвращать генератор, порождающий  max_names  имён из списка  names ,
# игнорируя имена, которые
# начинаются на  ignore_char (в любом регистре), содержат хотя бы одну цифру
# Если  max_names  больше количества имен в списке  names , то генератор должен породить все
# возможные имена из данного списка. 

def filter_names(names, ignore_char, max_names):
    i = 0
    for name in names: 
        if i < max_names:
            if name[0].lower() != ignore_char.lower() and name.isalpha():
                i+=1
                yield name  
               



# TEST_1:
data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))
print()
# TEST_2:
data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))
print()
# TEST_3:
data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']

print(*filter_names(data, 'A', 100))
print()
# TEST_4:
data = ['Arthur', 'Anri', 'Arina', 'Albert', 'Angel', 'Ariel']

print(*filter_names(data, 'F', 6))
print()
# TEST_5:
data = ['Arthur', 'Anri', 'Arina', 'Albert', 'Angel', 'Ariel']

print(*filter_names(data, 'A', 22))
print()
# TEST_6:
data = ['Arthur', 'Anri', 'Arina', 'Albert', 'Angel', 'Ariel']

print(next(filter_names(data, 'R', 1)))
print()
# TEST_7:
data = ['Barry']

print(*filter_names(data, 'B', 1))
print()
# TEST_8:
data = ['Dima1', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', '4Ruslan']

print(*filter_names(data, 'a', 20))
print()
# TEST_9:
data = ['Dima', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', '4Ruslan']

print(*filter_names(data, 'A', 1))
print()
# TEST_10:
data = ['1Dima', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', 'Ruslan']

print(*filter_names(data, 'A', 1))
print()
# TEST_11:
data = []

print(list(filter_names(data, 'B', 1)))
print()
# TEST_12:
data = ['Dima', 'Timur', 'Arthur', 'Anri', 'Arina', 'German', 'Ruslan', 'Roma5', 'Jenya', 'Anna']

print(*filter_names(data, 'A', 8))