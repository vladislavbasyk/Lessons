#!/usr/bin/env python3

deposit = int(input('Сделайте ваш вклад: '))
year = int(input('На какое количество лет? '))

def bank(deposit, year):
    
    total = deposit * 1.1 * year
    return total 

print('Ваша итоговая сумма выйдет = ', bank(deposit, year))
print('wedawed')