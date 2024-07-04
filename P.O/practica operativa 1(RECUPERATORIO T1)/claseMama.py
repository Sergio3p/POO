class Mama:
    __dni:int
    __edad:int
    __ayn:str

    def __init__(self,dni,edad,ayn):
        self.__dni=dni
        self.__edad=edad
        self.__ayn = ayn

    def getDni(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad

    def getAyN(self):
        return self.__ayn
        