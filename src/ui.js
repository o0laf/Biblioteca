export function render(libros, onClick) {
  const lista = document.getElementById("lista");
  lista.innerHTML = "";

  libros.forEach(libro => {
    const div = document.createElement("div");
    div.className = "libro";

    div.innerHTML = `
      <strong>${libro.titulo}</strong><br>
      Estado: ${libro.estado}
    `;

    div.onclick = () => onClick(libro);

    lista.appendChild(div);
  });
}