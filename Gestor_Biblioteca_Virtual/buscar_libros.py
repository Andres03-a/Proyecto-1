from gestion_libros import cargar_libros



def mostrar_libro(i):
        print("Titulo: ", i["Titulo"], "-", 
              "Autor: ", i["Autor"], "-", 
              "Genero: ", i["Genero"], "-", 
              "Año de publicacion: ", i["Año"], "-",
              "Estado: ", i["Estado"])
        

def buscar():
    libros = cargar_libros()
    dato = input("Buscar libro por (titulo/autor/genero): ").lower()

    encontrado = False

    for i in libros:
        if (dato in i["Titulo"].lower() or
            dato in i["Autor"].lower() or
            dato in i["Genero"].lower()):
            
            mostrar_libro(i)
            encontrado = True

    if not encontrado:
        print("No se encontro ningun libro con esta informacion")