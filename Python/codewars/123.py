#!/usr/bin/env python3
from random import random
N = 10
a = []
for i in range(N):
    a.append(int(random()*100))
    print("%3d" % a[i], end='')
print()
 
if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0
    
for i in range(2,N):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i
        
print("№%3d:%3d" % (min1+1, a[min1]))
print("№%3d:%3d" % (min2+1, a[min2]))

b=a[min1]+a[min2]
print(b)