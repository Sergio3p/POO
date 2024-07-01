import abc
from abc import ABC

class Herramientas(ABC):
    __marca:str
    __modelo:str
    __año:int
    __combustible:str
    __potencia:str
    __capacidad:str
    __tarifa:int
    __diasPorAlquiler:int

    def __init__(self,marca,modelo,año,combustible,potencia,capacidad,tarifa,diasPorAlquiler):
        self.__marca=marca
        self.__modelo=modelo
        self.__año=año
        self.__combustible=combustible
        self.__potencia=potencia
        self.__capacidad=capacidad
        self.__tarifa=tarifa
        self.__diasPorAlquiler=diasPorAlquiler
    
    @abc.abstractmethod
    def calcularTarifa(self):
        pass

    def getCapacidad(self):
        return self.__capacidad
    
    def getAño(self):
        return self.__año

    def getDiasPorAlquiler(self):
        return self.__diasPorAlquiler

    def getTarifa(self):
        return self.__tarifa

    def __str__(self):
        return f"marca: {self.__marca}, modelo: {self.__modelo}, año: {self.__año}, combustible: {self.__combustible} \n potencia: {self.__potencia}, capacidad: {self.__capacidad}, tarifa: {self.__tarifa}, dias por alquiler: {self.__diasPorAlquiler} \n"