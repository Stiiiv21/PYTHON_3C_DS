from modelo import lista_funciones
import vista
from controlador_tours import controlador

modelo = lista_funciones()
mi_controlador =  controlador(modelo, vista)

mi_controlador.iniciar()