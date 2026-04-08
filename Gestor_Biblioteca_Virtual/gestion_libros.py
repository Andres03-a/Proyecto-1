import json
archivo = "Data/Libros.json"


def mostrar_libro(i):
        print("Titulo: ", i["Titulo"], "-", 
              "Autor: ", i["Autor"], "-", 
              "Genero: ", i["Genero"], "-", 
              "Año de publicacion: ", i["Año"], "-",
              "Estado: ", i["Estado"])



def cargar_libros():
    try:
        with open(archivo, "r",) as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []



def guardar(libros):
    with open(archivo, "w",encoding="utf-8") as file:
        json.dump(libros, file, indent=4, ensure_ascii=False)




def agregar_libro():
    libros = cargar_libros()
    
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    genero = input("Genero: ")
    año = int(input("Año de publicacion: "))

    libro = {
        "Titulo": titulo,
        "Autor": autor,
        "Genero": genero,
        "Año": año,
        "Estado": "Disponible",
        "Usuario": ""
    }

    libros.append(libro)
    guardar(libros)


def ver():
    libros = cargar_libros()
    for i in libros:
        mostrar_libro(i)
    print("Ruta usada: ", archivo)