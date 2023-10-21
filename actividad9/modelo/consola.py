from modelo.datosmeteorologicos import Datos_meteorologicos

class ConsolaUI:
    def __init__(self):
        pass
    
    def iniciar(self):
        with open("datos.txt", "r") as archivo:
            calcular= Datos_meteorologicos(archivo)
            calcular.procesar_datos()