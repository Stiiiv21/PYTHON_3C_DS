class controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def registrar_tour(self):
        self.vista.mostrar_mensaje("REGISTRAR TOUR")
        nombre, precio, cupos = self.vista.pedir_datos_tour()
        codigo = self.modelo.generar_codigo()
        self.modelo.registrar_tour(codigo, nombre, precio, cupos)
        self.vista.mostrar_mensaje("Tour registrado correctamente")

    def mostrar_tours(self):
        self.vista.mostrar_tours(self.modelo.mostrar_lista())

    def reservar_cupos(self):
        self.vista.mostrar_mensaje("RESERVAR CUPOS")
        codigo, cantidad = self.vista.pedir_datos_reserva()
        resultado = self.modelo.vender_cupos(codigo, cantidad)

        if resultado == True:
            self.vista.mostrar_mensaje("Listo. Reserva completada.")
        elif resultado == None:
            self.vista.mostrar_mensaje("Error: no existe ese codigo.")
        else:
            self.vista.mostrar_mensaje("Error: cantidad invalida o no hay cupos suficientes.")

    def iniciar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion == 1:
                self.registrar_tour()
            elif opcion == 2:
                self.mostrar_tours()
            elif opcion == 3:
                self.reservar_cupos()
            elif opcion == 4:
                self.vista.mostrar_mensaje("Saliendo del programa...")
                break
            else:
                self.vista.mostrar_mensaje("Opcion no valida")