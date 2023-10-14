from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.item_compra import ItemCompra

class CarroCompras:
    def __init__(self):
        self.lista_itemcompra: list[ItemCompra]= []
    
    def agregar_itm(self, libro: Libro, cantidad: int):
        itm= ItemCompra(libro, cantidad)
        self.lista_itemcompra.append(itm)
        return itm
    
    def calcular_total(self):
        total=0
        for i in range(len(self.lista_itemcompra)):
            total += self.lista_itemcompra[i].calcular_subtotal
        return total

    def quitar_item(self,isbn: str):
        self.lista_itemcompra= [x for x in self.lista_itemcompra if x.libro.isbn != isbn]

