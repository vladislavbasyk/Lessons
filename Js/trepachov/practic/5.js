#!/usr/bin/env node
let str = '';
for (var i = 1; i <= 9; i++) {
    str += i ;   
}
str =str.split('').join('-');
console.log(str)