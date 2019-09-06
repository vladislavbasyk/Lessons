#!/usr/bin/env python3

a = [':)', ';(', ';}', ':-D']
def count_smileys(arr):
    count = 0
    smile = [':)', ':~)', ':-)', ':D', ':~D', ':-D', ';)', ';~)', ';-)', ';D', ';~D', ';-D']
    for i in range(len(smile)):
        for y in range(len(arr)):
            if smile[i] == arr[y]:
                count += 1 
    return count


print(count_smileys(a))