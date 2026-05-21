class Usuario:
    def __init__( self, id, nombre, apellido, libros_prestados):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.libros_prestados = []

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.disponible = True  # devuelve el libro (vuelve a estar disponible)
            self.libros_prestados.remove(libro)  # lo saca de la lista del usuario
            print(f"{self.nombre} devolvió el libro: {libro.titulo}")
        else:
            print("Error: ese libro no está en la lista de préstamos del usuario.")