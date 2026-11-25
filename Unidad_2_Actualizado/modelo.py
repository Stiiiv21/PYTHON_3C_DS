class Tour:
    def __init__(self, codigo, nombre, precio, cupos):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cupos = cupos

    def reservar(self, cantidad):
        if cantidad <= 0 or cantidad > self.cupos:
            return False
        else:
            self.cupos = self.cupos - cantidad
            return True

    def __str__(self):
        return str(self.codigo) + "" + self.nombre + "$" + str(self.precio) + "" + str(self.cupos)


class lista_funciones:
    def __init__(self):
        self.lista_funciones = []
        self.cargar_datos()

    def cargar_datos(self):
        datos = [
            Tour(1, "Centro historico", 15.00, 20),
            Tour(2, "El Cajas", 35.00, 12)
        ]

        for f in datos:
            self.lista_funciones.append(f)

    def registrar_tour(self, codigo, nombre, precio, cupos):
        self.lista_funciones.append(Tour(codigo, nombre, precio, cupos))

    def vender_cupos(self, codigo, cantidad):
        for funcion in self.lista_funciones:
            if funcion.codigo == codigo:
                return funcion.reservar(cantidad)

        return None

    def mostrar_lista(self):
        return self.lista_funciones

    def generar_codigo(self):
        return len(self.lista_funciones) + 1