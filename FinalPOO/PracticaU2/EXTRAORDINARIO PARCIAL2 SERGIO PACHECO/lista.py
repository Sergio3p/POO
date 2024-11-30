from claseAnuncio import Anuncio
from claseAnuncioAudio import Audio
from claseAnuncioAudiovisual import Audiovisual
import csv

class Nodo:
    __Anuncio: Anuncio
    __siguiente: object
    
    def __init__(self, Anuncio):
        self.__Anuncio = Anuncio
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__Anuncio
    
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0 

    def __iter__(self):
        return self 
    
    def __getTope(self):
        return self.__tope

    def __next__(self):
        if self.__indice == self.__tope: 
            self.__actual = self.__comienzo
            self.__indice = 0 
            raise StopIteration 
        else:  
            self.__indice += 1  
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente() 
            return dato 
        
    def agregarAnuncio(self, maquina):
        nodo = Nodo(maquina)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
        
    def cargar_archivo_csv(self):
        with open('anuncios.csv','r',newline='',encoding='UTF-8') as archivo:
            reader = csv.reader(archivo, delimiter = ";")
            next(reader)
            for fila in reader:
                if fila[0] == "AA":
                    unAudio = Audio(fila[1], int(fila[2]),fila[3], float(fila[4]), fila[5], fila[6])
                    self.agregarAnuncio(unAudio)
                elif fila[0] == "AV":
                    unAudiovisual = Audiovisual(fila[1],int(fila[2]),fila[3],float(fila[4]),fila[5],fila[6])
                    self.agregarAnuncio(unAudiovisual)
        print("csv cargado")
        
    def agregarAnuncioFinal(self, unAnuncio):
        nodo = Nodo(unAnuncio)
        if self.__comienzo is None:
            self.__comienzo = nodo
            self.__actual = nodo
        else:
            aux = self.__comienzo
            while aux.getSiguiente() is not None:
                aux = aux.getSiguiente()
            aux.setSiguiente(nodo)
        self.__tope += 1

    def buscarAnuncio(self, titulo):
        actual = self.__comienzo
        encontrado = False
        while actual is not None and not encontrado:
            if isinstance(actual.getDato(), Audio) or isinstance(actual.getDato(), Audiovisual):
                if actual.getDato().getTitulo() == titulo:
                    encontrado = True  
                else:
                    actual = actual.getSiguiente()

        if encontrado:
            if isinstance(actual.getDato(), Audio):
                print(f"El anuncio con título '{titulo}' tiene las siguientes características:")
                print(f"Tipo: Audio")
                print(f"Formato: {actual.getDato().getFormato()}")
                print(f"Canal de audio: {actual.getDato().getCanalDeAudio()}")
            elif isinstance(actual.getDato(), Audiovisual):
                print(f"El anuncio con título '{titulo}' tiene las siguientes características:")
                print(f"Tipo: Audiovisual")
                print(f"Formato: {actual.getDato().getFormato()}")
                print(f"Resolución: {actual.getDato().getResolucion()}")
        else:
            print(f"No se encontró ningún anuncio con el título '{titulo}'.")

    def buscarResolucion(self, res):
        band = True
        actual = self.__comienzo
        for i in range(self.__tope):
            if actual is not None:
                if isinstance(actual.getDato(), Audiovisual):
                    if int(actual.getDato().getResolucion()) == res:
                        print(f"{actual.getDato().getTitulo()} cumple con la resolucion")
                        band = False
                actual = actual.getSiguiente()
        if band:
            print(f"No hay anuncios audiovisuales con la resolucion")
        
    def mostrar(self):        
        aux = self.__comienzo
        for aux in self:
            print("")
            print(aux)
            print(f"El costo total de este anuncio es: ${aux.costoTotal()}")
        