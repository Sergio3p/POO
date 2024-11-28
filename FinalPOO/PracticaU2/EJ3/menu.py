from gestorMoto import GestorMoto
from gestorPedidos import GestorPedidos

def menu():
    op = int(input("""Elija una opcion:
                   1) Cargar archivos CSV motos
                   2) Cargar archivos CSV pedidos
                   3) Mostrar archivos CSV motos
                   4) Mostrar archivos CSV pedidos
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
            
