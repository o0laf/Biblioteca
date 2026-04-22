import { libros } from "./data.js";
import { render } from "./ui.js";
import { Libro } from "./libro.js";

function actualizar() {
  render(libros, manejarClick);
}

function manejarClick(libro) {
  libro.cambiarEstado();
  actualizar();
}

// CORREGIDO: id correcto del botón
document.getElementById("btn-agregar").onclick = () => {
  const titulo = prompt("Nombre del libro:");
  if (!titulo) return;

  const nuevo = new Libro(libros.length + 1, titulo);
  libros.push(nuevo);

  actualizar();
};

actualizar();