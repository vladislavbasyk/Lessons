#!/usr/bin/env python3

def crc(msg, polynom, null_bits):
    
    if null_bits == 4:
        null_bits = '0000'
        polynom = '10011'
    elif null_bits == 8:
        null_bits = '00000000'
        polynom = '100000111'
    elif null_bits == 16:
        null_bits = '0000000000000000'
        polynom = '10001000000100001'
    elif null_bits == 32:
        null_bits = '00000000000000000000000000000000'
        polynom = '100000100110000010001110110110111'

    msg = msg + null_bits
    print('Полином:', polynom)
    print('Выровненное сообщение:', msg)

    msg = list(msg)
    polynom = list(polynom)

# Loop over every message bit (minus the appended code)
    for i in range(len(msg)-len(null_bits)):
        # If that messsage bit is 1, perform modulo 2 multiplication
        if msg[i] == '1':
            for j in range(len(polynom)):
                # Perform modulo 2 multiplication on each index of the divisor
                msg[i+j] = str((int(msg[i+j])+int(polynom[j]))%2)

    # Output the last error-checking code portion of the message generated
    return ''.join(msg[-len(null_bits):])

try:
    polynom = ' '
    null_bits= int(input('Введите старшую степень полинома:'))
    msg = input('Введите cообщение в двоичном виде:')

    null_bits = crc(msg, polynom, null_bits)
    print('Контрольная сумма:', null_bits)
except ValueError:
    print('Символы не могут быть степенью полинома')
except TypeError:
    print('Такая стеень полинома в программе не предуматрена, введите 4, 8, 16 или 32')




    

        
