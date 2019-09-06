#!/usr/bin/env python3

import re 

def count_smileys(arr):
    if (re.findall('[:;][-~]?[D\)]', ' '.join(arr))):
        return True
    return False
    
    
    #  and re.search('^[-]$|^[~]$', arr_str) and re.search('^[)]$|^[D]$', arr_str):
    # result = re.findall(b, arr_str)
    # return result

print(count_smileys([':-)', '}', ':-D']))