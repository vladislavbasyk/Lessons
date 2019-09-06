#!/usr/bin/env python3

def crc():
    plm = 0
    nulb = int(input('Введите старшую степень полинома:'))
    if nulb == 4:
        nulb = 16
        plm = 19
    elif nulb == 8:
        nulb = 256
        plm = 263
    elif nulb == 16:
        nulb = 65536
        plm = 69665
    elif nulb == 32:
        nulb = 4294967296
        plm = 4374732215
    else:
        print('Неверная степень полинома')

    msg = int(input('Введите cообщение: '))
    print('Сообщение в двоичном виде:', bin(msg))
    
    #выравниваем сообщение
    msg = msg * nulb


    print('Выровненное сообщение в двоичном виде:', bin(msg))
    print('Полином в двоичном виде:', bin(plm))
    msg = msg^plm
    print(msg) 



crc()


n = bin(8)
n = int(n, 2)
print(n)
