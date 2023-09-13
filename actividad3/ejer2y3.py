import math
class punto:
    def __init__(self):
        self.coord_x = 2
        self.coord_y = 3
    
    def mostrar(self):
        print(f"las coordenadas en x es:{self.coord_x} y en y es: {self.coord_y}")
    
    def mover(self):
        self.coord_x = 8
        self.coord_y = 5
    
    def calcular_distancia(self,otro_punto):
        distancia = math.sqrt((self.coord_x - otro_punto.coord_x)**2 + (self.coord_y - otro_punto.coord_y)**2)
        return distancia
     
        
p1 = punto()
p2= punto()
p2.mover()
p1.mostrar()
p2.mostrar()

dis = p1.calcular_distancia(p2)
print("la distancia es: ",dis)

