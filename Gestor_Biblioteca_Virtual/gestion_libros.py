import json
import config

archivo = config.ruta_absoluta/"Data/Libros.json"


def mostrar_libro(i):
        print("Titulo: ", i["Titulo"], "-", 
              "Autor: ", i["Autor"], "-", 
              "Genero: ", i["Genero"], "-", 
              "Año de publicacion: ", i["Año"], "-",
              "Estado: ", i["Estado"])



def cargar_libros():
    try:
        with open(archivo, "r", encoding="utf-8") as file:
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
    print(f"Libro '{titulo}' agregado correctamente")


def ver():
    libros = cargar_libros()
    for i in libros:
        mostrar_libro(i)
    print("Ruta usada: ", archivo)

def eliminar_libro():
    libros = cargar_libros()
    
    if len(libros) == 0:
        print("No hay libros en la biblioteca")
        return
    
    titulo = input("Título del libro a eliminar: ").lower()
    
    for i in range(len(libros)):
        if titulo in libros[i]["Titulo"].lower():
            print("\n" + "=" * 40)
            print("LIBRO ENCONTRADO:")
            mostrar_libro(libros[i])
            print("=" * 40)
            
            confirmar = input("\n¿Estás seguro de eliminar este libro? (s/n): ").lower()
            if confirmar == "s" or confirmar == "si":
                libro_eliminado = libros.pop(i)
                guardar(libros)
                print(f"\n✅ Libro '{libro_eliminado['Titulo']}' eliminado correctamente")
            else:
                print("\n❌ Eliminación cancelada")
            return
    
    print(f"\n❌ No se encontró ningún libro con '{titulo}'")
