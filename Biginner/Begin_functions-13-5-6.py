# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True 
# если указанный текст является палиндромом и False в противном случае.

# объявление функции
def is_palindrome(text):
    st = ''
    strev = ''
    for i in range(0, len(text)):
        if text[i] not in ".,!?- ":
            st = st + text[i]
    strev = st[-1:-len(st)-1:-1]
    #print(strev)
    #print(st)
    if st.lower() == strev.lower(): return True
    else: return False
    
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))