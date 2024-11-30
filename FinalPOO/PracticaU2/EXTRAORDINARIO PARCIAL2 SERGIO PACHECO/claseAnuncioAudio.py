from claseAnuncio import Anuncio

class Audio(Anuncio):
    __canalDeAudio:str

    def __init__(self, titulo, duracion, fechaCreacion, costoPorSegundo, formato,canalDeAudio):
        super().__init__(titulo, duracion, fechaCreacion, costoPorSegundo, formato)
        self.__canalDeAudio = canalDeAudio
    
    def getCanalDeAudio(self):
        return self.__canalDeAudio
    
    def costoTotal(self):
        if self.__canalDeAudio == 'surround':
            costo = (super().getCostoPorSegundo() * super().getDuracion()) + (0.005 * super().getCostoPorSegundo())
        elif self.__canalDeAudio == 'mono':
            costo = (super().getCostoPorSegundo() * super().getDuracion()) + (0.001 * super().getCostoPorSegundo())
        else:
            costo = super().getCostoPorSegundo() * super().getDuracion() 
        return costo
    
    def __str__(self):
        return super().__str__() + f"canal de audio: {self.__canalDeAudio}"