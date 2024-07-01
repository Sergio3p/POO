from herramienta import Herramientas

class MPesada(Herramientas):
    __tipo:str
    __peso:int
    def __init__(self,marca,modelo,año,combustible,potencia,capacidad,tarifa,diasPorAlquiler,tipo,peso):
        super().__init__(marca,modelo,año,combustible,potencia,capacidad,tarifa,diasPorAlquiler)
        self.__tipo = tipo
        self.__peso = peso
    """
    def getPeso(self):
        return self.__peso
    """
    """
    def calcularTarifa(self):
        c1 = 0
        dias_por_alquiler = int(self.getDiasPorAlquiler())
        tarifa = float(self.getTarifa())
    
        if int(self.__peso) <= 10:
            c1 = dias_por_alquiler * tarifa
        elif int(self.__peso) > 10:
            c1 = dias_por_alquiler * tarifa + ((dias_por_alquiler * tarifa) * 0.1)
        else:
            return "error"
        return c1
    """
    def calcularTarifa(self):
        imp  = super().getTarifa()
        cantDias = super().getDiasPorAlquiler()
        if int(self.__peso) <= 10:
            imp = float(imp * cantDias)
        elif int(self.__peso) > 10:
            imp = float(imp) * int(cantDias) + float(int(cantDias) * 20 / 100)
        return imp
    
    def getTipo(self):
        return self.__tipo
    
    def __str__(self):
        return super().__str__() + f"{self.__tipo}, {self.__peso}"