#!/usr/bin/env python3
import random


good = {'Hobbits' : 1, 'Men' : 2, 'Elves' : 3, 'Dwarves' : 3, 'Eagles' : 4, 'Wizards' : 10}
evil = {'Orcs' : 1, 'Men' : 2, 'Wargs' : 2, 'Goblins' : 2, 'UrukHai' : 3, 'Trolls' : 5, 'Wizards' : 10}

def ran(count):
    return random.randint(0, count)
    
goods = [ran(good['Hobbits']), ran(good['Men']), ran(good['Elves']), ran(good['Dwarves']), ran(good['Eagles']), ran(good['Wizards'])]
evils = [ran(evil['Orcs']), ran(evil['Men']), ran(evil['Wargs']), ran(evil['Goblins']), ran(evil['UrukHai']), ran(evil['Trolls']), ran(evil['Wizards'])]
print(goods)
print(evils)

def goodVsEvil():
    if sum(goods) > sum(evils):
        return 'Battle Result: Good triumphs over Evil'
    elif sum(goods) < sum(evils):
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'

print(goodVsEvil())

