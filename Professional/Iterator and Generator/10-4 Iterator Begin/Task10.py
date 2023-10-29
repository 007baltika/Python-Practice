# Узнать как работать с Unicode

# Реализуйте класс  Alphabet , порождающий итераторы, конструктор которого принимает один
# аргумент:
# language  — код языка:  ru  — русский,  en  — английский
# Итератор класса  Alphabet()  должен циклично генерировать последовательность букв:
# русского алфавита, если  language  имеет значение  ru
# английского алфавита, если  language  имеет значение  en

# class Alphabet:
    
#     def __init__(self, language):
#         self.language = language
#         self.ru_start = 0x0430
#         self.en_start = 0x0061
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.language == 'ru':
#             if self.ru_start <= 0x0460:
#                 self.ru_start += 1
#                 # ascii_word =  chr(self.ru_start - 1)
#                 # code_unicode = ascii_word.encode()
#                 # return code_unicode.decode("ascii")
#                 return self.ru_start.decode('unicode_escape')
#         elif self.language == 'en':
#             if self.en_start <= 122:
#                 self.en_start += 1
#                 return chr(self.en_start - 1)        
#         else: raise StopIteration
        
# ru_alpha = Alphabet('ru')
# print(next(ru_alpha))
# print(next(ru_alpha))
# print(next(ru_alpha))            
            
            