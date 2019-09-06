#!/usr/bin/env python3

import time

try:
    f = open('poem.txt')
    while True: # обычный сп-б читать файлы
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2) #время ожидания
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла.')
finally:
    f.close()
    print('(Очистка: Закрытие файла)')
