const navegacion = document.querySelector(".barra_navegacion");
const abrir = document.querySelector(".abrirMenu");
const cerrar = document.querySelector(".cerrarMenu");
const enlaces = document.querySelectorAll(".botones");

// Abre el menú al hacer clic en el botón de abrir
abrir.addEventListener("click", () => {
  navegacion.classList.add("visible");
});

// Cierra el menú al hacer clic en el botón de cerrar
cerrar.addEventListener("click", () => {
  navegacion.classList.remove("visible");
});

// Cierra el menú al hacer clic en cualquier enlace con la clase "botones"
enlaces.forEach((enlace) => {
  enlace.addEventListener("click", () => {
    navegacion.classList.remove("visible");
  });
});
