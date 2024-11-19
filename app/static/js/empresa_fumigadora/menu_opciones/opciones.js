const navegacion2 = document.querySelector(".barra2");
const abrir2 = document.getElementById("abrir_menu");
const cerrar2 = document.getElementById("cerrar_menu");
const enlaces2 = document.querySelectorAll(".titulos_empleados");

// Abre el menú al hacer clic en el botón de abrir
abrir2.addEventListener("click", () => {
  navegacion2.classList.add("visible");
});

// Cierra el menú al hacer clic en el botón de cerrar
cerrar2.addEventListener("click", () => {
  navegacion2.classList.remove("visible");
});

// Cierra el menú al hacer clic en cualquier enlace con la clase "botones"
enlaces2.forEach((enlace2) => {
  enlace2.addEventListener("click", () => {
    navegacion2.classList.remove("visible");
  });
});
