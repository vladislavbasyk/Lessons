#!/usr/bin/env python3

class Product:
    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year

    def tell(self):
       print(name, price, year)

class Lamp(Product):
    def __init__(self, name, price, year, kind, capacity):
        Product.__init__(self, name, price, year)
        self.kind = kind
        self.capacity = capacity
    
    def tell(self):
        Product.tell(self)
        print ('Вид светильника:', kind, 'Мощность:',capacity)



name = input ('Введите имя товара:')
price = int(input('Введите цену товара:'))
year = int(input('Ведите год выпуска товара:'))
kind = input ('Введите вид светильника:')
capacity = int(input('Введите мощность светилька:'))


lamp = Lamp(name, price, year, kind, capacity)

products = [lamp]
for product in products:
    product.tell()

