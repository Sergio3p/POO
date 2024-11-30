from claseMoto import Moto
import csv
import os
class GestorMoto:
    def __init__(self):
        self.__motos = []


    def cargar_motos(self):
        
        try:
            with open("EJ3\datosMotos.csv", newline="") as archivo:
                reader = csv.reader(archivo)
                for fila in reader:
                    moto = Moto(*fila)
                    self.__motos.append(moto)
            print("Motos cargadas correctamente.")
        except FileNotFoundError:
            print("Error: El archivo no se encontró.")
        except Exception as e:
            print(f"Error: {e}")

        
    def mostrar_motos(self):
        for moto in self.__motos:
            print(moto)
    
    def comprobar_patente(self,patente):
        i = 0
        band = False
        while i < len(self.__motos) and not band:
            if self.__motos[i].get_patente() == patente:
                band = True
            i += 1
        
        if band:
            print("Patente encontrada")
            return True
        else:
            print("Patente no encontrada")
    
    def datos_conductor(self,patente, GP):
        i = 0
        band = False
        while i < len(self.__motos) and not band:
            if self.__motos[i].get_patente() == patente:
                v = GP.promedio_entregas(patente)
                print(f"""
                        Conductor: {self.__motos[i].get_nombre()}
                        Modelo de moto: {self.__motos[i].get_marca()}
                        Patente: {self.__motos[i].get_patente()}
                        kilometraje: {self.__motos[i].get_kilometraje()} km
                        tiempo promedio real de entrega: {v}
                    """)
                band = True
            i += 1
        if not band:
            print("Patente no encontrada")

    def listado_comisiones(self,GP):
        for i in range(len(self.__motos)):
            print(f"""
            Patente de Moto: {self.__motos[i].get_patente()}
            Conductor: {self.__motos[i].get_nombre()}
            """)
            GP.comisiones(self.__motos[i].get_patente())
