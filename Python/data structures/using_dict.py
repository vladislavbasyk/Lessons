#!/usr/bin/env python3

ab = {  'Swaroop' : 'swaroop@swaroopch.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer' : 'spammer@hotmail.com'
    }
print('Адрес Swaroopa:', ab['Swaroop'])

del ab['Spammer']

print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])
    