class Nacimiento:
    __dniM:int
    __tipoDeParto:str
    __fecha:str
    __hora:str
    __peso:str
    __alturaBB:float

    def __init__(self,dniM,tipoDeParto,fecha,hora,peso,alturaBB):
        self.__dniM=dniM
        self.__tipoDeParto=tipoDeParto
        self.__fecha=fecha
        self.__hora=hora
        self.__peso=peso
        self.__alturaBB=alturaBB
        
    def getDniM(self):
        return self.__dniM

    def getTipoDeParto(self):
        return self.__tipoDeParto

    def getfecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora
    
    def getPeso(self):
        return self.__peso
    
    def getAltura(self):
        return self.__alturaBB
    
    def __eq__(self, otro):
            return self.__fecha == otro.getfecha() and self.__dniM == otro.getDniM()
