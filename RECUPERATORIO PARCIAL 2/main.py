from gestorEquipo import GestorE
from lista import Lista

def tipoLista():
    n = None
    while not isinstance(n, int):
        try:
            n = int(input("""
                          ---------------------------------------
                            Elegir el tipo de lista: 
                          [0]Salir del programa
                          [1]Lista de python
                          [2]Listas definidas por el programador
                          ---------------------------------------
                          ->"""))
            if n > 2:
                print("Debe ingresar una de las 3 opciones mostradas por pantalla")
                n = None
        except ValueError:
            print("Ingreso un valor de tipo string")
    return n
    
def menu():
    op = int(input("""
            [0] Salir
            [1] Cargar archivos CSV
            [2] Ingresar una posicion de la lista para saber el tipo de maquinaria
            [3] Cantidad de herramientas electricas
            [4] Cantidad de equipos de maquinaria pesadas
            [5] Mostrar todos los equipos
            """))
    return op 

if __name__ == '__main__':

    tipo = tipoLista() 
    
    if tipo == 1:
        GE = GestorE()
        op = menu()
    elif tipo == 2:
        GE = Lista()
        op = menu()
    else:
        print("el programa a finalizado")
        op = 0
    
    
    while op != 0:
        if op == 1:
            GE.cargar_archivo_csv()
        elif op == 2:
            try:
                num = int(input("Ingrese la posicion a buscar: ->"))
                GE.buscarPosicion(num-1)
            except IndexError:
                print("El valor ingresado excede el rango")
        elif op == 3:
            try:
                num = int(input("Ingrese el año: ->"))
                GE.mostrarHerramientas(num)
            except ValueError:
                print("Error: el año que ingreso fue en cadena")
        elif op == 4:
            num = int(input("ingresar por teclado la cantidad de carga de la maquina ->"))
            GE.maquinariaspesadas(num)
        elif op == 5:
            GE.mostrar()
        op = menu()
