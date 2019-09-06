#!/usr/bin/env python3

def goodVsEvil(good, evil):
    goods = good.split(' ')
    evils = evil.split(' ')
    
    for i in range(len(goods)):
        goods[i] = int(goods[i])
        if goods[i] < 0:
            goods[i] = 0
    for i in range(len(evils)):
        evils[i] = int(evils[i])
        if evils[i] < 0:
            evils[i] = 0
    
    if sum(goods) < sum(evils):
        return 'Battle Result: Evil eradicates all trace of Good'
    elif sum(goods) > sum(evils):
        return 'Battle Result: Good triumphs over Evil'
    else:
        return 'Battle Result: No victor on this battle field'
  
print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 -5'))


    # goods1 = [1, 2, 3, 3, 4, 10]
    # evils1 = [1, 2, 2, 2, 3, 5, 10]

    # for i in range(len(goods)):
    #     for y in range(len(goods1)):
    #         if goods[i] > goods1[y] and i == y:
    #             goods[i] = goods1[y]
    

    # for i in range(len(evils)):
    #     for y in range(len(evils1)):
    #         if evils[i] > evils1[y] and i == y:
    #             evils[i] = evils1[y]
    # print(evils) 
    # print(goods)
