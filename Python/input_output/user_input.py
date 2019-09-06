#!/usr/bin/env python3

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    tetx = string.replace(' ', '')
    
    return text == reverse(text)


something = input('Введите текст:')

if (is_palindrome(something)):
    print('Да это палиндром')
else:
    print('Нет это не палиндром')


def is_palindrome(string):
    string = string.lower().replace(' ', '')
    rev_string = ''.join(reversed(string))

    return string == rev_string

my_str = 'b ba'
print('YES' if is_palindrome(my_str) else 'NO')