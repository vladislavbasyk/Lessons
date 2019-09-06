#!/usr/bin/env python3
import re

def zeros(n):
    a = []
    mult = 1
    b = []
    c = []
    for i in range(1, n+1):
        a.append(i)
    
    for i in a:
        mult *= i
    
    mult = str(mult)
    res = re.findall(r'.', mult)
    for i in reversed(res):
        b.append(i)
    for i in range(len(b)):
        if b[i] == '0':
            c.append(b[i])
        else:
            break
    return len(c)
    

print(zeros(20))