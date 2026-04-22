export class Libro {
  constructor(id, titulo, estado = "disponible") {
    this.id = id;
    this.titulo = titulo;
    this.estado = estado;
  }

  cambiarEstado() {
    if (this.estado === "disponible") {
      this.estado = "prestado";
    } else {
      this.estado = "disponible";
    }
  }
}