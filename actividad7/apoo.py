from dataclasses import dataclass, field



@dataclass
class Elemento:
    nombre: str

    def __eq__ (self, nombre1: str):
        if self.nombre == nombre1:
            return True
        else:
            False


class Conjunto:
    contador = 0
    def __init__(self, nombre):
        Conjunto.contador: int = Conjunto.contador + 1
        self.__id: int = Conjunto.contador
        self.lis_elemento: list[Elemento] = []
        self.nombre: str = nombre
        
    def contiene(self, elemento: Elemento)-> bool:
        if elemento not in self.lis_elemento:
            return True
        else:
            return False

    def agregar_elemento(self, elemento: Elemento):
        if self.contiene(elemento) == True:
            self.lis_elemento.append(elemento)

    def __add__(self,otro):
        for i in range(len(otro.lis_elemento)):            
            if self.contiene(otro.lis_elemento[i-1]) == True:
                union= self.lis_elemento.append(otro.lis_elemento[i-1])                
        return self.lis_elemento
    
    @classmethod
    def intersectar(cls, conjunto1, conjunto2):        
        inter=[]

        if len(conjunto1.lis_elemento) > len(conjunto2.lis_elemento):
            may = conjunto1.lis_elemento
            men= conjunto2.lis_elemento
        else:
            may = conjunto2.lis_elemento        
            men= conjunto1.lis_elemento
        for i in range(len(may)):
            if may[i-1] not in men:
                    inter.append(may[i-1])
        intercepcion= Conjunto("<estudiantes>INTERSECTADO<profesores>")
        intercepcion.lis_elemento= inter
        return intercepcion

    def __str__(self) -> str:
        nom=[]
        for nombres in self.lis_elemento:
            nom.append(nombres.nombre)
        return f" {self.nombre}: {nom}"

    @property
    def id(self):
        return self.__id


elemento1: Elemento= Elemento("santi")
estudiantes: Conjunto= Conjunto("estudiantes")
estudiantes.agregar_elemento(elemento1)
profesores: Conjunto= Conjunto("profesores")
elemento3: Elemento= Elemento("carlos")
elemento2: Elemento= Elemento("juan")
profesores.agregar_elemento(elemento3)
profesores.agregar_elemento(elemento2)
profesores.agregar_elemento(elemento1)
print(estudiantes + profesores)
print(Conjunto.intersectar(estudiantes, profesores))
print(profesores)