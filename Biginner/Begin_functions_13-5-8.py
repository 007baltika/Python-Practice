# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из символов ( и ) и возвращает значение True 
# если поступившая на вход строка является правильной скобочной последовательностью и False в противном случае.

# Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ), 
# где каждой открывающей скобке найдется парная закрывающая скобка (при этом каждая открывающая скобка должна быть левее соответствующей ей закрывающей скобки).

# объявление функции
def is_correct_bracket(text):
    c1 = 0
    c2 = 0
    stmass = []
    for j in range(0, len(text)):
        stmass.append(text[j])

        
    b = stmass.count(")")    
    c = stmass.count("(")
    #print(c)
    if b == c:
        for k in range(0, c):
            if stmass.index("(") < stmass.index(")"):
                iotkr = stmass.index("(")
                izakr = stmass.index(")")
                stmass[iotkr] = 0
                stmass[izakr] = 0
                #print(1)
        if stmass == [0] * len(stmass):
            return True
        else: return False
    else: return False        
# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))