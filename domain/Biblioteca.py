class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_por_titulo(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                print("Libro encontrado:", libro.titulo, "-", libro.autor)

    def buscar_por_autor(self, autor):
        for libro in self.libros:
            if libro.autor == autor:
                print("Libro encontrado:", libro.titulo, "-", libro.autor)