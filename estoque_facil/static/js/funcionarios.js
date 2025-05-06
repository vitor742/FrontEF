const button1 = document.querySelector("button")
const modal = document.querySelector("dialog")
const buttonClose = document.querySelector("dialogbutton")

button.onclick = function(){
    modal.show()
}

buttonClose.onclick = function(){
    modal.close()
}