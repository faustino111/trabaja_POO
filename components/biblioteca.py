class Biblioteca:
    def __init__(self):
        self.libros = []

    def cargar_libro(self, id, titulo, autor, genero):
        for l in self.libros:
            if l["id"] == id:
                print(f"Error: ya existe un libro con el ID {id}.")
                return
        
        nuevo = {
            "id": id,
            "titulo": titulo,
            "autor": autor,
            "genero": genero
        }
        self.libros.append(nuevo)
        print(f"Libro '{titulo}' cargado correctamente.")

    def borrar_libro(self, id):
        for l in self.libros:
            if l["id"] == id:
                self.libros.remove(l)
                print(f"Libro con ID {id} eliminado correctamente.")
                return
        print(f"Error: no se encontró un libro con el ID {id}.")

    def listar_libros(self):
        if not self.libros:
            print("No hay libros registrados.")
            return
        print("\n── Libros registrados ──")
        for l in self.libros:
            print(f"ID: {l['id']} | {l['titulo']} - {l['autor']} | Género: {l['genero']}")