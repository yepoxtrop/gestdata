let textarea = document.getElementById("detalle_servicio");
let contador = document.getElementById("caracteres");

textarea.addEventListener("input", () => {
  const caracteres = textarea.value.length;
  contador.innerHTML = `<span id="caracteres">${caracteres}</span>`;
  if (caracteres < 30) {
    contador.classList.add("mal");
    contador.classList.remove("bien");
  } else {
    contador.classList.remove("mal");
    contador.classList.add("bien");
  }
});
