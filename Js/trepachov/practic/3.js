#!/usr/bin/env node

let b = [1, 2, 3, 4, 5, 5, 6];
function qwe(a){
    let flag = false;
    for (i=0; i<a.length; i++){
        if(a[i] == a[i+1]){
            flag = true;
            break;
        }
    }
    if(flag == true){
        return flag;
    } else{
        return flag;
    }
}
console.log(qwe(b))