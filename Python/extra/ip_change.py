#!/usr/bin/env python3
import re

type_ip = input('Выберите тип ip адреса S-статический, D-динамический: ')
interface = input('Введите имя интерфейса: ')

def read_file():
    a = ''
    with open('interfaces', 'r') as f:
        for line in f:
           a = a + re.sub(interface, interface, line)
        with open('interfaces', 'w') as f:
            f.write(a)
                
def dhcp():
    ip_dhcp = '\nauto ' + interface + '\niface ' + interface + ' inet dhcp' + '\n'
    with open('interfaces', 'a') as f:
        read_file()
        f.write(ip_dhcp)
        
def static():
    ip = input('Добавьте ip адрес:')
    mask = input('Добавьте маску подсети:')
    gateway = input('Добавьте основной шлюз подсети если его нету нажмите Enter :')
    ip_static = '\nauto ' + interface + '\niface ' + interface + ' inet static' +'\naddress ' + ip + '\nnetmask ' + mask + '\n'
    with open('interfaces', 'a') as f:     
        f.write(ip_static)
   
if type_ip == 'D' or type_ip == 'd':
    dhcp()
elif type_ip == 'S' or type_ip == 's':
    static()





