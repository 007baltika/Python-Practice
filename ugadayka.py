from random import *


def is_valid(chislo):
    flag = False
    while flag == False:
        if chislo.isdigit() == True and x < int(chislo) < y + 1:
            flag = True
            global a 
            a = int(chislo)
            return a
        else: 
            flag =  False
            print('А может быть все-таки введем целое число в диапазоне от', x, 'до', y, "?")
            chislo = input()   
    ugadayka()


def eshe_raz():
    print("Желаете сыграть еще раз? Да/Нет")
    otvet = input()
    while True:
        if otvet.lower() == "да":
            main()
        elif otvet.lower() == 'нет': 
            break    

def ugadayka():
    count = 1
    while True:
        global chislo2
        if a < sluchchislo:
            count = count + 1 
            print ('Ваше число меньше загаданного, попробуйте еще разок')
            chislo2 = input()
            is_valid(chislo2)
        if a > sluchchislo:
            count = count + 1 
            print ("Ваше число больше загаданного, попробуйте еще разок")
            chislo2 = input()
            is_valid(chislo2)   
        if a == sluchchislo:
            print ('Вы угадали, поздравляем!')
            print("Вы угадали с", count, 'попытки!')
            eshe_raz()
            


def main():
    print('Добро пожаловать в числовую угадайку')
    print("Для начала укажите диапазон цифр, среди которых вы будете угадывать число")
    global x
    global y
    x, y = int(input()), int(input())
    global sluchchislo
    sluchchislo = randint(x, y + 1)
    print("Теперь загадайте число")
    chislo = input()
    is_valid(chislo)
    print(ugadayka())

main()    