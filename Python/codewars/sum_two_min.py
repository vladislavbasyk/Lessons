#!/usr/bin/env python3

num_list = [25, 42, 1.2, 12, 18]

def sum_two_smallest_numbers(numbers):
  
    b=[]
    for i in numbers:
        if type(i)==str or i<0 or (not(i%1))==False:
            continue
        b.append(i)
    b.sort()
    return b[0] + b[1]

print(sum_two_smallest_numbers(num_list))

    


