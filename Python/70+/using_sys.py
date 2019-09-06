#!/usr/bin/env python3
import sys
import os

print('Аргументы командной строки: ')
for i in sys.argv:
    print(i)
print('\n\nПеременная содержит PYTHONPATH', sys.path, '\n')
print(os.getcwd())