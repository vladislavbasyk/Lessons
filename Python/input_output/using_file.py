#!/usr/bin/env python3

poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
используй Python!
'''

f = open('poem.txt', 'w') #откр для записи (writting)
f.write(poem) #записываем текст в файл
f.close() # закрываем файл

f = open('poem.txt') #открываем для чтения(по умолчнию r'eading)

while True:
    line = f.readline()
    if len(line) == 0: #нулевая длина обозначает конец файла (EOF)
        break
    print(line, end='')

f.close

