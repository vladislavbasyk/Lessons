#!/usr/bin/env python3

def sqInRect(lng, wdth):
    side=[]
    if lng < wdth:
        side.append(lng)
    elif lng > wdth:
        side.append(wdth) 
    else:
        return None

    while lng != wdth:
        if lng < wdth:
            wdth -= lng
            if wdth < lng:
                side.append(wdth)
            else:
                side.append(lng)   
        else:
            lng -= wdth
            if wdth < lng:
                side.append(wdth)
            else:
                side.append(lng) 
    return side
            
print(sqInRect(5,3))