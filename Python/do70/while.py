#!/usr/bin/env python3
number=15
running=True
while running == True:
	guess=int(input('Введите целое число: '))	

	if guess == number:
		print('Поздравляю, вы угадали. ')
		running=False
	elif guess<number:
		print('Нет, число больше вашего')
	else:
		print('Нет, число меньше вашего')
else:
	print('цикл окончен.')
print('Завершение')

