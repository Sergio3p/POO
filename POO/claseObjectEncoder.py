import json
from claseJugador import Jugador
from manejadorJSON import Manejador
from main import SimonDice
from pathlib import Path

class ObjectEncoder(object):
    def codificarDiccionario(self,d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                jugadores = d['jugadores']
                dJugador = jugadores[0]
                Manejador = class_()
                for i in range(len(jugadores)):
                    dJugador = jugadores[i]
                    class_name=dJugador.pop('__class__')
                    class_=eval(class_name)
                    atributos=dJugador['__atributos__']
                    unJugador=class_(**atributos)
                    Manejador.agregarPunto(unJugador)
                return Manejador
   
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()            
   
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario
    
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)