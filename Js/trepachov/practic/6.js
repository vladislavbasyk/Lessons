#!/usr/bin/env node

let arr = [];
let n = 10;
let x = 0;
let p = '';
for(let i = 0; i < n; i++){
    p += '1';
    p = parseInt(p); 
    arr.push(p);
}
for(let i = 1; i <=n; i++){
    arr[i-1] *= i 
}

console.log(arr)