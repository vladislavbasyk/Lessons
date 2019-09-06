#!/usr/bin/env node

let balance = 1000;
let number = numRandom(0, 36);
let table ={
    1 : {1 : 'red'}, 2 : {2 : 'black'}, 3 : {3 : 'red'}, 4 : {1 : 'black'}, 5 : {2 : 'red'}, 6 : {3 : 'black'}, 7 : {1 : 'red'}, 8 : {2 : 'black'}, 9 : {3 : 'red'},
    10 : {1 : 'black'}, 11 : {2 : 'red'}, 12 : {3 : 'black'}, 13 : {1 : 'red'}, 14 : {2 : 'black'}, 15 : {3 : 'red'}, 16 : {1 : 'black'}, 17 : {2 : 'red'}, 18 : {3 : 'black'},
    19 : {1 : 'red'}, 20 : {2 : 'black'}, 21 : {3 : 'red'}, 22 : {1 : 'black'}, 23 : {2 : 'red'}, 24 : {3 : 'red'}, 25 : {1 : 'black'}, 26 : {2 : 'red'}, 27 : {3 : 'black'},
    28 : {1 : 'red'}, 29 : {2 : 'black'}, 30 : {3 : 'red'}, 31 : {1 : 'black'}, 32 : {2 : 'red'}, 33 : {3 : 'black'}, 34 : {1 : 'red'}, 35 : {2 : 'black'}, 36 : {3 : 'red'}, 0 : {0 : 'zero'}
};
let string = table[number];


console.log(number, table[number]);

function numRandom(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function straightBet(num, bet){
    if(num == number){
        balance = balance + (bet * 35);    
    } else{
        balance -= bet;
    }   
}

function red_blackBet(color, bet){
    let coller = '';
    for(let key in string){
        coller = [string[key]];
    }
    if(color == coller){
        balance = balance + (bet * 2); 
    } else{
        balance -= bet;
    }
}

function halfBet(half, bet){
    if(half == 1 && number > 0 && number < 19 || half == 2 && number > 18 && number < 37){
        balance = balance + (bet * 2);
    } else{
        balance -= bet; 
    }
}

function even_oddBet(parity, bet){
    if((parity == 'even' && number % 2 == 0 && number > 0) || (parity == 'odd' && number % 2 != 0)){
        balance = balance + (bet * 2);
    } else{
        balance -= bet;
    }

}

function columnBet(column, bet){
    let numstr = {};
    let str = '';
    for(let key in string){
        numstr[string[key]] = key;
        for (let key1 in numstr){
            str = [numstr[key1]];
    }
    if(column == str){
        balance = balance + (bet * 3);
    } else{
        balance -= bet;
    }
    }
}

function dozenBet(dozen, bet){
    if(dozen == 1 && number > 0 && number < 13 || dozen == 2 && number > 12 && number < 25 || dozen == 3 && number > 24 && number < 37){
        balance = balance + (bet * 3);
    } else{
        balance -= bet; 
    }
}

function sixlineBet(line, bet){
    let table = [
        [1, 2, 3, 4, 5, 6], 
        [4, 5, 6, 7, 8, 9], 
        [7, 8, 9, 10, 11, 12], 
        [10, 11, 12, 13, 14, 15], 
        [13, 14, 15, 16, 17, 18], 
        [16, 17, 18, 19, 20, 21], 
        [19, 20, 21, 22, 23, 24],
        [22, 23, 24, 25, 26, 27],
        [25, 26, 27, 28, 29, 30],
        [28, 29, 30, 31, 32, 33], 
        [31, 32, 33, 34, 35, 36]
    ];

    if (!!~table[line].indexOf(number)) {
        balance = balance + (bet * 6);
    } else {
        balance -= bet;
    }
}

function cornerBet(corner, bet){
    let table = [
        [0, 1, 2, 3],
        [1, 2, 4, 5], [2, 3, 5, 6], [4, 5, 7, 8], [5, 6, 8, 9],
        [7, 8, 10, 11], [8, 9, 11, 12], [10, 11, 13, 14], [11, 12, 14, 15],
        [13, 14, 16, 17], [14, 15, 17, 18], [16, 17 ,19, 20], [17, 18, 20, 21],
        [19, 20, 22, 23], [20, 21, 23, 24], [22, 23, 25, 26], [23, 24, 26, 27],
        [25, 26, 28, 29], [26, 27, 29, 30], [28, 29, 31, 32], [29, 30, 32, 33],
        [31, 32, 34, 35], [32, 33, 35 ,36] 
    ];
    if(table[corner].indexOf(number)>=0){
        balance = balance + (bet * 9);
    } else{
        balance -= bet;
    }
    
}

function streetBet(street, bet){
    let table = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12],
        [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24],
        [25, 26, 27], [28, 29, 30], [31, 32, 33], [34, 35, 36]
    ];
    if(!!~table[street].indexOf(number)){
        balance = balance + (bet * 12)    
    } else{
        balance -= bet;
    }
}

function splitBet(split, bet){
    table = [[0, 1, 2], [0, 2, 3]];
    if(!!~table[split].indexOf(number)){
        balance = balance + (bet * 12)
    } else{
        balance -= bet;
    }
}


red_blackBet('red', 1)

console.log(balance);