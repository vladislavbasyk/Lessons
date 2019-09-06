#!/usr/bin/env node

let str = 'qwe.html';
let a = str.substr(-5);
function check(){
    if(str.substr(-5) == '.html'){
    return true;
    } else {
        return false;
    }
}

console.log(check())