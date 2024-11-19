//nombres delos archivos
let nombre_logo = document.getElementById("logo_cliente");
let nombre_foto_encargado = document.getElementById("foto_encargado");
//archivo del logo
const foto_defecto = "/static/src/images/logos/logo_ejemplo.jpg";
let foto_logo = document.getElementById("logo_ejemplo");
//archivo foto del empleado
const empleado_defecto = "/static/src/images/imagenes_adicionales/perfil3.jpg";
let foto_encargado = document.getElementById("foto_ejemplo");

//LOGO DE LA EMPRESA
//detectar en nombre del archivo
nombre_logo.addEventListener("change", function () {
  var fileName;
  if (this.files[0]) {
    fileName = this.files[0].name;
  } else {
    fileName = "No se ha seleccionado ningún archivo";
  }

  document.getElementById("file-name").textContent = fileName;
});

//preview del archivo
nombre_logo.addEventListener("change", (e) => {
  if (e.target.files[0]) {
    let logo_cliente = new FileReader();
    logo_cliente.onload = function (e) {
      foto_logo.src = e.target.result;
    };
    logo_cliente.readAsDataURL(e.target.files[0]);
  } else {
    foto_logo.src = foto_defecto;
  }
});

//FOTO EMPLEADO
//detectar en nombre del archivo
nombre_foto_encargado.addEventListener("change", function () {
  var fileName;
  if (this.files[0]) {
    fileName = this.files[0].name;
  } else {
    fileName = "No se ha seleccionado ningún archivo";
  }

  document.getElementById("file-name2").textContent = fileName;
});

//preview del archivo
nombre_foto_encargado.addEventListener("change", (e) => {
  if (e.target.files[0]) {
    let fot_empleado = new FileReader();
    fot_empleado.onload = function (e) {
      foto_encargado.src = e.target.result;
    };
    fot_empleado.readAsDataURL(e.target.files[0]);
  } else {
    foto_encargado.src = empleado_defecto;
  }
});
