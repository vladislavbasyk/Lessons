#!/usr/bin/env python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHi(self):
        print('Привет меня зовут ', self.name, self.age)

p = Person('Swaroop', 20)
p.sayHi()
