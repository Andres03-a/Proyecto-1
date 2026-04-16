from gestion_libros import agregar_libro, ver, eliminar_libro
from buscar_libros import buscar
from prestamos import prestar, devolver
from reportes import reporte
from auditoria_estados import inconsistencias

while True:
    print("BIBLIOTECA VIRTUAL")
    print("1. Ver inventario de libros")
    print("2. Registrar un nuevo libro")
    print("3. Buscar un libro")
    print("4. Prestar un libro")    
    print("5. Devolver un libro")
    print("6. Reporte de inventario")  
    print("7. Eliminar libro")
    print("8. Reporte de inconsistencias")  
    print("9. Salir")  

    option=input("Seleccione una opcion: ")
    print("")


    if option == "1":
        ver()
    elif option == "2":
        agregar_libro()
    elif option == "3":
        buscar()
    elif option == "4":
        prestar()
    elif option == "5":
        devolver()
    elif option == "6":
        reporte()
    elif option == "7":
        eliminar_libro()    
    elif option == "8":
        inconsistencias()
    elif option == "9":
        print("Saliste de la biblioteca virtual")
        break
    else:
        print("Opcion invalida")
