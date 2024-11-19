let nueva_contraseña = document.getElementById("nueva_contraseña");
let contador = document.getElementById("caracteres");

nueva_contraseña.addEventListener("input", () => {
  const caracteres = nueva_contraseña.value.length;
  contador.innerHTML = `<span id="caracteres">${caracteres}</span>`;
  if (caracteres < 10) {
    contador.classList.add("mal");
    contador.classList.remove("bien");
  } else {
    contador.classList.remove("mal");
    contador.classList.add("bien");
  }
});

let contraseña_verificar = document.getElementById("contraseña_verificar");
let contador2 = document.getElementById("caracteres2");

contraseña_verificar.addEventListener("input", () => {
  const caracteres2 = contraseña_verificar.value.length;
  contador2.innerHTML = `<span id="caracteres">${caracteres2}</span>`;
  if (caracteres2 < 10) {
    contador2.classList.add("mal");
    contador2.classList.remove("bien");
  } else {
    contador2.classList.remove("mal");
    contador2.classList.add("bien");
  }
});
