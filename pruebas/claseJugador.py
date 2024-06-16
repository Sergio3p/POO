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
        self.__fecha = fecha
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
        
    def __gt__(self, otro):
        return self.__puntaje > otro.getPuntaje()
    