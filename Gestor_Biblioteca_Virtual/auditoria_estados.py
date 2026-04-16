import json
def inconsistencias():
    archivo_libros = open("Data/Libros.json", "r", encoding="utf-8")
    libros = json.load(archivo_libros)
    archivo_libros.close()

    print("REPORTE DE INCONSISTENCIAS")
    print("-" * 40)

    libros_con_problemas = []
    contador_estado_invalido = 0
    contador_disponible_con_usuario = 0
    contador_prestado_sin_usuario = 0


    for libro in libros:
        print(libro)
        titulo = libro["Titulo"]
        autor = libro["Autor"]
        estado = libro["Estado"]
        prestado_a= libro["Usuario"]

    problema = ""

    if estado != "Disponible" and estado != "Prestado":
        problema = "Estado invalido"
        contador_estado_invalido = contador_estado_invalido + 1
    elif estado == "Disponible":
        if prestado_a != None and prestado_a != "" and prestado_a != "null":
            problema = "Disponible con usuario"
            contador_disponible_con_usuario = contador_disponible_con_usuario + 1
    elif estado == "Prestado":
        if prestado_a == None or prestado_a == "":
            problema = "Prestado sin usuario"
        contador_prestado_sin_usuario = contador_prestado_sin_usuario + 1
    
    if problema !="":
        libros_con_problemas = {
            "Titulo:": titulo,
            "Autor:":  autor,
            "Estado: ":  estado,
            "Prestado a:": prestado_a,
            "Tipo de inconsistencia:" : problema
        }

    libros_con_problemas.append(libros_con_problemas)

    if len(libros_con_problemas) > 0:
        print("LIBROS CON INCONSISTENCIAS:")
        for libro in libros_con_problemas:
            print(f" {libro['titulo']} | {autor['autor']}")
            print(f"Estado: " + {libro["estado"]} + " | Prestado a: " + {libro["prestado_a"]})
            print(f"Tipo: " + libro["tipo_inconsistencia"])
            print()
    else:
        print("No se encontraron inconsistencias")

    print("RESUMEN: ")
    print("Total de libros revisados: " + str(len(libros)))
    print("Total de libros con inconsistencias: " + str(len(libros_con_problemas)))
    print("Conteo por tipo de inconsistencias: ")
    print("- Estado invalido: " + str(contador_estado_invalido))
    print("- Disponible con usuario" + str(contador_disponible_con_usuario))
    print("- Prestados sin usuario: " + str(contador_prestado_sin_usuario))

    reporte = {
    "Libros con problemas: ": libros_con_problemas,
    "Resumen: ": {
        "total_libros_revisados: ": len(libros), 
        "Total de libros con inconsistencias: ": len(libros_con_problemas),
        "Conteo por tipo de inconsistencia: ": {
            "Estado invalido: ": contador_estado_invalido,
            "Disponible con usuario: ": contador_disponible_con_usuario,
            "Prestado sin usuario: ": contador_prestado_sin_usuario
        }
    }
}
    
    archivo2 = open("Data/reporte_auditoria_estados.json", "w", encoding="uft-8")
    json.dump(reporte, archivo2, indent=4, ensure_ascii=False)
    archivo2.close()

    print("Reporte guardado")
    input("Presione enter para continuar")