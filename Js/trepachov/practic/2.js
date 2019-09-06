#!/usr/bin/env node

function pow(num){
    let days = {
        1 : 'понедельник',
        2 : 'вторник',
        3 : 'среда',
        4 : 'четверг',
        5 : 'пятница',
        6 : 'суббота',
        7 : 'воскресенье'
    }
    return days[num];
}
console.log(pow(7))