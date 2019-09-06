#!/usr/bin/env node
let str = 'var_testfefe_textsd';
let arr = str.split('_');
for(i=1; i<arr.length; i++){
    arr[i] = arr[i].slice(0,1).toUpperCase() + arr[i].slice(1)
}
arr = arr.join('')
console.log(arr)

