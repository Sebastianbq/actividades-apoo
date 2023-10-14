from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, libro: Libro, cantidad: int):
        super().__init__(libro)
        self.libro= libro
        self.cantidad_a_comprar: int = cantidad

    def __str__(self) -> str:
        return print(f"El libro con titulo {self.libro.titulo} y isbn {self.libro.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar {self.cantidad}, existencias {self.libro.existencias}")
    
