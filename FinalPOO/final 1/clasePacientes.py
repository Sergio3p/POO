from abc import ABC
import abc
class Paciente(ABC):
    __nombre : str
    __apellido : str
    __email : str
    __telefono : str
    __valorConsulta : float
    def __init__(self,nombre,apellido,email,telefono,valorConsulta=15000):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__telefono = telefono
        self.__valorConsulta = valorConsulta
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getEmail(self):
        return self.__email
    
    def getTelefono(self):
        return self.__telefono
    
    def getValorConsulta(self):
        return self.__valorConsulta
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Apellido: {self.__apellido}, Email: {self.__email}, Teléfono: {self.__telefono}, Valor Consulta: ${self.__valorConsulta}"
    
    def set_valor_consulta(cls, valor_consulta):
        cls.__valorConsulta = valor_consulta

    @abc.abstractmethod 
    def calcularImporte(self):
        pass

    