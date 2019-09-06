#!/usr/bin/env python3

slovo='qwe'
run=True
while run:
	vvod=input('Введите слово: ')
	
	if vvod == slovo:
		print ('Правильно')
		run = False
	elif vvod != slovo:
		print ('Не верно')
else:
	print('Конец')
