#!/usr/bin/env python3

try:
    text = input('Введите что-нибудь --> ')
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
except text == '1':
    print('Вы вывели 1')
else:
    print('Вы ввели:', text)