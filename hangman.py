from random import *

tries = 6


word_list = ['гвоздь', 'шуруп', 'тряпка', 'веревка', 'перфоратор',
             'одеколон', 'мышь', 'тетрадь', 'сумка', 'стол', 
             'пенал', 'молоток', 'арбуз', 'суп', 'резак']

def get_word():
    word = choice(word_list).upper()
    return word

wo = get_word()
word = wo.lower()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    
    return stages[tries]

def vvod_zash():
    flag = False
    while flag == False:
        print("Введите букву, слог или слово, если ты считаешь что она есть в загадке")
        vvod = input()
        c = 0
        for i in range(0, len(vvod)):
            if vvod[i].lower() in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
                c = c + 1
        if c == len(vvod):
            flag = True
            return vvod
        else:
            print("Я не могу разобрать символы, которые вы ввели. Попробуй еще раз.")
            flag = False
            

def play(word):
    
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    
    print('Давайте играть в угадайку слов!')
    print("На данный момент тут никого нет)")
    print(display_hangman(tries))
    
    print(word)
    print(word_completion)
    
    
    #otv = vvod_zash()
    #otvet = otv.lower()
    tek_stroka = ''
    ind = 0
    
    flag = False
    
    while flag == False:
        
        otv = vvod_zash()
        otvet = otv.lower()
        
        #когда на вход 1 буква
        if len(otvet) == 1:
            
            for i in range(0, len(word)):

                if otvet == word[i]: #and tek_stroka[i] == '_':
                    tek_stroka = tek_stroka + otvet
                    
                elif otvet != word[i]:
                    tek_stroka = tek_stroka + '_'
                    
            if tek_stroka != '_' * len(word):
                flag = True
                print(tek_stroka)        
            elif tek_stroka == '_' * len(word):
                print("К сожалению, данной буквы нет в загаданном слове, попробуй снова")
                tries = tries - 1
                print(display_hangman(tries))
                vvod_zash()          
                    
        #когда на вход поступило слово  
            
        if otvet in word and len(otvet) > 1:
            ind = word.find(otvet)
            tek_stroka = "_" * ind + otvet + "_" * (len(word) - len(otvet) - ind)
            #print(tek_stroka)
        elif tek_stroka == '_' * len(word):
            print("К сожалению, данной буквы нет в загаданном слове, попробуй снова")
            tries = tries - 1
            print(display_hangman(tries))
            vvod_zash()                 
                
        
        
        if tries == 0:
            print('Вы проиграли, исчерпав количество попыток(6)')
            print(display_hangman(tries))
            
        elif '_' in tek_stroka:
            print(tek_stroka)
            print(display_hangman(tries))
            flag = False
            
        elif '_' not in tek_stroka: 
            flag = True
            print('Поздравляем, вы отгадали слово')
            print(display_hangman(tries))
                
        #return word

play(word)

