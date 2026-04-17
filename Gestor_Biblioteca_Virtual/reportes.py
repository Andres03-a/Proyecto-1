import json
from gestion_libros import cargar_libros
import config

ruta_reporte = config.ruta_absoluta/"Data/reportes/reporte_libros.json"

def reporte():
    libros = cargar_libros()

    print("REPORTE DE INVENTARIO")
    categorias = {}

    for i in libros:
        genero = i["Genero"]

        if genero not in categorias:
            categorias[genero] = []
        categorias[genero].append(i)
    
    for genero, lista in categorias.items():
        print(f"{genero}: ")
        for libro in lista:
            estado = libro["Estado"]
            if "Usuario" in libro and libro["Usuario"]:
                estado += f" a {libro['Usuario']}"

            print(f"- {libro['Titulo']} | {estado}")
    nombre_archivo = ruta_reporte

    with open(nombre_archivo, "w") as file:
        json.dump(categorias,file, indent=4, ensure_ascii=False)

        print("Reporte guardado en data/reportes")
        input("Presione enter para continuar")