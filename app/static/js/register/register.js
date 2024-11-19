let rol1 = document.getElementById("rol1");
let rol2 = document.getElementById("rol2");
let contendor_rol1 = document.querySelector(".contendor_rol1");
let contendor_rol2 = document.querySelector(".contendor_rol2");
let intermedio = document.querySelector(".intermedio");
let intermedio2 = document.querySelector(".intermedio2");
let contenedor1 = document.querySelector(".contendor1");
let contenedor2 = document.querySelector(".contenedor2");

/*CONTENDORES*/
let nit_empresa = document.getElementById("nit_empresa");
let nombre_comercial = document.getElementById("nombre_comercial");
let solo_razonSocial = document.getElementById("solo_razonSocial");
let direccion_empresa = document.getElementById("direccion_empresa");
let departamento_empresa = document.getElementById("departamento_empresa");
let telefono_empresa = document.getElementById("telefono_empresa");
let contenedor1_de2 = document.querySelector(".contenedor1_de2");
let contenedor2_de2 = document.querySelector(".contenedor2_de2");
let descripcion_empresa = document.getElementById("descripcion_empresa");
let contraseña_empresa = document.getElementById("contraseña_empresa");
let Enombre_Ecorreo = document.getElementById("Enombre_Ecorreo");
let Etelefono_solo = document.getElementById("Etelefono_solo");

/*INPUTS*/
let nit = document.getElementById("nit");
let comercial = document.getElementById("comercial");
let razon = document.getElementById("razon");
let direccion = document.getElementById("direccion");
let departamento = document.getElementById("departamento");
let telefono = document.getElementById("telefono");
let correo = document.getElementById("correo");
let encargado_foto = document.getElementById("encargado_foto");
let descripcion = document.getElementById("descripcion");
let contraseña = document.getElementById("contraseña");
let encargado_nombre = document.getElementById("encargado_nombre");
let encargado_correo = document.getElementById("encargado_correo");
let encargado_telefono = document.getElementById("encargado_telefono");

/*EVENTOS DE CLICK SEGÚN LA CHECK BOX*/
rol1.addEventListener("click", () => {
  /*CHECKBOX*/
  contendor_rol2.classList.toggle("no_visible");
  rol2.toggleAttribute("required");

  /*CONTENEDOR*/
  nit_empresa.classList.toggle("visible");
  nombre_comercial.classList.toggle("reduce");
  solo_razonSocial.classList.toggle("visible");

  /*INPUTS*/
  nit.toggleAttribute("required");
  razon.toggleAttribute("required");
});

rol2.addEventListener("click", () => {
  /*CHECKBOX*/
  contendor_rol1.classList.toggle("no_visible");
  rol1.toggleAttribute("required");

  /*CONTENEDOR*/
  nit_empresa.classList.toggle("visible");
  nombre_comercial.classList.toggle("reduce");
  direccion_empresa.classList.toggle("reduce");
  departamento_empresa.classList.toggle("visible");
  contenedor1_de2.classList.toggle("visible");
  contenedor2_de2.classList.toggle("reduce");
  Enombre_Ecorreo.classList.toggle("visible");
  Etelefono_solo.classList.toggle("visible");

  /*INPUTS*/
  nit.toggleAttribute("required");
  departamento.toggleAttribute("required");
  encargado_nombre.toggleAttribute("required");
  encargado_correo.toggleAttribute("required");
  encargado_telefono.toggleAttribute("required");
  encargado_foto.toggleAttribute("required");
});

intermedio.addEventListener("click", () => {
  contenedor1.classList.add("no_visible");
  contenedor2.classList.add("visible");
  intermedio.classList.add("no_visible");
  intermedio2.classList.add("visible");
});

intermedio2.addEventListener("click", () => {
  contenedor1.classList.remove("no_visible");
  contenedor2.classList.remove("visible");
  intermedio.classList.remove("no_visible");
  intermedio2.classList.remove("visible");
});
