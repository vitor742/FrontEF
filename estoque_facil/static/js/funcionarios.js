const button = document.getElementById("butao")
const modal = document.getElementById("dialogo")
const buttonClose = document.getElementById("btnclose")

button.onclick = function() {
    modal.showModal()
}

buttonClose.onclick = function() {
    modal.close()
}
