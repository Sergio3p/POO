from claseMoto import Moto
import csv
import os
class GestorMoto:
    def __init__(self):
        self.__motos = []

    import os
import csv

def cargar_motos(self):
    os.system("cls")
    try:
        with open("FINAL POO\U2\Practica\EJ3\gestorMoto.py", newline="") as archivo:
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
    
