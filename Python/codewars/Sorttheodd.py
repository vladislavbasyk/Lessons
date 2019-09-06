#!/usr/bin/env python3

def sort_array(source_array):
    a = []
    for i in range(len(source_array)):
        if source_array[i]%2 != 0:
            a.append(source_array[i])
    a.sort(reverse=True)

    for i in range(len(source_array)):
        if source_array[i]%2 != 0: 
            source_array[i] = a.pop()

    return source_array

print(sort_array([3, 2, 1, 4, 6, 9, 7, 8]))

