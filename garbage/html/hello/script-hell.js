let count = 0;
let raz = 100;


    
let button = document.querySelector("button")
let p = document.querySelector(".count")
button.onclick = function() {
    count += 1;
    p.innerHTML = count;
    raz -= 1;
    a.innerHTML = raz;
}

  
let button1 = document.querySelector("#one")
let a = document.querySelector(".window")
button1.onclick = function(){
    raz -= 1;
    a.innerHTML = raz;
    count += 1;
    p.innerHTML = count
}

