def mostrar_mensaje(mensaje):
    print(mensaje)

def mostrar_menu():
    mostrar_mensaje("===== TOURS CUENCA =====")
    mostrar_mensaje("1. Registrar tour")
    mostrar_mensaje("2. Mostrar tours")
    mostrar_mensaje("3. Reservar cupos")
    mostrar_mensaje("4. Salir")

def pedir_opcion():
    return int(input("Ingrese una opcion: "))

def pedir_datos_tour():
    nombre = input("Ingrese el nombre: ")
    precio = float(input("Ingrese el precio: "))
    cupos = int(input("Ingrese los cupos: "))
    return nombre, precio, cupos

def pedir_datos_reserva():
    codigo = int(input("Ingrese el codigo del tour: "))
    cantidad = int(input("Ingrese la cantidad de cupos: "))
    return codigo, cantidad

def mostrar_tours(tours):
    mostrar_mensaje("LISTA DE TOURS")
    if not tours:
        mostrar_mensaje("No hay tours registrados.")
    for tour in tours:
        print(tour)