let descargar = document.getElementById("aceptar_modal");
let cancelar = document.getElementById("cerrar_modal");
let modal = document.getElementById("modal");

window.onload = function() {
    modal.showModal();
}

descargar.addEventListener("click", ()=>{
    modal.close();
})

cancelar.addEventListener("click", ()=>{
    modal.close();
})