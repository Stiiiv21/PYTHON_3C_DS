
from modelo import lista_funciones

def mostrar_mensaje(mensaje):
    print(mensaje)

objeto = lista_funciones()

while True:
    mostrar_mensaje("===== TOURS CUENCA =====")
    mostrar_mensaje("1. Registrar tour")
    mostrar_mensaje("2. Mostrar tours")
    mostrar_mensaje("3. Reservar cupos")
    mostrar_mensaje("4. Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        mostrar_mensaje("REGISTRAR TOUR")

        nombre = input("Ingrese el nombre: ")
        precio = float(input("Ingrese el precio: "))
        cupos = int(input("Ingrese los cupos: "))

        codigo = len(objeto.mostrar_lista()) + 1

        objeto.registrar_tour(codigo, nombre, precio, cupos)

    elif opcion == 2:
        mostrar_mensaje("LISTA DE TOURS")

        for tour in objeto.mostrar_lista():
            print(tour)

    elif opcion == 3:
        mostrar_mensaje("RESERVAR CUPOS")

        codigo = int(input("Ingrese el codigo del tour: "))
        cantidad = int(input("Ingrese la cantidad de cupos: "))

        resultado = objeto.vender_cupos(codigo, cantidad)

        if resultado == True:
            mostrar_mensaje("Listo. Quedan los cupos actualizados.")

        elif resultado == None:
            mostrar_mensaje("Error: no existe ese codigo.")

    elif opcion == 4:
        mostrar_mensaje("Saliendo del programa...")
        break

    else:
        mostrar_mensaje("Opcion no valida")

    