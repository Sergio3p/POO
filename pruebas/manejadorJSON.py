from claseJugador import Jugador
import json
from tkinter import Tk,ttk

class Manejador(object):
    __jugadores: list
    
    def __init__(self):
        self.__jugadores=[]
    
    def agregarJugador(self, unJugador):
        self.__jugadores.append(unJugador)
    
    def mostrarDatos(self):
        for i in range(len(self.__jugadores)):
            print(self.__jugadores[i])
    
    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        jugadores=[jug.toJSON() for jug in self.__jugadores]
     )
        return d    
    
    