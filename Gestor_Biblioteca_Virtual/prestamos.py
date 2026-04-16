from gestion_libros import cargar_libros, guardar

def prestar():
    libros = cargar_libros()
    titulo = input("Libro a prestar: ").lower()

    for i in libros:
        if titulo in i["Titulo"].lower():

            if i["Estado"] == "Prestado":
                print("Ese libro ya esta prestado")
                return
            usuario = input("Nombre del usuario: ")
            i["Estado"] = "Prestado"
            i["Usuario"] = usuario

            guardar(libros)
            print(f"Libro '{titulo}' prestado correctamente a {usuario}")
            return
    print("Libro no encontrado")



def devolver():
    libros = cargar_libros()
    titulo = input("Libro a devolver: ").lower()

    for i in libros:
        if titulo in i["Titulo"].lower():
            i["Estado"] = "Disponible"
            i["Usuario"] = ""

            guardar(libros)
            print(f"Libro '{titulo}' devuelto correctamente")
            return
    print("Libro no encontrado")