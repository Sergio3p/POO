from claseAnuncio import Anuncio

class Audiovisual(Anuncio):
    __resolucion:int

    def __init__(self, titulo, duracion, fechaCreacion, costoPorSegundo, formato,resolucion):
        super().__init__(titulo, duracion, fechaCreacion, costoPorSegundo, formato)
        self.__resolucion = resolucion

    def getResolucion(self):
        return self.__resolucion
    
    def costoTotal(self):
        if self.__resolucion == 1440:
            costo = (super().getCostoPorSegundo() * super().getDuracion()) + (0.015 * super().getCostoPorSegundo())
        elif self.__resolucion == 1080:
            costo = (super().getCostoPorSegundo() * super().getDuracion()) + (0.01 *super().getCostoPorSegundo())
        else:
            costo = super().getCostoPorSegundo() * super().getDuracion() 
        return costo

    def __str__(self):
        return super().__str__() + f", resolucion: {self.__resolucion}"