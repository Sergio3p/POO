from clasePacientes import Paciente
class Ambulatorio(Paciente):
    __historial : str
    __alergia: str
    __obra_social: str
    def __init__(self,nombre,apellido,email,telefono,valorConsulta,historial,alergia,obra_social):
        super().__init__(nombre,apellido,email,telefono,valorConsulta)
        self.__historial = historial
        self.__alergia = alergia
        self.__obra_social = obra_social

    def getHistorial(self):
        return self.__historial
    
    def getAlergia(self):
        return self.__alergia
    
    def getObraSocial(self):
        return self.__obra_social
    
    def calcularImporte(self):
        # Usar self
        total = 0
        if self.__obra_social == "Obra Social Provincia":
            total =int (super().getValorConsulta() - 5000)
        elif self.__obra_social == "OSDE":
            total = int (super().getValorConsulta() - 2000)
        else:
            total = int (super().getValorConsulta() - 10000)
        
        return total