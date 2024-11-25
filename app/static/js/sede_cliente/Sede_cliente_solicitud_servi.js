function countCharacters() {
    const textarea = document.getElementById('descripcion');
    const count = textarea.value.length;
    document.getElementById('caracteres').textContent = count;
}