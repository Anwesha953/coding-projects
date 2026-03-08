let lights = document.querySelectorAll(".light")

let colors = ["red","blue","yellow","green","purple","orange"]

function blink(){

lights.forEach(function(light){

let random = Math.floor(Math.random()*colors.length)

light.style.backgroundColor = colors[random]

})

}

setInterval(blink,500)
