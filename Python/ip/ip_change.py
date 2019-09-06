#!/usr/bin/env python3
import re

type_ip = input('Выберите тип ip адреса S-статический, D-динамический: ')

interface_dhcp = input('Введите имя интерфейса для динамического адреса, если он не нужен нажмите Enter: ')
ip_dhcp = '\nauto ' + interface_dhcp + '\niface ' + interface_dhcp + ' inet dhcp' + '\n'

interface_static = input('Введите имя интерфейса для статического адреса, если он не нужен нажмите Enter: ')
ip = input('Добавьте ip адрес:')
mask = input('Добавьте маску подсети:')
gateway = input('Добавьте основной шлюз подсети если его нету нажмите Enter :')
ip_static = '\nauto ' + interface_static + '\niface ' + interface_static + ' inet static' +'\naddress ' + ip + '\nnetmask ' + mask + '\n'

def delate():
    a = ''
    with open('interfaces', 'r') as f:
        for line in f:
           a = a + re.sub(interface, interface, line)
        with open('interfaces', 'w') as f:
            f.write(a)

def dhcp():    
    with open('interfaces', 'a') as f:
        f.write(ip_dhcp)
        a = ''
        with open('interfaces', 'r') as f:
            for line in f:
                if interface_dhcp == interface_static:
                    a = a + re.sub(ip_static, ip_dhcp, line)
            with open('interfaces', 'w') as f:
                f.write(a)

def static():
    with open('interfaces', 'a') as f:     
        f.write(ip_static)
        a = ''
        with open('interfaces', 'r') as f:
            for line in f:
                if interface_dhcp == interface_static:
                    a = a + re.sub(ip_dhcp, ip_static, line)
            with open('interfaces', 'w') as f:
                f.write(a) 

if type_ip == 'D' or type_ip == 'd':
    dhcp()
elif type_ip == 'S' or type_ip == 's':
    static()