#!/usr/bin/env python3

def season(x):
    if x < 3 or x == 12:
        print('winter')
    elif x < 6 and x > 2:
        print('spring')
    elif x < 9 and x > 5:
        print('summer')
    elif x < 12 and x > 8:
        print('autmn')
        
    
k = int(input('Число:\n'))   
while (k>12):
    print('Число должно быть от 1 до 12')
    k = int(input('Число:\n'))
else:
    season(k)
    



        
        
        

