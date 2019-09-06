#!/usr/bin/env python3
import json

while True:
    try:
        with open('addressbook.json', 'r') as file:
            addrbook = json.load(file)
    except json.decoder.JSONDecodeError:
        addrbook = {}
    except FileNotFoundError:
        addrbook = {}

    print('\nДля просмотра всех контактов нажмите 0')
    print('Для добавления нового контакта нажмите 1')
    print('Для удаления контакта нажмите 2')
    print('Для поиска контакта нажмите 3')
    print('Для замены контакта нажмите 4')
    print('Для закрытия программы нажмите любую цифру больше 4')

    def add_contact():
        new_name = input('\nВведите имя нового контакта: ') 
        new_number = input ('Введите номер нового контакта: ')
        if len(new_number) < 14:
            addrbook[new_name] = new_number
            print('Контакт', new_name, 'с номером:', new_number, 'добавлен.')
        else:
            print('Максимальное количество цифр в номере не должно превышать 13-ти')

    def del_contact():
        try:
            del_name = input('\nВведите имя контакта, которого вы хотите удалить: ')
            del addrbook[del_name]
        except KeyError:
            print('\nНет такого контакта!')
    
    def search_contact():
        try:
            search_name = input('\nВведите имя контакта: ')
            print('Номер контакта:', addrbook[search_name])
        except KeyError:
            print('\nНет такого контакта!')

    def replace_contact():
        try:
            replace_name = input('\nВведите имя контакта, который вы хотите заменить: ')
            del addrbook[replace_name]
            replace_new_name = input('\nВведите имя нового контакта: ') 
            replace_new_number = input ('Введите номер нового контакта: ')
            if len(replace_new_number) < 14:
                addrbook[replace_new_name] = replace_new_number
            else:
                print('Максимальное количество цифр в номере не должно превышать 13-ти')    
        except KeyError:
            print('\nНет такого контакта!')
        
    try:
        option = int(input('\nВведите цифру: '))
        if option == 0:
            for name, number in addrbook.items():
                print('Контакт', name, 'с номером', number)
        elif option == 1:
            add_contact()
        elif option == 2:
            del_contact()
        elif option == 3:
            search_contact()
        elif option == 4:
            replace_contact()
        elif option > 4:
            print('Программа завершена!!!')
            break
    except ValueError:
        print('Введите именно цифру!')
         
    with open('addressbook.json', 'w') as f: 
        f.write(json.dumps(addrbook, indent=4))


