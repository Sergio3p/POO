from clase_vehiculo import Vechiculo
class Automovil(Vechiculo):
    __pasajerosMax: int
    __cantPasajerosReal: int

    def __init__(self,matricula,modelo,costoxKM,cantDias,pasajerosMax,cantPasajerosReal):
        super().__init__(matricula,modelo,costoxKM,cantDias)
        self.__pasajerosMax = pasajerosMax
        self.__cantPasajerosReal = cantPasajerosReal
    
    def get_pasajerosMax(self):
        return self.__pasajerosMax
    
    def get_cantPasajerosReal(self):
        return self.__cantPasajerosReal
    
    def calcular_costo(self):
        alquiler = self.get_cantDias()* self.get_costoxKM() + 5000 * self.__cantPasajerosReal
        return float(alquiler)
        
    def __str__(self):
        return f'Automovil:\nMatricula: {self.get_matricula()}\nModelo: {self.get_modelo()}\nCosto x KM: ${self.get_costoxKM()}\nCant Dias: {self.get_cantDias()}\nPasajeros Max: {self.__pasajerosMax}\nCant Pasajeros Real: {self.__cantPasajerosReal}'