#!/usr/bin/env python3


def is_year_leap(x):
    if x % 4 == 0:
        return True
    else:
        return False

while is_year_leap(int(input('Введите год: '))) == False:
    print(False)
else:
    print(True)


