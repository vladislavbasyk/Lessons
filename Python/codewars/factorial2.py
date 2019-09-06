#!/usr/bin/env python3
import math
import re

def zeros(n):
    a = []
    mult = 1
    for i in range(1, n+1):
        a.append(i)
    
    for i in a:
        mult *= i
    
    mult = str(mult)
    
    res = re.findall('0+$', mult)
    res = ''.join(res)
    return len(res)

print(zeros(100))

# mult=math.factorial(n)
