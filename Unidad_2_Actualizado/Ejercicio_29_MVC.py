class Tour:
    def __init__(self, codigo, nombre, precio, cupos):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cupos = cupos

    def reservar(self, cantidad):
        if cantidad <= 0 or cantidad > self.cupos:
            print("Error: solo hay", self.cupos, "cupos.")
            return False
        else:
            self.cupos = self.cupos - cantidad
            return True

    def __str__(self):
        return str(self.codigo) + " | " + self.nombre + " | $" + str(self.precio) + " | " + str(self.cupos)


tours = []

tours.append(Tour(1, "Centro historico", 15.00, 20))
tours.append(Tour(2, "El Cajas", 35.00, 12))


while True:
    print("\n===== TOURS CUENCA COLONIAL =====")
    print("1. Registrar tour")
    print("2. Mostrar tours")
    print("3. Reservar cupos")
    print("4. Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        nombre = input("Nombre del tour: ")
        precio = float(input("Precio: "))
        cupos = int(input("Cupos: "))

        codigo = len(tours) + 1

        tour = Tour(codigo, nombre, precio, cupos)
        tours.append(tour)

        print("Registrado con el codigo", codigo)

    elif opcion == 2:
        print("\nCODIGO | NOMBRE | PRECIO | CUPOS")

        for tour in tours:
            print(tour)

    elif opcion == 3:
        codigo = int(input("Ingrese el codigo del tour: "))

        encontrado = False

        for tour in tours:
            if tour.codigo == codigo:
                encontrado = True

                cantidad = int(input("Cantidad de cupos a reservar: "))

                if tour.reservar(cantidad):
                    print("Listo. Quedan", tour.cupos, "cupos.")

                break

        if encontrado == False:
            print("Error: no existe ese codigo.")

    elif opcion == 4:
        print("Saliendo del programa")
        break

    else:
        print("Opcion no valida")
