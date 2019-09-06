#!/usr/bin/env python3

def divisors(integer):
    res=[]
    for i in range(2, integer):
        if integer%i == 0:
            res.append(i)           
    if res == []:
        return str(integer) + ' is prime'
    else:    
        return res
    
print(divisors(13))


