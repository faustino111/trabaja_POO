class Usuarios:
    def __init__(self):
        self.usuarios = []

    def crear_usuario(self, id, nombre, apellido, password):
        # Verificar que el ID no esté repetido
        for u in self.usuarios:
            if u["id"] == id:
                print(f"Error: ya existe un usuario con el ID {id}.")
                return
        
        nuevo = {
            "id": id,
            "nombre": nombre,
            "apellido": apellido,
            "password": password
        }
        self.usuarios.append(nuevo)
        print(f"Usuario {nombre} {apellido} creado correctamente.")

    def borrar_usuario(self, id):
        for u in self.usuarios:
            if u["id"] == id:
                self.usuarios.remove(u)
                print(f"Usuario con ID {id} eliminado correctamente.")
                return
        print(f"Error: no se encontró un usuario con el ID {id}.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        print("\n── Usuarios registrados ──")
        for u in self.usuarios:
            print(f"ID: {u['id']} | {u['nombre']} {u['apellido']}")