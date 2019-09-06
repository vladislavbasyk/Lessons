#!/usr/bin/env python3
import re

regular = '''
Шла Саша по шоссе и сосала сушку
сушка упала и написала
'''
a=input('a')
b=input('b')
try:
    with open('regular.txt', 'w') as f:
        f.write(regular)
except FileNotFoundError:
    regular

result = re.sub(a, b, regular)
print(result)
