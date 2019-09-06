#!/usr/bin/env node

function rowSumOddNumbers(n) {
    let array = [];
    let y = 0
    let x = 0
    for(let k=0; k<n*2; k+=2){
        y = k;
    }

    for(let k=0; k<(n-1)*2; k+=2){
        x = k;
    }

    for(let i=n+y; array.length<n; i+=2){
        array.push(i);
    }
    // return array
    // return array.reduce((s,v) => s+=v);
}

console.log(rowSumOddNumbers(5))