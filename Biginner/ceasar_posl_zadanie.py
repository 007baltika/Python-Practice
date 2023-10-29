
en = 'abcdefghijklmnopqrstuvwxyz'
en_high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input()
zash_st = ''
tekst = ''
s = ''
massslov = text.split()
massslov_chist = []
#очистка списка от всех символов

for k in range(0, len(massslov)):
    for l in range(0, len(massslov[k])):
        if massslov[k][l] in en or massslov[k][l] in en_high:
            s = s + massslov[k][l]
    massslov_chist.append(s)
    s = ''   
         
#шифровка по длине слова работает 
        
for j in range(0, len(massslov)):
    for i in range(0, len(massslov[j])):        
        if massslov[j][i] in en:
        
            zash_st = zash_st + en[(en.index(massslov[j][i]) + len(massslov_chist[j])) % len(en)]
        
        elif massslov[j][i] in en_high:
        
            zash_st = zash_st + en_high[(en_high.index(massslov[j][i]) + len(massslov_chist[j])) % len(en_high)] 
          
        else: zash_st = zash_st + massslov[j][i]
    
    tekst = tekst + zash_st + ' '
    zash_st = '' 
    
          

#print(massslov)
print(tekst)            
#print(zash_st) 