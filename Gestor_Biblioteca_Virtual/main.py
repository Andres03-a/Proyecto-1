from gestion_libros import agregar_libro, ver
from buscar_libros import buscar
from prestamos import prestar, devolver
from reportes import reporte

while True:
    print("BIBLIOTECA VIRTUAL")
    print("1. Ver inventario de libros")
    print("2. Registrar un nuevo libro")
    print("3. Buscar un libro")
    print("4. Prestar un libro")    
    print("5. Devolver un libro")
    print("6. Reporte de inventario")  
    print("7. Salir")  

    option=input("Seleccione una opcion: ")


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
        print("Saliste de la biblioteca virtual")
        break
    else:
        print("Opcion invalida")
