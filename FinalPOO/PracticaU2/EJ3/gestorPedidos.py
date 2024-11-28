from clasePedidos import Pedidos
import csv
import os
class GestorPedidos:
    def __init__(self):
        self.__pedidos = []

    def cargar_pedidos(self):
        os.system("cls")
        with open('FINAL POO\U2\Practica\EJ3\gestorPedidos.py', newline='') as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                pedido = Pedidos(*fila)
                self.__pedidos.append(pedido)
            print("Pedidos cargados correctamente")
    
    def mostrar_pedidos(self):
        for pedido in self.__pedidos:
            print(pedido)