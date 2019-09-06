#!/usr/bin/env node

var land = {
    ru : ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
    en : ['Mn', 'Ts', 'Wd', 'Th', 'Fr', 'St', 'Sn']
}
day = 6
console.log(land['ru'][day], land['en'][day])
