#!/usr/bin/env python3
#Filename: func_return.py

def maximum(x, y):
    if x>y:
        return x
    elif x==y:
        return 'Числа равны.'
    else:
        return y

x=int(input ('x = '))
y=int(input ('y = '))

print(maximum(x,y))

        
        