from tiendalibros.modelo.carro_compra import CarroCompras
from tiendalibros.modelo.libro import Libro
import sys
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.libro_existente_error import LibroExistenteError

class TiendaLibros:
    def __init__(self):
        isbn: str
        self.catalogo: dict[isbn: str, Libro]= {}
        self.carrito: CarroCompras= CarroCompras()
    
    def adicionar_libro_a_catalogo(self,isbn: str, titulo: str, precio: float,existencias: int) -> Libro:
        if isbn in self.catalogo:
            a= self.catalogo[isbn]
            raise LibroExistenteError(a)
        else:
            libro=Libro(isbn,titulo,precio,existencias)
            self.catalogo[isbn] = libro
            return libro                
              
    def agregar_libro_a_carrito(self,libro: Libro, cantidad_a_agregar: int):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro)
        elif libro.existencias < cantidad_a_agregar:
            raise ExistenciasInsuficientesError(libro, cantidad_a_agregar)
        else:
            self.carrito.agregar_itm(libro, cantidad_a_agregar)

    def retirar_itm(self,isbn):
        self.carrito.quitar_item(isbn)

        