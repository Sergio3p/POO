from clase_automovil import Automovil
from clase_camion import Camion
from clase_ruta import Ruta
import csv

class GestorRuta:
    def __init__(self):
        self.__lista = []
    
    def agregar_ruta(self, ruta):
        self.__lista.append(ruta)

    def cargar_rutas_csv(self):
        with open('Rutas.csv',newline='') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader) 
            for fila in reader:
                ruta = Ruta(*fila)
                self.agregar_ruta(ruta)
        print("rutas cargadas con exito")

    def buscar_ruta(self):
        for ruta in self.__lista:
                print(ruta)
        
        band = False
        
        x = int(input("Elegir el codigo de la ruta que desea navegar: "))
        i = 0
        
        while i < len(self.__lista) and not band:
            if int(self.__lista[i].get_codigo()) == x:
                if self.__lista[i].get_ruta_asignada() == "FALSO":
                    print("Se asigno la ruta")
                    self.__lista[i].set_ruta_asignada(True)
                    band = True
                    return self.__lista[i]
            i += 1
        if not band:
            print("Ruta ya asignada")
        raise IndexError 
        