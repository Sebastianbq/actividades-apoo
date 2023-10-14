from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):
    def __init__(self, libro: Libro):
        super().__init__(libro)
        self.libro= libro

    def __str__(self) -> str:
        return print("El libro ya existe en el catalogo")    


