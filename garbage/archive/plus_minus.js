let plus = 0;
let minus = 100;

//button+1
let button_plus = document.querySelector("#button_plus")
let window_plus = document.querySelector(".window_plus")
button_plus.onclick = function() {
    plus += 1;
    window_plus.innerHTML = plus;
    minus -= 1;
    window_minus.innerHTML = minus;
}

 //button-1 
let button_minus = document.querySelector("#button_minus")
let window_minus = document.querySelector(".window_minus")
button_minus.onclick = function(){
    minus -= 1;
    window_minus.innerHTML = minus;
    plus += 1;
    window_plus.innerHTML = plus;
}
