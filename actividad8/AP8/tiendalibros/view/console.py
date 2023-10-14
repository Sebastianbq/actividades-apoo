import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.libro_existente_error import LibroExistenteError

class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }
    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print("4. salir")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def retirar_libro_de_carrito_de_compras(self):
        retirar: str= input("Ingrese el isbn del libro a retirar: ")    
        self.tienda_libros.retirar_itm(retirar)
        print("Libro retirado con exito.")
    

    def agregar_libro_a_carrito_de_compras(self):
        agregar: str= input("ingrese isbn del libro a agregar: ") 
        cantidad: int= input("ingrese cantidad de unidades a comprar: ")
        try:
            if agregar in self.tienda_libros.catalogo:
                libro= self.tienda_libros.catalogo[agregar]
                self.tienda_libros.agregar_libro_a_carrito(libro, cantidad)
                print("se agrego con exito")
            else:
                print("libro no existe")
        except ExistenciasInsuficientesError as err:
            print(err)
        except LibroAgotadoError as err1:
            print(err1)
        finally:
            return

    def adicionar_un_libro_a_catalogo(self):
        isbn: str= input("ingrese isbn del libro a agregar: ") 
        titulo: str= input("ingrese titulo del libro a agregar: ") 
        precio: float= input("ingrese precio del libro: ")
        existencias: int= input("ingrese cantidad de existencias del libro: ")
        try:
            if isbn in self.tienda_libros.catalogo:
                libro= self.tienda_libros.catalogo[isbn]
            self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print(f"el libro {titulo} se agrego con exito")
        except LibroExistenteError as err:
            print()
            print(err)
        finally:
            return
        
