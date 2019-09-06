#!/usr/bin/env node
let id = process.argv  

function vyvod(a){
    b = 10
    sum = a+b
    if(a>b | a==b){
        return sum;
    }
    else{
        for(i=1; i<=10; i++){
            console.log(i);
        }
    }
  
}

let browser = 'Chrome';

if (browser == 'IE'){
    console.log('0, да у вас IE')
} else if (browser == 'Chrome' || browser == 'Firefox' || browser == 'Safari' || browser == 'Opera'){
    console.log('Да, и эти браузеры мы поддерживаем'.toUpperCase())
} else{
    console.log('Мы надеемся, что и в вашем браузере все ок!'.length)
}
console.log(console.count('qwe  qw'.length))
let c = '5.9'
c = parseFloat(c)

console.log(c)

let mas = [1, 4, 9, 8]
for( let i=0; i<mas.length; i++){
    console.log(i)
}

