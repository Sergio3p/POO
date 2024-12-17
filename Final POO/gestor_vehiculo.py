from clase_automovil import Automovil
from clase_camion import Camion
from clase_vehiculo import Vechiculo

class GestorVehiculo:
    def __init__(self):
        self.__camion = []
        self.__automovil = []

    def agregar_vehiculo(self,GR):
        print("Ingrese el tipo de vehiculo que desea agregar:")
        print("1. Automovil")
        print("2. Camion")
        opcion = int(input("Opcion: "))
        if opcion == 1:
            matricula = input("Matricula: ")
            modelo = input("Modelo: ")
            costoxKM = float(input("Costo por KILOMETRO: "))
            cantDeDias = int(input("Cantidad de dias: "))
            pasajerosMax = int(input("Cantidad de pasajeros maximo: "))
            cantPasajerosReal = int(input("Cantidad de pasajeros real: "))
            auto = Automovil(matricula,modelo,costoxKM,cantDeDias,pasajerosMax,cantPasajerosReal)
            self.__automovil.append(auto)
        elif opcion == 2:
            try:
                matricula = input("Matricula: ")
                modelo = input("Modelo: ")
                costoxKM = float(input("Costo por KILOMETRO: "))
                cantDeDias = int(input("Cantidad de dias: "))
                capacidadMax = float(input("Capacidad maxima: "))
                cargaRealTransp = float(input("Cargar real del transporte: "))
                ruta = GR.buscar_ruta()
                camion = Camion(matricula, modelo, costoxKM, cantDeDias, capacidadMax, cargaRealTransp, ruta)
                self.__camion.append(camion)
            except Exception as e:
                print(f"Error al agregar el camion: {e}")
    
    def mostrar_datos(self, matricula):
        band = False 
        i = 0
        while i < len(self.__camion) and not band:
            if self.__camion[i].get_matricula() == matricula:  
                print("Datos del camión:")
                print(f"{self.__camion[i]}")
                band = True
            i += 1
        j = 0
        while j < len(self.__automovil) and not band:
            if self.__automovil[j].get_matricula() == matricula:
                print("Datos del automóvil:")
                print(f"{self.__automovil[j]}")
                band = True
            j += 1
        if not band:
            print("No se encontró la matrícula.")

    
    def calcular_costo_alquiler(self):
        i = 0
        j = 0
        print("Automoviles:")
        while i < len(self.__automovil):
            print(f"matricula: {self.__automovil[i].get_matricula()}, modelo: {self.__automovil[i].get_modelo()}, costo del alquiler: ${self.__automovil[i].calcular_costo()}")
            i += 1
        print("Camiones:")
        while j < len(self.__camion):
            print(f"matricula: {self.__camion[j].get_matricula()}, modelo: {self.__camion[j].get_modelo()}, costo del alquiler: ${self.__camion[j].calcular_costo()}")
            j += 1