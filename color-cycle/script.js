function changeColor(){

let colors = [
"red",
"blue",
"green",
"yellow",
"purple",
"orange",
"pink"
];

let random = Math.floor(Math.random()*colors.length);

document.body.style.backgroundColor = colors[random];

}
