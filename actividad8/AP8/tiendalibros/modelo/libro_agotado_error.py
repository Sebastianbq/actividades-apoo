from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    def __init__(self, libro: Libro):
        super().__init__(libro)
        self.libro= libro

    def __str__(self) -> str:
        return print(f"El libro con el titulo {self.libro.titulo} y isbn {self.libro.isbn} esta agotado")
