from clase_camion import Camion

class Ruta:
    __codigo:int
    __destino:str
    __distanciaTotalKM:float
    __rutaAsignada:str
    
    
    def __init__(self,codigo,destino,distanciaTotalKM,rutaAsignada):
        self.__codigo = codigo
        self.__destino = destino
        self.__distanciaTotalKM = distanciaTotalKM
        self.__rutaAsignada = rutaAsignada  
    
    def get_codigo(self):
        return self.__codigo
    
    def get_destino(self):
        return self.__destino
    
    def get_distancia_total_km(self):
        return self.__distanciaTotalKM
    
    def get_ruta_asignada(self):
        return self.__rutaAsignada

    def set_ruta_asignada(self, rutaAsignada):
        self.__rutaAsignada = rutaAsignada 
    def __str__(self):
        return f"Ruta/codigo: {self.__codigo}, Destino: {self.__destino}, Distancia Total (km): {self.__distanciaTotalKM}, Ruta Asignada: {self.__rutaAsignada}"