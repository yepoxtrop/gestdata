let textarea = document.getElementById("descripcion");
let contador = document.getElementById("caracteres");

textarea.addEventListener("input", () => {
  const caracteres = textarea.value.length;
  contador.innerHTML = `<span id="caracteres">${caracteres}</span>`;
  if (caracteres < 50) {
    contador.classList.add("mal");
    contador.classList.remove("bien");
  } else {
    contador.classList.remove("mal");
    contador.classList.add("bien");
  }
});

let password = document.getElementById("contraseña");
let contador2 = document.getElementById("caracteres2");

password.addEventListener("input", () => {
  const caracteres2 = password.value.length;
  contador2.innerHTML = `<span id="caracteres">${caracteres2}</span>`;
  if (caracteres2 < 10) {
    contador2.classList.add("mal");
    contador2.classList.remove("bien");
  } else {
    contador2.classList.remove("mal");
    contador2.classList.add("bien");
  }
});
