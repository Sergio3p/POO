from herramienta import Herramientas

class MElectrica(Herramientas):
    __durabilidad:str
    def __init__(self,marca,modelo,año,combustible,potencia,capacidad,tarifa,diasPorAlquiler,durabilidad):
        super().__init__(marca,modelo,año,combustible,potencia,capacidad,tarifa,diasPorAlquiler)
        self.__durabilidad = durabilidad
    """
    def calcularTarifa(self):
        c1 = 0
        c2 = 0
        dias_por_alquiler = int(self.getDiasPorAlquiler())
        tarifa = float(self.getTarifa())
        
        if self.__durabilidad == 'bateria':
            c1 = dias_por_alquiler * tarifa
            c2 = c1 + (c1*0.1)
        elif self.__durabilidad == 'cable':
            c2 = dias_por_alquiler * tarifa 
        else:
            'error'
        return c2
    """
    """
    def getDurabilidad(self):
        return self.__capacidad
    """
    def calcularTarifa(self):
        imp = super().getTarifa()
        cantDias= super().getDiasPorAlquiler()
        if self.__durabilidad == "bateria":
            imp = float(imp) * int(cantDias) + (int(cantDias) * 10 / 100)
        elif self.__durabilidad == "cable":
            imp = float(imp) * int(cantDias)
        return imp
    

    def __str__(self):
        return super().__str__() + f"{self.__durabilidad}"