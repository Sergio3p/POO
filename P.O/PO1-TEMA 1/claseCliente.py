class Cliente:
    __nombre:str
    __apellido:str
    __dni:int
    __numCuenta:int
    __saldoAnt:float

    def __init__(self,nombre,apellido,dni,numCuenta,saldoAnt):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
        self.__numCuenta=numCuenta
        self.__saldoAnt = saldoAnt

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDni(self):
        return self.__dni
    
    def getNumCuenta(self):
        return self.__numCuenta
    
    def getSaldoAnt(self):
        return self.__saldoAnt
    
    def getNumCuenta(self):
        return self.__numCuenta
    
    def setSaldoAnt(self,otro):
        self.__saldoAnt += otro