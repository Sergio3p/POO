import csv
from herramienta import Herramientas
from maquinariaElectrica import MElectrica
from maquinariaPesada import MPesada

class GestorE:
    __lista: list
    
    def __init__(self):
        self.__lista = []
    

    def cargar_archivo_csv(self):
        with open('equipos.csv','r',newline='',encoding='UTF-8') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                if fila[0]=="M":
                    objeto = MPesada(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10])
                    self.__lista.append(objeto)
                elif fila[0]=="E":
                    objeto = MElectrica(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9])
                    self.__lista.append(objeto)
            print("csv cargado")
        archivo.close()

    def buscarPosicion(self,n):
        objeto = self.__lista[n-1]
       
        if isinstance(objeto,MElectrica):
            print(f"En la posición {n} se encuentra una maquinaria Electrica")
        elif isinstance(objeto,MPesada):
            print(f"En la posición {n} se encuentra una maquinaria Pesada")
        else:
            raise IndexError("El valor ingresado excede el rango")
    
    def mostrarHerramientas(self, año):
        j = 0
        for i in self.__lista:
            if isinstance(i, MElectrica):
                if int(i.getAño()) == int(año):
                    j += 1

        if j == 0:
            print("No hay máquinas eléctricas creadas en ese año")
        else:
            print(f"La cantidad total de máquinas eléctricas creadas en ese año es: {j}")  

    def maquinariaspesadas(self, capacidad):
        contH = 0
        i = 0
        while i < len(self.__lista):
            if isinstance(self.__lista[i], MPesada):
                if int(self.__lista[i].getCapacidad()) <= capacidad:
                    contH += 1
            i += 1
        print(f"Maquinarias pesadas, con capacidad de carga menor o igual a la ingresada por teclado: {contH}")
    
    def mostrar(self):
        for i in self.__lista:
            print(f"{i}")
            print(f"La tarifa de alquiler de esta maquina es de: ${i.calcularTarifa()}")
