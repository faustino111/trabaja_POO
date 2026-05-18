class Libros:
    def __init__(self, id, titulo, autor, genero, disponibilidad=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponibilidad = disponibilidad

    def prestar(self):
        if self.disponibilidad:
            self.disponibilidad = False
            return True 
        else:
            print("Error: el libro no está disponible.")
            return False

