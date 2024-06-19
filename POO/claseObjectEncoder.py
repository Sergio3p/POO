import json
from claseJugador import Jugador
from manejadorJSON import Manejador
from pathlib import Path
from datetime import datetime

class ObjectEncoder(object):
    def decodificarDiccionario(self,d):
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
                    if 'fecha' in atributos:
                        atributos['fecha'] = datetime.strptime(atributos['fecha'], '%Y-%m-%d')
                    if 'hora' in atributos:
                        atributos['hora'] = datetime.strptime(atributos['hora'], '%H:%M:%S')
                    unJugador=class_(**atributos)
                    Manejador.agregarJugador(unJugador)
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