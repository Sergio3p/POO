from clasePedidos import Pedidos
import csv
import os
class GestorPedidos:
    def __init__(self):
        self.__pedidos = []

    def cargar_pedidos(self):
        os.system("cls")
        with open('EJ3\datosPedidos.csv', newline='') as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                pedido = Pedidos(*fila)
                self.__pedidos.append(pedido)
            print("Pedidos cargados correctamente")
    
    def mostrar_pedidos(self):
        for pedido in self.__pedidos:
            print(pedido)
    
    def nuevo_pedido(self, patente):
        id_p = int(input("Ingrese el id del pedido: "))
        comida = input("Ingrese la comida: ")
        tiempo_e = int(input("Tiempo estimado: "))
        tiempo_r = int(input("Tiempo real del pedido: "))
        precio = float(input("Ingrese el precio del pedido: "))
        self.__pedidos.append(Pedidos(patente, id_p, comida, tiempo_e, tiempo_r, precio))
        print("Pedido agregado correctamente")
    
    def mod_tiempo_real_pedido(self,patente):
        id_pedido = int(input("Ingrese el id del pedido: "))
        tiempo_real = int(input("Ingrese el tiempo real del pedido: "))
        i = 0
        band = False
        while i < len(self.__pedidos) and not band:
            if self.__pedidos[i].get_patente() == patente:
                self.__pedidos[i].set_tiempo_real(int(input("Ingrese el nuevo tiempo real del pedido: ")))
                print("Tiempo real modificado correctamente")
                band = True
            i += 1
        if not band:
            print("Pedido no encontrado")
        
    def promedio_entregas(self,patente):
        cont = 0
        sumador = 0
        for i in range(len(self.__pedidos)):
            if self.__pedidos[i].get_patente() == patente:
                sumador += int(self.__pedidos[i].get_tiempo_real())
                cont += 1
        total = sumador / cont
        return total

    def comisiones(self,patente):
        band = False
        i = 0
        sumador = 0
        print("""
              Identificador de pedido     Tiempo estimado     Tiempo real     Precio
              """)
        while i < len(self.__pedidos):
            if self.__pedidos[i].get_patente() == patente:
                print(f"""
                        {self.__pedidos[i].get_id_pedidos()}                         {self.__pedidos[i].get_tiempo_estimado()}               {self.__pedidos[i].get_tiempo_real()}          ${self.__pedidos[i].get_precio_pedido()}        
                        """)
                sumador += float(self.__pedidos[i].get_precio_pedido())
                band = True
            i += 1
        if not band:
            print("Sin pedidos")
        else:
            print(f"""
                Total: ${sumador}
                Comisión: ${sumador//0.20}
                """)
        
    def ordenar(self):
        self.__pedidos = sorted(self.__pedidos)
        print("Pedidos ordenados por patente")
        for i in self.__pedidos:
            print(i)