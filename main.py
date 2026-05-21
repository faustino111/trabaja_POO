from components.libros import Libros
from components.usuario import Usuario
from components.usuarios import Usuarios
from components.biblioteca import Biblioteca

# ── Gestión de usuarios ──
gestion_usuarios = Usuarios()
gestion_usuarios.crear_usuario(101, "Ignacio",   "Rodriguez", "101")
gestion_usuarios.crear_usuario(102, "Valentina", "López",     "102")
gestion_usuarios.crear_usuario(103, "Mateo",     "González",  "103")
gestion_usuarios.crear_usuario(104, "Sofía",     "Martínez",  "104")
gestion_usuarios.crear_usuario(105, "Lucía",     "Fernández", "105")

# ── Gestión de libros ──
gestion_libros = Biblioteca()
gestion_libros.cargar_libro(1, "El Principito",           "Antoine de Saint-Exupéry", "Ficción")
gestion_libros.cargar_libro(2, "1984",                    "George Orwell",            "Distopía")
gestion_libros.cargar_libro(3, "Cien Años de Soledad",    "Gabriel García Márquez",   "Realismo Mágico")
gestion_libros.cargar_libro(4, "Don Quijote",             "Miguel de Cervantes",      "Clásico")
gestion_libros.cargar_libro(5, "Harry Potter",            "J.K. Rowling",             "Fantasía")
gestion_libros.cargar_libro(6, "El Señor de los Anillos", "J.R.R. Tolkien",           "Fantasía")
gestion_libros.cargar_libro(7, "Crimen y Castigo",        "Fiódor Dostoyevski",       "Drama")
gestion_libros.cargar_libro(8, "El Aleph",                "Jorge Luis Borges",        "Cuentos")

# ── Objetos activos ──
usuarios_activos = {}
for u in gestion_usuarios.usuarios:
    usuarios_activos[u["id"]] = Usuario(u["id"], u["nombre"], u["apellido"], u["password"])

biblioteca_activa = {}
for l in gestion_libros.libros:
    biblioteca_activa[l["id"]] = Libros(l["id"], l["titulo"], l["autor"], l["genero"])

# ── Helpers ──
def buscar_usuario(id_ingresado):
    try:
        return usuarios_activos.get(int(id_ingresado))
    except ValueError:
        return None

# ── Submenú Usuarios ──
def menu_usuarios():
    while True:
        print("\n--- USUARIOS ---")
        print("1. Ver usuarios y préstamos")
        print("2. Agregar usuario")
        print("3. Eliminar usuario")
        print("4. Volver")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            print("\n── Usuarios y préstamos ──")
            for u in gestion_usuarios.usuarios:
                obj = usuarios_activos.get(u["id"])
                prestados = [l.titulo for l in obj.libros_prestados] if obj else []
                print(f"ID: {u['id']} | {u['nombre']} {u['apellido']} | Libros: {prestados if prestados else 'ninguno'}")

        elif opcion == "2":
            try:
                nuevo_id       = int(input("ID: "))
                nuevo_nombre   = input("Nombre: ")
                nuevo_apellido = input("Apellido: ")
                nuevo_password = input("Password: ")

                gestion_usuarios.crear_usuario(nuevo_id, nuevo_nombre, nuevo_apellido, nuevo_password)

                if nuevo_id not in usuarios_activos:
                    usuarios_activos[nuevo_id] = Usuario(nuevo_id, nuevo_nombre, nuevo_apellido, nuevo_password)

            except ValueError:
                print("Error: el ID debe ser un número.")

        elif opcion == "3":
            try:
                id_borrar = int(input("ID del usuario a eliminar: "))
                gestion_usuarios.borrar_usuario(id_borrar)

                if id_borrar in usuarios_activos:
                    del usuarios_activos[id_borrar]

            except ValueError:
                print("Error: el ID debe ser un número.")

        elif opcion == "4":
            break

        else:
            print("Opción inválida")

# ── Submenú Libros ──
def menu_libros():
    while True:
        print("\n--- LIBROS ---")
        print("1. Ver libros")
        print("2. Agregar libro")
        print("3. Eliminar libro")
        print("4. Volver")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            print("\n── Libros registrados ──")
            for libro in biblioteca_activa.values():
                print(f"ID: {libro.id} | {libro.titulo} - {libro.autor} | Disponible: {libro.disponibilidad}")

        elif opcion == "2":
            try:
                nuevo_id     = int(input("ID: "))
                nuevo_titulo = input("Título: ")
                nuevo_autor  = input("Autor: ")
                nuevo_genero = input("Género: ")

                gestion_libros.cargar_libro(nuevo_id, nuevo_titulo, nuevo_autor, nuevo_genero)

                if nuevo_id not in biblioteca_activa:
                    biblioteca_activa[nuevo_id] = Libros(nuevo_id, nuevo_titulo, nuevo_autor, nuevo_genero)

            except ValueError:
                print("Error: el ID debe ser un número.")

        elif opcion == "3":
            try:
                id_borrar = int(input("ID del libro a eliminar: "))
                gestion_libros.borrar_libro(id_borrar)

                if id_borrar in biblioteca_activa:
                    del biblioteca_activa[id_borrar]

            except ValueError:
                print("Error: el ID debe ser un número.")

        elif opcion == "4":
            break

        else:
            print("Opción inválida")

# ── Menú principal ──
while True:
    print("\n--- SISTEMA DE PRÉSTAMOS ---")
    print("1. Prestar libro")
    print("2. Devolver libro")
    print("3. Usuarios")
    print("4. Libros")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion in ("1", "2"):
        id_ingresado = input("Ingrese su ID de usuario: ")
        usuario = buscar_usuario(id_ingresado)
        if usuario is None:
            print("Error: ID de usuario no encontrado.")
            continue

    # PRESTAR
    if opcion == "1":
        libros_disponibles = list(biblioteca_activa.values())
        print("\nLibros:")
        for i, libro in enumerate(libros_disponibles):
            print(f"{i+1}. {libro.titulo} - {libro.autor} (Disponible: {libro.disponibilidad})")

        eleccion = int(input("Seleccione libro: ")) - 1

        if 0 <= eleccion < len(libros_disponibles):
            libro = libros_disponibles[eleccion]
            if libro.prestar():
                usuario.libros_prestados.append(libro)
                print(f"Préstamo exitoso. {usuario.nombre} llevó: {libro.titulo}")
        else:
            print("Opción inválida")

    # DEVOLVER
    elif opcion == "2":
        if len(usuario.libros_prestados) == 0:
            print(f"{usuario.nombre} no tiene libros prestados.")
            continue

        print(f"\nLibros de {usuario.nombre}:")
        for i, libro in enumerate(usuario.libros_prestados):
            print(f"{i+1}. {libro.titulo}")

        eleccion = int(input("Seleccione libro: ")) - 1

        if 0 <= eleccion < len(usuario.libros_prestados):
            usuario.devolver_libro(usuario.libros_prestados[eleccion])
        else:
            print("Opción inválida")

    elif opcion == "3":
        menu_usuarios()

    elif opcion == "4":
        menu_libros()

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")