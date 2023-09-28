# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True, 
# если пароль является надежным и False - в противном случае.

# Пароль является надежным если:

# его длина не менее 
# 8
# 8 символов; 
# он содержит как минимум одну заглавную букву (верхний регистр); 
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

# объявление функции
def is_password_good(password):
    c = 0
    if len(password) >= 8: c = c + 1 
    for i in range(0, len(password)):
        if password[i] in "QWERTYUIOPASDFGHJKLZXCVBNM": 
            c = c + 1
            break
    for j in range(0, len(password)):
        if password[j] in "qwertyuioplkjhgfdsazxcvbnm": 
            c = c + 1
            break
    for k in range(0, len(password)):
        if password[k] in "1234567890": 
            c = c + 1
            break
                  
    if c == 4: return True
    else: return False        
# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))