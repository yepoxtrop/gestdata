let caracteristicas1 = document.querySelectorAll(".MEDIDAS_PREVENTIVAS");
let caracteristicas2 = document.querySelectorAll(".REPORTE_DE_SERVICIO");

let clase = document.querySelector(".clase");
let caracteristica = document.querySelector("#caracteristicas_cont");
let clases = document.querySelector("#clases_cont");


clase.addEventListener("change", (event) => {
  let valor_opcion = event.target.value;

  caracteristica.classList.add("visible");
  clases.classList.add("reduce");

  if (valor_opcion == "MEDIDAS PREVENTIVAS") {
    caracteristicas2.forEach((caracteristicas) => {
      caracteristicas.classList.add("no_visible");
    });

    caracteristicas1.forEach((caracteristicas) => {
      caracteristicas.classList.remove("no_visible");
    });
  }

  if (valor_opcion == "REPORTE DE SERVICIO") {
    caracteristicas2.forEach((caracteristicas) => {
      caracteristicas.classList.remove("no_visible");
    });

    caracteristicas1.forEach((caracteristicas) => {
      caracteristicas.classList.add("no_visible");
    });
  }
});
