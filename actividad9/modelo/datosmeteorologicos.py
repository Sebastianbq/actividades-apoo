import re

class Datos_meteorologicos:
    def __init__(self,nombre_archivo):
        self.archivo= nombre_archivo

    
    def promedio(self,nombre: str, lista: list):
        numeros= []
        for i in range(len(lista)):
            if nombre in lista[i]:
               numeros.append(lista[i][1])          
        if nombre == "Viento:":
            num=[]
            for i in range (len(numeros)):
                compr_num= ([float(x) for x in (re.findall(r"-?\d+\.?\d*",numeros[i]))])
                num.extend(compr_num)            
        else:
            num= numeros  
        num_prom= [float(x) for x in num]
        promedio= sum(num_prom) / len(num_prom)
        return promedio
    

    def procesar_datos(self) -> tuple[float, float, float, float, str]:
        datos= []
        for x in self.archivo:
            datos.append(x.split())    
        temperatura= self.promedio("Temperatura:", datos)
        humedad= self.promedio("Humedad:", datos)
        Presion= self.promedio("Presion:", datos)
        viento= self.promedio("Viento:", datos)
        print("el promedio de la temperatura es:",temperatura)
        print("el promedio de la humedad es:",humedad)
        print("el promedio de la presion es:",Presion)
        print("el proemdio de la velocidad del vienteo es:",viento)

        direccion_viento: dict[str: float]= {"N": 0,
            "NNE": 22.5,
            "NE": 45,
            "ENE": 67.5,
            "E": 90,
            "ESE": 112.5,
            "SE": 135,
            "SSE": 157.5,
            "S": 180,
            "SSW": 202.5,
            "SW": 225,
            "WSW": 247.5,
            "W": 270,
            "WNW": 292.5,
            "NW": 315,
            "NNW": 337.5,
                    }

        coordenadas=[]
        for i in range(len(datos)):
            if "Viento:" in datos[i]:
               coordenadas.append(datos[i][1])   
        direccion=[]
        for i in range (len(coordenadas)):                
                letras= re.sub(r"[^a-zA-Z]","",coordenadas[i])                                
                direccion.append(letras)
        print(direccion)

        direccion_viento_obtenida= [direccion_viento[x] for x in direccion]
        conteo= {}

        for x in direccion_viento_obtenida:
            sector= int(x // 45)
            if sector in conteo:
                conteo[sector]  += 1
            else:
                conteo[sector] = 1
        
        direccion_predominante= max(conteo, key=conteo.get) * 45        
        resultado= [x for x, y in direccion_viento.items() if y == direccion_predominante] 
        nombres_direcciones= {"N": "Norte",
        "NE": "Noreste",
        "E": "Este",
        "SE": "Sureste",
        "S": "Sur",
        "SW": "Suroeste",
        "W": "Oeste",
        "NW": "Noroeste"
        }
        resultado= nombres_direcciones[resultado[0]]
        print("la direccion predominante del viento es en el:", resultado)