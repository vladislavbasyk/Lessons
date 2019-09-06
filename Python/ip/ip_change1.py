#!/usr/bin/env python3
import re
import os

lb = """#interfaces(5) file used by ifup(8) and ifdown(8)
auto lo
iface lo inet loopback
"""
def clean():
    with open('interfaces', 'w') as f:
        f.write(lb)
clean()

print('\nИмена итерфейсов вашего компьютера:')
os.system('sudo ls /sys/class/net/')

while True:  
    type_ip = input('\nДля выхода из программы нажмите <q>  \nВыберите тип ip адреса S-статический, D-динамический: ')

    # def read_file():
    #     a = ''
    #     with open('interfaces', 'r') as f:
    #         for line in f:
    #         a = a + re.sub(interface, interface, line)
    #         with open('interfaces', 'w') as f:
    #             f.write(a)
                    
    def dhcp():
        interface = input('Введите имя интерфейса: ')
        ip_dhcp = '\nauto ' + interface + '\niface ' + interface + ' inet dhcp' + '\n'
        with open('interfaces', 'a') as f:
            f.write(ip_dhcp)
            
    def static():
        interface = input('Введите имя интерфейса: ')
        ip = input('Добавьте ip адрес: ')
        mask = input('Добавьте маску подсети: ')
        gateway = input('Добавьте основной шлюз подсети: ')
        if len(gateway) > 7:
            ip_static = '\nauto ' + interface + '\niface ' + interface + ' inet static' +'\naddress ' + ip + '\nnetmask ' + mask + '\ngateway ' + gateway + '\n'
        else:
            ip_static = '\nauto ' + interface + '\niface ' + interface + ' inet static' +'\naddress ' + ip + '\nnetmask ' + mask + '\n'  
        with open('interfaces', 'a') as f:     
            f.write(ip_static)
   
    if type_ip == 'D' or type_ip == 'd':
        dhcp()
    elif type_ip == 'S' or type_ip == 's':
        static()
    elif type_ip == 'q':
        break

os.system('sudo cp interfaces /etc/network')
os.system('sudo service networking restart')
clean()