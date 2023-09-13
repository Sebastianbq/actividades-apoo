import math
class punto:
    def __init__(self,x,y):
        self.coord_x = x
        self.coord_y = y

class crear_rectangulo:
    def __init__(self,esquina_inferior_izq,esquina_superior_der):
        self.esquina_inferior_izquierda = esquina_inferior_izq
        self.esquina_superior_derecha = esquina_superior_der

    def calcular_perimetro(self):
        base= abs(self.esquina_inferior_izquierda.coord_x - self.esquina_superior_derecha.coord_x)
        altura = abs(self.esquina_inferior_izquierda.coord_y - self.esquina_superior_derecha.coord_y)
        perim= 2 * (base + altura)
        return perim

    def calcular_area(self):
        base= abs(self.esquina_inferior_izquierda.coord_x - self.esquina_superior_derecha.coord_x)
        altura = abs(self.esquina_inferior_izquierda.coord_y - self.esquina_superior_derecha.coord_y)
        A= base * altura
        return A

    def calcular_cuadrado(self):
        base= abs(self.esquina_inferior_izquierda.coord_x - self.esquina_superior_derecha.coord_x)
        altura = abs(self.esquina_inferior_izquierda.coord_y - self.esquina_superior_derecha.coord_y)
        return base == altura

esq_i_iz = punto(4,5)
esq_s_der = punto(2,3)

rectangulo= crear_rectangulo(esq_i_iz,esq_s_der)
perimetro = rectangulo.calcular_perimetro()
area= rectangulo.calcular_area()
print(area, perimetro)

if rectangulo.calcular_cuadrado():
    print("es un cuadrado")
else:
    print("no es un cuadrado")
    