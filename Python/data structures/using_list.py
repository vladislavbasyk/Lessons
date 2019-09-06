#!/usr/bin/env python3
#Список покупок:
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print('Я должен сделать ', len(shoplist), 'покупок.')

print('Покупки: ', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список таков: ', shoplist)

print('Отсортирую список')
shoplist.sort()
print('Отсортированный список:', shoplist)

print('Первое, что мне надо купитьб это-', shoplist[0])
olditem=shoplist[0]
del shoplist [0]
print('Я купил:', olditem)
print('Теперь мой список покупок:', shoplist)
