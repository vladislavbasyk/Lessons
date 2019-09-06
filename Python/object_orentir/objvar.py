#!/usr/bin/env python3

class Robot:
    #Предоставляет робота с именем
    #Переменная класса, содержащая количество роботов
    population = 0

    def __init__(self, name):
        #инициализация данных
        self.name = name
        print('(Иницализация) ',self.name)

        if Robot.population == 0:
            print(self.name, ' Я первый робот)')
        

        #При создании этой личности, робот добавляется
        #к переменной 'population'
        Robot.population += 1

    def __del__(self):
        #Я умираю
        print(self.name, ' уничтожается!')

        Robot.population -= 1

        if Robot.population == 0:
            print(self.name, ' Я был последним ...')
        else:
            print('Осталось ', Robot.population, 'работающих роботов')

    def sayHi(self):
        #Приветствие робота.
        print('Приветуля! Мой черный господин меня называет', self.name)

    def howMany():
        #Выводит численность роботов
        print('У нас ', Robot.population, ' роботов')

    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3P0')
droid2.sayHi()
droid2.howMany()

droid3 = Robot('Слава Конопелько')
droid3.sayHi()
droid3.howMany()

Robot.howMany()

print("\nЗдесь роботы могут проделать какую-то работу.\n")

print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2

Robot.howMany()
