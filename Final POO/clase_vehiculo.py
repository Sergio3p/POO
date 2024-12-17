from abc import ABC, abstractmethod

class Vechiculo(ABC):
    __matricula:str
    __modelo:str
    __costoxKM:float
    __cantDias:int
    
    def __init__(self, matricula, modelo, costoxKM, cantDias):
        self.__matricula = matricula
        self.__modelo = modelo
        self.__costoxKM = costoxKM
        self.__cantDias = cantDias
    
    def get_matricula(self):
        return self.__matricula
    
    def get_modelo(self):
        return self.__modelo
    
    def get_costoxKM(self):
        return float(self.__costoxKM)
    
    def get_cantDias(self):
        return int(self.__cantDias)
    
    @abstractmethod
    def calcular_costo(self):
        pass