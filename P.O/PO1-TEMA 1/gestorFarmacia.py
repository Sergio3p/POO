import csv
import numpy as np
from claseMovimiento import Movimiento
from datetime import datetime

class GestorF:
    __lista:np.array

    def __init__(self):
        self.__lista = np.array([],dtype=Movimiento)
    
    def cargarMovimientos_csv(self):
        with open('MovimientosAbril2024.csv',newline='') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                unMovimiento = Movimiento(int(fila[0]),fila[1],fila[2],fila[3],float(fila[4]))
                self.__lista = np.append(self.__lista,unMovimiento)
            
            print("Archivo 'MovimientoAbril2024' cargados con exito")
        
    def buscarNumCuenta(self, nc, GC):
        total = credito = pago = 0
        print("MOVIMIENTOS:")
        print("            Fecha               descripcion             importe         tipo de Movimiento")
        
        for j in range(len(self.__lista)):
            movimiento = self.__lista[j]
            if movimiento.getNumCuenta() == nc: 
                print(f"""
                    {movimiento.getFecha()}      {movimiento.getDescripcion()}    {movimiento.getImp()}    {movimiento.getTipoDeM()}
                    """)
                if movimiento.getTipoDeM() == 'P':
                    pago += movimiento.getImp()
                elif movimiento.getTipoDeM() == 'C':
                    credito += movimiento.getImp()
        total = credito - pago
        GC.saldoActualizado(total, nc)
    
    def verificarMovimientos(self, n):
        band = False
        i = 0
        formato = "%d/%m/%Y"
        fecha_str2 = "01/04/2024"
        fecha2 = datetime.strptime(fecha_str2, formato)

        while i < len(self.__lista) and not band:
            if self.__lista[i].getNumCuenta() == n:
                fecha1 = datetime.strptime(self.__lista[i].getFecha(), formato)
                if fecha1.month == fecha2.month:
                    print("El cliente tuvo movimientos en el mes de abril")
                else:
                    print("El cliente no tuvo movimientos en el mes de abril")
                band = True 
            i += 1  
    
    def ordenar(self):
        se1f