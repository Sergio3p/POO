from clase_vehiculo import Vechiculo

class Camion(Vechiculo):
    __capacidadMax:float
    __cargaRealTransp:float
    __ruta: object
    def __init__(self,matricula,modelo,costoxKM,cantDias,capacidadMax,cargaRealTransp,ruta):
        super().__init__(matricula, modelo, costoxKM, cantDias)
        self.__capacidadMax = capacidadMax
        self.__cargaRealTransp = cargaRealTransp
        self.__ruta = ruta
        self.__lista = []
    def get_capacidadMax(self):
        return self.__capacidadMax
    
    def get_cargaRealTransp(self):
        return self.__cargaRealTransp
    
    def agregar_ruta(self):
        self.__lista.append(self.__ruta)
    
    def calcular_costo(self):
        alquiler = 0
        if self.__cargaRealTransp > 4500:
            alquiler = (self.get_cantDias() * self.get_costoxKM()) + (self.get_costoxKM() * 0.05)
        elif self.__cargaRealTransp <= 4500:
            alquiler = (float(self.get_cantDias()) * float(self.get_costoxKM())) + (self.get_costoxKM() * 0.05)
        return float(alquiler)
    
    def __str__(self):
        return f"Matricula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Costo x KM: {self.get_costoxKM()}, Cant Dias: {self.get_cantDias()}, Capacidad Max: {self.get_capacidadMax()}, Carga Real Transp: {self.get_cargaRealTransp()}, Ruta: {self.__ruta}"