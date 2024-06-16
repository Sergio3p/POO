from claseJugador import Jugador
from claseObjectEncoder import ObjectEncoder
from manejadorJSON import Manejador
import json

class Gestor:
    __lista: list

    def __init__(self):
        self.__lista = []