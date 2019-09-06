#!/usr/bin/env python3

num = int(input('Задайте число: '))
mon = int(input('Задайте месяц: '))
ye = int(input('Задайте Год: '))

def date(number, month, year):
    if number == num and month == mon and year == ye:
        return True
    else:
        return False

while date(int(input('Угадайте число: ')), int(input('Угадайте месяц: ')), int(input('Угадайте Год: '))) == False:
    print(False)
else:
    print(True) 



