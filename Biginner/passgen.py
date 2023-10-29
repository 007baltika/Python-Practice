from random import *

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

print("Введите количество паролей для генерации")
count = int(input())

print("Введите длину одного пароля")
length = int(input())

print("Включать ли цифры? Да/Нет")
cifri = input()

print("Включать ли прописные буквы? Да/Нет")
propis = input()

print("Включать ли строчные буквы? Да/Нет")
strochn = input()

print("Включать ли символы? Да/Нет")
symb = input()

print("Исключать ли неоднозначные символы il1Lo0O ? Да/Нет")
iskl = input()

for i in range(0, count):
    for j in range(0, length):
        
        if cifri.lower() == "да":
            sluchchislo = str(randrange(10))
            if iskl.lower() == 'да':
                if sluchchislo not in 'il1Lo0O':
                    chars = chars + sluchchislo
            else: chars = chars + sluchchislo
                    
        if len(chars) == length: 
            print(chars)
            chars = ''
            break    
            
        if propis.lower() == "да":
            sluch_upper = choice(uppercase_letters)
            if iskl.lower() == 'да':
                if sluch_upper not in 'il1Lo0O':
                    chars = chars + sluch_upper
            else: chars = chars + sluch_upper
            
        if len(chars) == length: 
            print(chars)
            chars = ''
            break       
            
        if strochn.lower() == "да":
            sluch_lower = choice(lowercase_letters)
            if iskl.lower() == 'да':
                if sluch_lower not in 'il1Lo0O':
                    chars = chars + sluch_lower
            else: chars = chars + sluch_lower
            
        if len(chars) == length: 
            print(chars)
            chars = ''
            break    
            
        if symb.lower() == "да":
            sluch_symb = choice(punctuation)
            if iskl.lower() == 'да':
                if sluch_symb not in 'il1Lo0O':
                    chars = chars + sluch_symb
            else: chars = chars + sluch_symb
          
        if len(chars) == length: 
            print(chars)
            chars = ''
            break                   