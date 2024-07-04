import csv
from claseCliente import Cliente

class GestorC:
    __lista:list

    def __init__(self):
        self.__lista = []

    def cargarCliente(self,unCliente):
        self.__lista.append(unCliente)

    def cargarCliente_CSV(self):
        with open('ClientesFarmaCiudad.csv',newline='') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                self.cargarCliente(Cliente(fila[0],fila[1],int(fila[2]),int(fila[3]),float(fila[4])))
        print("Archivos 'ClientesFarmaCiudad' cargados con exito")
    
    def actualizarSaldo(self,GM,GC):
        band = False
        i = 0
        dni = int(input("ingrese el dni del cliente: "))

        while i < len(self.__lista) and not band:
            if dni == self.__lista[i].getDni():
                print(f"""
                        Cliente: {self.__lista[i].getNombre()} {self.__lista[i].getApellido()}
                        Número de tarjeta: {self.__lista[i].getNumCuenta()}
                        Saldo anterior: {self.__lista[i].getSaldoAnt()}
                    """)
                band = True
                numCuenta = self.__lista[i].getNumCuenta()
            else:
                i+=1

        if band == True:
            GM.buscarNumCuenta(numCuenta,GC)
        else:
            print("No se encontro al cliente")
    
    def saldoActualizado(self,total,nc):
        band = False
        i = 0

        while i < len(self.__lista) and not band:
            if self.__lista[i].getNumCuenta() == nc:
                self.__lista[i].setSaldoAnt(total)
                band = True
                print(f"Saldo actualizado: {self.__lista[i].getSaldoAnt()}")
            else:
                i+=1
    
    def movimientosAbril(self,GF):
        num = int(input("Ingrese el numero de cuenta a buscar:"))    
        band = False
        i = 0
        while i < len(self.__lista) and not band:
            if self.__lista[i].getNumCuenta() == num:
                print(f"Cliente: {self.__lista[i].getApellido()} {self.__lista[i].getNombre()}")
                GF.verificarMovimientos(num)
                band = True
            else:
                i+=1
        
        