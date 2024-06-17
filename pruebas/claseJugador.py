import json
from datetime import datetime

class Jugador:
    __nombre:str
    __puntaje:int
    __fecha:datetime
    __nivel:int

    def __init__(self,nombre,puntaje,fecha,nivel):
        self.__nombre = nombre
        self.__puntaje = puntaje
        self.__fecha = fecha.isoformat() #convertir fecha a cadena
        self.__nivel = nivel

    def getNombre(self):
        return self.__nombre
    
    def getPuntaje(self):
        return self.__puntaje
    
    def getFecha(self):
        return self.__fecha
    
    def getNivel(self):
        return self.__nivel
    
    def setNivel(self,nuevoNivel):
        self.__nivel = nuevoNivel

    def __str__(self):
        return f'{self.__nombre}  {self.__puntaje}   {self.__fecha}   {self.__nivel}'
        
    def __gt__(self, otro):
        return self.__puntaje > otro.getPuntaje()
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.__nombre,
                puntaje = self.__puntaje,
                fecha = self.__fecha,
                nivel = self.__nivel,
                )
            )
        return d
    