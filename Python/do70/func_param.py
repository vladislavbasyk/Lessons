#!/usr/bin/env python3
def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a==b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')

printMax(3,4) #прямая передача значений

x=int(input('x: '))
y=int(input('y: '))

printMax(x,y) #косенная передача зна-ний