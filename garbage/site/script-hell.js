///
let com_input = document.forms.com;
let com_intput = document.querySelector("#com_input")

com_input.onsubmit = function() {
	comAdd(this.com.value);
    document.forms.com.reset();
    return false;
}

let com_output = document.getElementById("com_output");
// let com_title = document.getElementById("com_title");
// let com_message = document.getElementById("com_message")
function comAdd(text) {
    let div_out = document.createElement('div');
    // let div_title = document.createElement('div');
    // let div_message = document.createElement('div');
    if (text.length != 0){
        // div_title.innerHTML = "User"
        div_out.innerHTML = text.split('\n').join('<br />') ;
        console.log(div_out)
        // com_title.appendChild(div_title);
        com_output.appendChild(div_out);
        console.log(text)
        return;
    }
    console.log("Не чего постить") 
}

//calculator
let cal_output = '';
let cal_out = document.querySelector(".cal_out");
let in_1 = document.querySelector(".in_1");
let in_2 = document.querySelector(".in_2");
let in_plus = document.querySelector(".in_plus");

in_1.onclick = function(){
    cal_output += '1';
    cal_out.innerHTML = cal_output;
}
in_2.onclick = function(){
    cal_output += '2';
    cal_out.innerHTML = cal_output;
}
in_plus.onclick = function(){
    cal_output += '+';
    cal_out.innerHTML = cal_output;
}