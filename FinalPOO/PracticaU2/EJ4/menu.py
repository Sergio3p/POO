from gestorMoto import GestorMoto
from gestorPedidos import GestorPedidos

def menu():
    op = int(input("""Elija una opcion:
                   1) Cargar archivos CSV motos
                   2) Cargar archivos CSV pedidos
                   3) Mostrar archivos CSV motos
                   4) Mostrar archivos CSV pedidos
                   5) Cargar nuevos pedidos
                   6) Modificar el tiempo real de entrega de un pedido
                   7) Mostrar datos del conductor y tiempo promedio real de entrega de los pedidos que hizo
                   8) Listado para el pago de comisiones
                   9) Mostrar lista ordenada
                   0) Salir
                   """))
    return op


if __name__ == '__main__':
    GM = GestorMoto()
    GP = GestorPedidos()

    op = menu()

    while op!= 0:
        if op == 1:
            print("Cargando archivos CSV motos...")
            GM.cargar_motos()
        elif op == 2:
            print("Cargando archivos CSV pedidos...")
            GP.cargar_pedidos()
        elif op == 3:
            print("Mostrando archivos CSV motos...")
            GM.mostrar_motos()
        elif op == 4:
            print("Mostrando archivos CSV pedidos...")
            GP.mostrar_pedidos()
        elif op == 5:
            p = input("Ingrese la patente de la moto: ")
            v = GM.comprobar_patente(p)
            if v is True:
                GP.nuevo_pedido(p)
        elif op == 6:
            p = input("Ingrese la patente de la moto: ")
            v = GM.comprobar_patente(p)
            if v is True:
                GP.mod_tiempo_real_pedido(p)
        elif op == 7:
            p = input("Ingrese la patente de la moto: ")
            GM.datos_conductor(p,GP)
        elif op == 8:
            GM.listado_comisiones(GP)
        elif op == 9:
            GP.ordenar()
        op = menu()
