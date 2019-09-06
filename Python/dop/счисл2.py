#!/usr/bin/env python3

x = int(input('Введите 10-ное число: '))
print(x)
y = int(input('Введите 10-ное число: '))
print(y)

k=x^y
n=bin(k)

print('k=', n)

mes = int(input('Введите 10-ное число: '))

bitnull = 16
lin_mes=mes * bitnull
lin_mes_bi= bin(lin_mes)
print(lin_mes_bi)


k=0b10000
n=0b10011
x=n^k
print(x)


