from herramienta import Herramientas
from maquinariaPesada import MPesada
from maquinariaElectrica import MElectrica
import csv

class Nodo:
    __herramienta: Herramientas 
    __siguiente: object
    
    def __init__(self, herramienta):
        self.__herramienta = herramienta
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__herramienta
    
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
        
    def agregarherramienta(self, maquina):
        nodo = Nodo(maquina)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
        
    def cargar_archivo_csv(self):
        band1 = False
        band2 = False
        with open('equipos.csv','r',newline='',encoding='UTF-8') as archivo:
            reader = csv.reader(archivo, delimiter = ";")
            next(reader)
            for fila in reader:
                if fila[0] == "M":
                    unaMPesada = MPesada(fila[1], fila[2],fila[3], fila[4], fila[5], fila[6],fila[7],fila[8],fila[9],fila[10])
                    self.agregarherramienta(unaMPesada)
                elif fila[0] == "E":
                    unaMElectrica = MElectrica(fila[1], fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8], fila[9])
                    self.agregarherramienta(unaMElectrica)
        print("csv cargado")
        archivo.close()

    def buscarPosicion(self,n):
        if n < self.__getTope():
            aux = self.__comienzo
            for i in range(n):
                aux = aux.getSiguiente()
            if isinstance(aux.getDato(),MElectrica):
                print(f"En la posición {n+1} se encuentra una maquinaria Electrica")
            elif isinstance(aux.getDato(),MPesada):
                print(f"En la posición {n+1} se encuentra una maquinaria Pesada")
        else:
            raise IndexError("El valor ingresado excede el rango")
    def mostrarHerramientas(self, año):
        j = 0
        aux = self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(), MElectrica) and int(aux.getDato().getAño()) == año:
                j += 1
            aux = aux.getSiguiente()
        if j == 0:
            print("No hay máquinas eléctricas creadas en ese año")
        else:
            print(f"La cantidad total de máquinas eléctricas creadas en ese año es: {j}")
        
    def maquinariaspesadas(self, capacidad):
        contH = 0
        aux = self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(), MPesada):
                if int(aux.getDato().getCapacidad()) <= capacidad:
                    contH += 1
            aux = aux.getSiguiente()
        
        if contH != 0:
            print(f"Maquinarias pesadas, con capacidad de carga menor o igual a la ingresada por teclado: {contH}")
        else:
            print("No hay maquina que pueda soportar este peso")

    def mostrar(self):        
        aux = self.__comienzo
        for aux in self:
            print("")
            print(aux)
            print(f"La tarifa de alquiler de esta maquina es de: ${aux.calcularTarifa()}")