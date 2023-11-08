from abc import ABC, abstractclassmethod
from modelo.errores import ValidadorError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTienePalabraSecretaError, NoCumpleLongitudMinimaError


class Reglavalidacion:
    def __init__(self,longuitud_esperada: int):
        self.longitud: int= longuitud_esperada

    def validar_longitud(self,clave: str)-> bool: 
        if len(clave) > self.longitud:
            True
        else:
            False

    def contiene_mayuscula(self,clave: str) -> bool :
        letra= clave.split()
        for i in len(letra):        
            if letra[i].isupper():
                return True
    
    
    def contiene_minusculas(self,clave: str) -> bool :
        letra= clave.split()
        for i in len(letra):        
            if letra[i].islower():
               return True
    
    
    def contiene_numeros(self,clave: str) -> bool :
        letra= clave.split()
        for i in len(letra):        
            if letra[i].isdigit():
                return True
       
    
    @abstractclassmethod
    def es_valida(clave:str) -> bool:
        pass



class ReglavalidacionGanimedes:
    def contiene_caracter_especial(self,clave: str) -> bool:
        letra= clave.split()
        if "@" in letra or "_" in letra or "#" in letra or "$" in letra or "%" in letra:
            return True
        else:
            return False

    def es_valido(self,clave:str):
        longitud= 8
        reglas= Reglavalidacion(longitud)
        try:
            if not reglas.validar_longitud(clave):
                raise NoCumpleLongitudMinimaError
            if not reglas.contiene_mayuscula(clave):
                raise NoTieneLetraMayusculaError
            if not reglas.contiene_minusculas(clave):
                raise NoTieneLetraMinusculaError
            if not reglas.contiene_numeros(clave):
                raise NoTieneNumeroError
            if not self.contiene_caracter_especial(clave):
                raise NoTieneCaracterEspecialError
            return True
        except NoTieneCaracterEspecialError:
            return False
        except NoTieneNumeroError:
            return False
        except NoTieneLetraMinusculaError:
            return False
        except NoTieneLetraMayusculaError:
            return False
        except NoCumpleLongitudMinimaError:
            return False
        except ValidadorError:
            return False



class ReglaValidacionCalisto:
    def contiene_calist(clave: str) -> bool:
        palabra= clave.lower()
        if palabra.find("calisto"):
            letra= clave.split()
            contador= 0
            for i in len(letra):        
                if letra[i].isupper():
                    contador+= 1
            if contador >= 2 and contador < 7:
                return True
        return False

    def es_valido(self,clave:str):
        longitud= 6
        reglas= Reglavalidacion(longitud)
        try:
            if not reglas.validar_longitud(clave):
                raise NoCumpleLongitudMinimaError
            if not reglas.contiene_numeros(clave):
                raise NoTieneNumeroError
            if not self.contiene_calist(clave):
                raise NoTienePalabraSecretaError
            return True
        except NoTienePalabraSecretaError:
            return False
        except NoTieneNumeroError:
            return False
        except NoCumpleLongitudMinimaError:
            return False
        except ValidadorError:
            return False

        
        