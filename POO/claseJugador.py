import json
from datetime import datetime

class Jugador:
    __nombre:str
    __puntaje:int
    __fecha:datetime
    __nivel:int

    def __init__(self,nombre,puntaje,fecha,hora,nivel):
        self.__nombre = nombre
        self.__puntaje = puntaje
        self.__fecha = datetime.now()
        self.__hora = datetime.now()  # datetime.now() crea una fecha y hora actual.
        self.__nivel = nivel

    def getNombre(self):
        return self.__nombre
    
    def getPuntaje(self):
        return self.__puntaje
    
    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora
    
    def getNivel(self):
        return self.__nivel

    def setNivel(self,nuevoNivel):
        self.__nivel = nuevoNivel

    def __str__(self):
        return f'NOMBRE: {self.__nombre}  PUNTAJE: {self.__puntaje}   FECHA: {self.__fecha}   NIVEL: {self.__nivel}'
        
    def __gt__(self, otro):
        return self.__puntaje > otro.getPuntaje()
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.__nombre,
                puntaje = self.__puntaje,
                fecha = self.__fecha.strftime('%Y-%m-%d') if isinstance(self.__fecha,datetime) else str(self.__fecha),
                hora = self.__hora.strftime('%H:%M:%S') if isinstance(self.__hora, datetime) else str(self.__hora),
                nivel = self.__nivel,
                )
            )
        return d
    