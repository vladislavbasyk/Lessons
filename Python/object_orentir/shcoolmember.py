#!/usr/bin/env python3

class SchoolMember:
    #Представляет люого человека в школе
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def tell(self):
        #Вывести информациию
        print('Имя:', '"', self.name, '"', 'Возраст:', '"', self.age, '"')

class Teacher(SchoolMember):
    #Представляет преподователя
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Добавлен учитель:', self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата =', self.salary)

class Student(SchoolMember):
    #Класс студентов
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Добавлен студент:', '"', self.name, '"')
    
    def tell(self):
        SchoolMember.tell(self)
        print('Оценки:', self.marks)
        

t = Teacher('Курилович', 45, 800)
t1 = Teacher('Боря', 65, 1600)
s = Student('Пузыня', 21, 5)

members = [t, s]
for member in members:
    member.tell()