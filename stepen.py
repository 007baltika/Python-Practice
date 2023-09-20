
print("Введите основание")
osnov = int(input())

chislo_v_syst = 0

ch_88 = 513
ch_32 = 32
ch_22 = 22
ch_16 = 16
ch_17 = 17

ost_88 = 0
ost_32 = 0
ost_22 = 0
ost_16 = 0
ost_17 = 0

s_88 = ''
s_32 = ''
s_22 = ''
s_16 = ''
s_17 = ''



for i in range(0, 1):    
    while ch_88 != 0:
        ost_88 = ch_88 % osnov 
        ch_88 = ch_88 // osnov
        
        s_88 = s_88 + str(ost_88) 

    num88 = int(s_88[-1:-len(s_88)-1:-1])
    print(num88) 


    while ch_32 != 0:
        ost_32 = ch_32 % osnov 
        ch_32 = ch_32 // osnov
        
        s_32 = s_32 + str(ost_32) 

    num32 = int(s_32[-1:-len(s_32)-1:-1])
    print(num32) 


    while ch_22 != 0:
        ost_22 = ch_22 % osnov 
        ch_22 = ch_22 // osnov
        
        s_22 = s_22 + str(ost_22) 

    num22 = int(s_22[-1:-len(s_22)-1:-1]) 
    print(num22) 


    while ch_16 != 0:
        ost_16 = ch_16 % osnov 
        ch_16 = ch_16 // osnov
        
        s_16 = s_16 + str(ost_16) 

    num16 = int(s_16[-1:-len(s_16)-1:-1]) 
    print(num16) 


    while ch_17 != 0:
        ost_17 = ch_17 % osnov 
        ch_17 = ch_17 // osnov
        
        s_17 = s_17 + str(ost_17) 

    num17 = int(s_17[-1:-len(s_17)-1:-1])
    print(num17) 
 
    if num88 == num17 + num16 + num22 + num32:
        print(osnov)
        break


             