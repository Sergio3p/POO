from gestor_ruta import GestorRuta
from gestor_vehiculo import GestorVehiculo

def menu():
    op = int(input("""Elija una opcion:
                   1) Cargar vehiculo
                   2) Leer por teclado una matricula y mostrar datos
                   3) Indicar para cada vehículo la matricula, modelo y el costo total de alquiler del vehículo. 
                   0) Salir
                   """))
    return op


if __name__ == '__main__':
    GR = GestorRuta()
    GR.cargar_rutas_csv()
    GV = GestorVehiculo()

    op = menu()

    while op!= 0:
        if op == 1:
            GV.agregar_vehiculo(GR)
        elif op == 2:
            v = input("Ingrese una matricula: ")
            GV.mostrar_datos(v)
        elif op == 3:
            GV.calcular_costo_alquiler()
        op = menu()
        
"""
1
2
abc123
volvo
50
5
150
123


"""