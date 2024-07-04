from datetime import datetime

class Movimiento:
    __numCuenta:int
    __fecha:str
    __descripcion:str
    __tipoM:str
    __imp:float
    
    def __init__(self,numCuenta,fecha,descripcion,tipoM,imp):
        self.__numCuenta = numCuenta
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipoM = tipoM
        self.__imp = imp

    def getNumCuenta(self):
        return self.__numCuenta
    
    def getFecha(self):
        return self.__fecha
    
    def getDescripcion(self):
        return self.__descripcion
    
    def getTipoDeM(self):
        return self.__tipoM
    
    def getImp(self):
        return self.__imp
    
    def __lt_(self,otro):
        return self.__numCuenta < otro.getNumCuenta()