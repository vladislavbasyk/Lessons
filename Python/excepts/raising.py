#!/usr/bin/env python3

class ShotInputException(Exception):
    # пользовательский класс исключения
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Введите что-нибудь:')
    if len(text) < 3:
        raise ShotInputException(len(text), 3)
        # Здесь может происходить обычная работа
except EOFError:
    print('Зачем вы сделали EOF?')
except ShotInputException as ex:
    print('ShotInputException: Длина введенной\
строки', ex.length, 'ожидалось минимум', ex.atleast)
else:
    print('Не было исключений')