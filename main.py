from components.libros import Libros
from components.usuarios import Usuario

# Crear libros
libro1 = Libros(1, "El Principito", "Autor1", "Ficción")
libro2 = Libros(2, "1984", "Autor2", "Distopía")

# Crear usuario (lista vacía al inicio)
usuario = Usuario(1, "Ignacio", "Rodriguez", "2026")

# Lista de libros
biblioteca = [libro1, libro2]

# -------------------
# MENÚ
# -------------------
while True:
    print("\n--- SISTEMA DE PRÉSTAMOS ---")
    print("1. Prestar libro")
    print("2. Devolver libro")
    print("3. Salir")

    opcion = input("Elija una opción: ")

    # PRESTAR
    if opcion == "1":
        print("\nLibros:")
        for i, libro in enumerate(biblioteca):
            print(f"{i+1}. {libro.titulo} (Disponible: {libro.disponibilidad})")

        eleccion = int(input("Seleccione libro: ")) - 1

        if 0 <= eleccion < len(biblioteca):
            libro = biblioteca[eleccion]
            if libro.prestar():
                usuario.libros_prestados.append(libro)
                print("Préstamo exitoso")
        else:
            print("Opción inválida")

    # DEVOLVER
    elif opcion == "2":
        print("\nTus libros:")
        for i, libro in enumerate(usuario.libros_prestados):
            print(f"{i+1}. {libro.titulo}")

        if len(usuario.libros_prestados) == 0:
            print("No tenés libros")
            continue

        eleccion = int(input("Seleccione libro: ")) - 1

        if 0 <= eleccion < len(usuario.libros_prestados):
            usuario.devolver_libro(usuario.libros_prestados[eleccion])
        else:
            print("Opción inválida")

    # SALIR
    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")