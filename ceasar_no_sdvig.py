
print("Введи текст для обработки")
text = input()

en = 'abcdefghijklmnopqrstuvwxyz'
en_high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

zash_st = ''
for j in range(0, 26):
    for i in range(0, len(text)):
        if text[i] in en:
            zash_st = zash_st + en[(en.find(text[i]) - j) % len(en)]
            #zash_st = zash_st + text[(i + sdvig) % len(ru)]
        elif text[i] in en_high:
            zash_st = zash_st + en_high[(en_high.find(text[i]) - j) % len(en_high)]    
        else: zash_st = zash_st + text[i]
    print(zash_st, end = '\n')
    zash_st = ''