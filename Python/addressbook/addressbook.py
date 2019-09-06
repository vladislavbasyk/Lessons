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

    print('\nНажмите 0 для просмотра всех контактов')
    print('Нажмите 1 для добавления нового контакта')
    print('Нажмите 2 для поиска контакта')
    print('Нажмите 3 для удаления контакта')
    print('Нажмите 4 для замены контакта')
    print('Для закрытия программы нажмите любую цифру больше 4')

    def looking_contact():
        for look_id in addrbook:
                for name in addrbook[look_id]:
                    print(name, addrbook[look_id][name])  

    def add_contact():
        new_name = input('\nВведите имя нового контакта: ') 
        new_number = input ('Введите номер нового контакта: ')
        if len(new_number) < 14:
            new_id = len(addrbook)
            addrbook[new_id+1] = {new_name : new_number}
            print('Контакт', new_name, 'с номером:', new_number, 'добавлен.')
        else:
            print('Максимальное количество цифр в номере не должно превышать 13-ти')

    def search_contact():
        try:
            search_name = input('\nВведите имя контакта: ')
            for search_id in addrbook:
                for name in addrbook[search_id]:
                    if name == search_name:
                        print('ID=', search_id, name, addrbook[search_id][name])
        except KeyError:
            print('\nНет такого контакта!')

    def del_contact():
        search_contact()
        del_id = input('\nВведите ID контакта, которого вы хотите удалить: ')
        del addrbook[del_id]

    def replace_contact():
        del_contact()
        add_contact()
    
    def chisla_contact():
        for c_id in addrbook:
            print(range(int(addrbook[c_id])))    
     
    try:
        option = int(input('\nВведите цифру: '))
        if option == 0:
            looking_contact()         
        elif option == 1:
            add_contact()
        elif option == 2:
            search_contact()
        elif option == 3:
            del_contact()
        elif option == 4:
            replace_contact()
        elif option == 5:
            chisla_contact()
        elif option > 5:
            print('Программа завершена!!!')
            break
            
    except ValueError:
        print('Введите именно цифру!')
    except KeyboardInterrupt:
        print(' Программа завершена!!!')
        break
         
    with open('addressbook.json', 'w') as f: 
        f.write(json.dumps(addrbook, indent=4))