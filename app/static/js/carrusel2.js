//objeto con elementos de los slices
let contenido_clientes = [
  {
    url: "/static/src/images/imagenes_adicionales/avatar1.jpg",
    nombre: "Uldarico Andrade",
    recomendacion:
      "¿De que manera garantiza su plataforma que los profesionales certificados con los que me conectaré son realmente confiables y poseen la experiencia necesaria en el control de plagas? ¿Qué procesos siguen para asegurar su calidad y competencia?",
  },
  {
    url: "/static/src/images/imagenes_adicionales/avatar2.jpg",
    nombre: "Jonthan Espitia",
    recomendacion:
      "¿De que manera garantiza su plataforma que los profesionales certificados con los que me conectaré son realmente confiables y poseen la experiencia necesaria en el control de plagas? ¿Qué procesos siguen para asegurar su calidad y competencia?",
  },
  {
    url: "/static/src/images/imagenes_adicionales/avatar3.jpg",
    nombre: "Lady Paola Ballen",
    recomendacion:
      "¿De que manera garantiza su plataforma que los profesionales certificados con los que me conectaré son realmente confiables y poseen la experiencia necesaria en el control de plagas? ¿Qué procesos siguen para asegurar su calidad y competencia?",
  },
];

//variables necesarias
let atras_flecha = document.getElementById("atras_btn");
let adelante_flecha = document.getElementById("adelante_btn");
let imagen_cliente = document.getElementById("imagen_avatar");
let foto_cliente = document.getElementsByClassName("imagen_carrusel2");
let puntos_slide2 = document.getElementById("puntos_slide2");
let nombre = document.getElementById("nombre_caja_contenido_slice2");
let recomendacion = document.getElementById("txt_caja_contenido_slice2");

let actual_posicion = 0;

posicionCarrusel1();

//funcion del boton'atras'
atras_flecha.addEventListener("click", function () {
  actual_posicion -= 1;

  if (actual_posicion == -1) {
    actual_posicion = contenido_clientes.length - 1;
  }

  imagen_cliente.innerHTML = `<img src="${contenido_clientes[actual_posicion].url}" alt="imagen10" width="120" height="120" style="border-radius: 360px" class="imagen_carrusel2" />`;
  nombre.innerHTML = `<span class="nombre_caja_contenido_slice2">${contenido_clientes[actual_posicion].nombre}</span>`;
  recomendacion.innerHTML = `<span class="txt_caja_contenido_slice2">${contenido_clientes[actual_posicion].recomendacion}</span>`;
  posicionCarrusel1();
});

//funcion del boton'adelante'
adelante_flecha.addEventListener("click", function () {
  actual_posicion += 1;

  if (actual_posicion == contenido_clientes.length) {
    actual_posicion = 0;
  }

  imagen_cliente.innerHTML = `<img src="${contenido_clientes[actual_posicion].url}" alt="imagen10" width="120" height="120" style="border-radius: 360px" class="imagen_carrusel2" />`;
  nombre.innerHTML = `<span class="nombre_caja_contenido_slice2">${contenido_clientes[actual_posicion].nombre}</span>`;
  recomendacion.innerHTML = `<span class="txt_caja_contenido_slice2">${contenido_clientes[actual_posicion].recomendacion}</span>`;
  posicionCarrusel1();
});

//funcion para los puntos
function posicionCarrusel1() {
  puntos_slide2.innerHTML = "";
  for (var i = 0; i < contenido_clientes.length; i++) {
    if (i == actual_posicion) {
      puntos_slide2.innerHTML += `<svg xmlns="http://www.w3.org/2000/svg" 
            width="50" 
            style="color: rgb(255, 255, 255);
                    margin-right: 15px;
                    margin-left: 15px;
                    border-color: white;
                    border-width: 2.5px;
                    border-style: solid;
                    border-radius: 360px;" 
            height="50" 
            fill="currentColor" 
            class="bi bi-circle-fill" 
            viewBox="0 0 20 20"
        >
            <circle cx="10" cy="10" r="8"/>
        </svg>`;
    } else {
      puntos_slide2.innerHTML += `<svg xmlns="http://www.w3.org/2000/svg" 
            width="35" 
            style="color: white;
                    margin-right: 5px;
                    margin-left: 5px" 
            height="35" 
            fill="currentColor" 
            class="bi bi-circle-fill" 
            viewBox="0 0 16 16">
                <circle cx="8" cy="8" r="8"/>
            </svg>`;
    }
  }
}
