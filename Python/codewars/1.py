#!/usr/bin/env python3
import re
def solution(string):
    result = re.findall(r'.', string)
    result.reverse()
    result = ''.join(result)
    return result 

print(solution('Ну что ты братишка притих'))