import abc
from abc import ABC

class Anuncio(ABC):
    __titulo:str
    __duracion:int
    __fechaCreacion:str
    __costoPorSegundo:float
    __formato:str

    def __init__(self, titulo, duracion, fechaCreacion, costoPorSegundo, formato):
        self.__titulo = titulo
        self.__duracion = duracion
        self.__fechaCreacion = fechaCreacion
        self.__costoPorSegundo = costoPorSegundo
        self.__formato = formato
    
    def getCostoPorSegundo(self):
        return self.__costoPorSegundo
    
    def getDuracion(self):
        return self.__duracion
    
    def getTitulo(self):
        return self.__titulo
    
    def getFormato(self):
        return self.__formato
    
    def __str__(self):
        return f'\n titulo:{self.__titulo}, duracion:{self.__duracion},fecha de creacion:{self.__fechaCreacion}, costo por segundo:{self.__costoPorSegundo}, formato:{self.__formato} \n'

    @abc.abstractmethod 
    def costoTotal(self):
        pass
