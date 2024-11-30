from clasePacientes import Paciente

class Hospitalizado(Paciente):
    __habitacion: int
    __fecha_ing: str
    __diagnostico: str
    __cant_dias: int
    __imp_CD: str
    def __init__(self,nombre,apellido,email,telefono,valorConsulta,habitacion,fecha_ing,diagnostico,cant_dias,imp_CD):
        super().__init__(nombre, apellido, email, telefono,valorConsulta)
        self.__habitacion = habitacion
        self.__fecha_ing = fecha_ing
        self.__diagnostico = diagnostico
        self.__cant_dias = cant_dias
        self.__imp_CD = imp_CD
    
    def getHabitacion(self):
        return self.__habitacion
    
    def getFecha_ing(self): 
        return self.__fecha_ing
    
    def getDiagnostico(self):
        return self.__diagnostico
    
    def getCant_dias(self):
        return self.__cant_dias
    
    def getImp_CA(self):
        return self.__imp_CA
    
    def calcularImporte(self,x):
        total = float((self.__cant_dias * 150000) + self.__imp_CD)
        return total