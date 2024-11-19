//objeto con elementos de los slices
let contenido = [
  {
    url: "/static/src/images/imagen10.png",
    pregunta:
      "¿De que manera garantiza su plataforma que los profesionales certificados con los que me conectaré son realmente confiables y poseen la experiencia necesaria en el control de plagas? ¿Qué procesos siguen para asegurar su calidad y competencia?",
  },
  {
    url: "/static/src/images/imagen3.png",
    pregunta:
      "¿Cómo se asegura su plataforma de que las empresas de fumigación registradas cumplen con las normativas legales y ambientales vigentes? ¿Qué procesos de verificación llevan a cabo?",
  },
  {
    url: "/static/src/images/imagen10.png",
    pregunta:
      "¿Qué mecanismos implementa su plataforma para monitorear y evaluar la calidad del servicio prestado por las empresas de fumigación una vez que han realizado un trabajo en un hogar o negocio?",
  },
  {
    url: "/static/src/images/imagen3.png",
    pregunta:
      "¿De que manera garantiza su plataforma que los profesionales certificados con los que me conectaré son realmente confiables y poseen la experiencia necesaria en el control de plagas? ¿Qué procesos siguen para asegurar su calidad y competencia?",
  },
  {
    url: "/static/src/images/imagen10.png",
    pregunta:
      "¿Cómo se asegura su plataforma de que las empresas de fumigación registradas cumplen con las normativas legales y ambientales vigentes? ¿Qué procesos de verificación llevan a cabo?",
  },
  {
    url: "/static/src/images/imagen3.png",
    pregunta:
      "¿Qué mecanismos implementa su plataforma para monitorear y evaluar la calidad del servicio prestado por las empresas de fumigación una vez que han realizado un trabajo en un hogar o negocio?",
  },
  {
    url: "/static/src/images/imagen10.png",
    pregunta:
      "¿De que manera garantiza su plataforma que los profesionales certificados con los que me conectaré son realmente confiables y poseen la experiencia necesaria en el control de plagas? ¿Qué procesos siguen para asegurar su calidad y competencia?",
  },
  {
    url: "/static/src/images/imagen3.png",
    pregunta:
      "¿Cómo se asegura su plataforma de que las empresas de fumigación registradas cumplen con las normativas legales y ambientales vigentes? ¿Qué procesos de verificación llevan a cabo?",
  },
  {
    url: "/static/src/images/imagen10.png",
    pregunta:
      "¿Qué mecanismos implementa su plataforma para monitorear y evaluar la calidad del servicio prestado por las empresas de fumigación una vez que han realizado un trabajo en un hogar o negocio?",
  },
  {
    url: "/static/src/images/imagen3.png",
    pregunta:
      "¿De que manera garantiza su plataforma que los profesionales certificados con los que me conectaré son realmente confiables y poseen la experiencia necesaria en el control de plagas? ¿Qué procesos siguen para asegurar su calidad y competencia?",
  },
];

//variables necesarias
let atras = document.getElementById("atras");
let adelante = document.getElementById("adelante");
let imagen = document.getElementById("imagen");
let puntos = document.getElementById("punto");
let texto = document.getElementById("texto");

let actual = 0;

posicionCarrusel();

//funcion del boton'atras'
atras.addEventListener("click", function () {
  actual -= 1;

  if (actual == -1) {
    actual = contenido.length - 1;
  }

  imagen.innerHTML = `<img src="${contenido[actual].url}" alt="imagen10" class="imagen_representativa"/>`;
  texto.innerHTML = `<span class="txt_caja_contenido_slice">${contenido[actual].pregunta}</span>`;
  posicionCarrusel();
});

//funcion del boton'adelante'
adelante.addEventListener("click", function () {
  actual += 1;

  if (actual == contenido.length) {
    actual = 0;
  }

  imagen.innerHTML = `<img src="${contenido[actual].url}" alt="imagen10" class="imagen_representativa"/>`;
  texto.innerHTML = `<span class="txt_caja_contenido_slice">${contenido[actual].pregunta}</span>`;
  posicionCarrusel();
});

//funcion para los puntos
function posicionCarrusel() {
  puntos.innerHTML = "";
  for (var j = 0; j < contenido.length; j++) {
    if (j == actual) {
      puntos.innerHTML += `<svg xmlns="http://www.w3.org/2000/svg" 
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
      puntos.innerHTML += `<svg xmlns="http://www.w3.org/2000/svg" 
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
