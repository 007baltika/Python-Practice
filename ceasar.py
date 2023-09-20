
print("Привет, ты хочешь зашифровать или дешифровать текст? З/Д" )
shorde = input()
print("На каком языке будет текст? ru/en")
lan = input()
print("Подскажи шаг свдига")
sdvig = int(input())
print("Введи текст для обработки")
text = input()

ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ru_high = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
en = 'abcdefghijklmnopqrstuvwxyz'
en_high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

zash_st = ''


if shorde.lower() == "з":
    
    if lan.lower() == 'ru':
        
        for i in range(0, len(text)):
            
            if text[i] in ru:
                zash_st = zash_st + ru[(ru.find(text[i]) + sdvig) % len(ru)]
                #zash_st = zash_st + text[(i + sdvig) % len(ru)]
            elif text[i] in ru_high:
                zash_st = zash_st + ru_high[(ru_high.find(text[i]) + sdvig) % len(ru)]    
            else: zash_st = zash_st + text[i]  
            
    elif lan.lower() == 'en':
        
        for j in range(0, len(text)):
            
            if text[j] in en:
                zash_st = zash_st + en[(en.find(text[j]) + sdvig) % len(en)]
                #zash_st = zash_st + text[(j + sdvig) % len(en)]
            elif text[j] in en_high:
                zash_st = zash_st + en_high[(en_high.find(text[j]) + sdvig) % len(en_high)]   
            else: zash_st = zash_st + text[j]
            
elif shorde.lower() == "д":
    
    if lan.lower() == 'ru':
        
        for k in range(0, len(text)):
            if text[k] in ru:
                zash_st = zash_st + ru[(ru.find(text[k]) - sdvig) % len(ru)]
                #zash_st = zash_st + text[(k - sdvig) % len(ru)]
            elif text[k] in ru_high:
                zash_st = zash_st + ru_high[(ru_high.find(text[k]) - sdvig) % len(ru_high)]    
            else: zash_st = zash_st + text[k]
            
    elif lan.lower() == 'en':
        
        for l in range(0, len(text)):
            if text[l] in en:
                zash_st = zash_st + en[(en.find(text[l]) - sdvig) % len(en)]
                #zash_st = zash_st + text[(l - sdvig) % len(en)]
            elif text[l] in en_high:
                zash_st = zash_st + en_high[(en_high.find(text[l]) - sdvig) % len(en_high)]    
            else: zash_st = zash_st + text[l] 
            
print(zash_st) 

                 