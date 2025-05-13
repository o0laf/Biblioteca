class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id = id_usuario
        self.libros = []

    def pedir_libro(self, libro):
        if len(self.libros) >= 3:
            print("Ya tenés 3 libros. No podés pedir más.")
        elif not libro.disponible:
            print("El libro no está disponible.")
        else:
            self.libros.append(libro)
            libro.disponible = False
            print(self.nombre, "pidió el libro:", libro.titulo)

    def devolver_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            libro.disponible = True
            print(self.nombre, "devolvió el libro:", libro.titulo)
        else:
            print("No tenés ese libro.")
