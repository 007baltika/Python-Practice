# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.

# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.

# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True, 
# если пароль является действительным паролем BEEGEEK банка и False - в противном случае.

# объявление функции
def is_valid_password(password):
    st = ''
    mass = []
    for i in range(0, len(password)):
        if password[i] in '0123456789':
            st = st + password[i]
        elif password[i] == ':': 
            mass.append(st)
            st = ''
            continue
    mass.append(st) 
    #print(int(mass[1]))
    if len(mass) == 3:
        if mass[0] == mass[0][::-1]:
            c = 0
            for i in range(1, int(mass[1])):
                if int(mass[1]) % i == 0: 
                    c = c +1
            if c < 3 and mass[1] != 1: 
                if int(mass[2]) % 2 == 0:
                    return True
                else: return False
            else: return False    
        else: return False            
    else: return False        
# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))