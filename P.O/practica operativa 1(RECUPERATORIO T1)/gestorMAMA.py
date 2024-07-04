import csv
import numpy as np 
from claseMama import Mama

class gestorMM:
    def __init__(self):
        self.__lista = np.array([])  

    def archivos_mamas_csv(self):
        with open('Mamas.csv', newline='') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                unaMama = Mama(int(fila[0]), int(fila[1]), fila[2])
                self.__lista = np.append(self.__lista, unaMama)
        print("archivos 'Mamas.csv' cargados con éxito")    

    def mostrarInformacion(self, GN):
        i = 0
        band = False
        dni = int(input("Ingrese el DNI de una mamá a buscar -> "))
        while i < len(self.__lista) and not band:
            if self.__lista[i].getDni() == dni:  
                print(f"""  Apellido y Nombre: {self.__lista[i].getAyN()}
                            Edad: {self.__lista[i].getEdad()}
                            """)
                GN.mostrarInformacion2(dni)
                band = True
            else:
                i += 1
        if not band:
            print("No se encontró el DNI.")

    def mostrarMama(self,dni):
        i = 0
        band = False

        while i < len(self.__lista) and band is False:
            if self.__lista[i].getDni() == dni:
                print(f"""  
                            ---------------------------------
                            Nombre:{self.__lista[i].getAyN()}
                            Edad:{self.__lista[i].getEdad()}
                            DNI: {self.__lista[i].getDni()}
                            ---------------------------------""")
                band = True
            else:
                i+=1