#!/usr/bin/env python3
def printMax(x,y):
    '''Выводит максимальное из двух чисел.
        Оба значения должны быть целыми числами.'''
    x=int(x)
    y=int(y)

    if x>y:
        print(x, 'Наибольшее ')
    else:
        print(y, 'наибольшее')

printMax(3, 5)
print(printMax.__doc__)
