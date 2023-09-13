import math

class punto:
    def __init__(self,x,y):
        self.coord_x = x
        self.coord_y = y

class circulo:
    PI = 3.1416
    def __init__(self,centro,radio):
        self.centro = centro
        self.radio = radio
        
    def calcular_area(self):
        a = self.PI * (self.radio ** 2)
        return a
    
    def calcular_perimetro(self):
        p = 2 * self.PI * self.radio
        return p
    
    def calcular_distancia(self,otro_punto):
        distancia = math.sqrt((self.centro.coord_x - otro_punto.coord_x)**2 + (self.centro.coord_y - otro_punto.coord_y)**2)
        return distancia
    
    def pertenece(self,punto):
        distancia= self.calcular_distancia(punto)
        return distancia <= self.radio
    
centro_cir = punto(1, 2)
c1= circulo(centro_cir, 5)
print(c1.calcular_area())
print(c1.calcular_perimetro())
punto_dado = punto(3, 4)

if c1.pertenece(punto_dado):
    print("pertence al circulo")
else:
    print("no pertenece al circulo")

        