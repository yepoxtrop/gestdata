let boton1 = document.getElementById("editar");
let boton2 = document.getElementById("borrar");
let pencil = document.getElementById("vector_lapiz");
let trash = document.querySelector(".bi.bi-trash3");

boton1.addEventListener("mouseover", () => {
  pencil.classList.add("activo");
});

boton1.addEventListener("mouseout", () => {
  pencil.classList.remove("activo");
});

boton2.addEventListener("mouseover", () => {
  trash.classList.add("activo");
});

boton2.addEventListener("mouseout", () => {
  trash.classList.remove("activo");
});
