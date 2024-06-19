import json
from pathlib import Path
class Punto(object):
    __x: int
    __y: int
    def __init__(self,x , y):
        self.__x=x
        self.__y=y
    def __str__(self):
        cadena='(x,y)=({},{})'.format(self.__x, self.__y)
        return cadena
    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        __atributos__=dict(
        x=self.__x,
        y=self.__y
            )
        )
        return d

class Manejador(object):
    __puntos: list
    def __init__(self):
        self.__puntos=[]
    def agregarPunto(self, unPunto):
        self.__puntos.append(unPunto)
    def mostrarDatos(self):
        for i in range(len(self.__puntos)):
            print(self.__puntos[i])
    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        puntos=[punto.toJSON() for punto in self.__puntos]
        )
        return d
class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                puntos=d['puntos']
                dPunto = puntos[0]
                manejador=class_()
                for i in range(len(puntos)):
                    dPunto=puntos[i]
                    class_name=dPunto.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPunto['__atributos__']
                    unPunto=class_(**atributos)
                    manejador.agregarPunto(unPunto)
        return manejador    
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
    
class Menu(object):
    def mostrarMenu(self):
        print('Menú de Opciones: ')
        print('-----------------')
        print('1 - Crear un Punto')
        print('2 - Guardar Puntos en Archivo')
        print('3 - Leer datos de Puntos')
        print('4 - Mostrar datos Puntos')
        print('5 - Salir')
        opcionCorrecta = False
        while not opcionCorrecta:
            opcion=int(input('Seleccione un número del 1 al 5: '))
            if opcion in [1,2,3,4,5]:
                opcionCorrecta=True
        return opcion 

if __name__=='__main__':
    jsonF=ObjectEncoder()
    puntos = Manejador()
    bandera=True
    while bandera:
        menu=Menu()
        opcion=menu.mostrarMenu()
        if opcion==1:
            print('Creando un nuevo Punto')
            x=int(input('Coordenada x: '))
            y=int(input('Coordenada y: '))
            punto=Punto(x,y)
            puntos.agregarPunto(punto)
        else:
            if opcion==2:
                d=puntos.toJSON()
                jsonF.guardarJSONArchivo(d,'datosPuntos.json')
            else:
                if opcion==3:
                    diccionario=jsonF.leerJSONArchivo('datosPuntos.json')
                    puntos=jsonF.decodificarDiccionario(diccionario)
                else:
                    if opcion==4:
                        puntos.mostrarDatos()
                    else:
                        bandera=False
    print('Ha seleccionado salir, hasta la vuelta')