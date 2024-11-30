class Moto:
    def __init__(self,patente,marca,nombre,kilometraje):
        self.__patente = patente
        self.__marca = marca
        self.__nombre = nombre
        self.__kilometraje = kilometraje
        
    def get_patente(self):
        return self.__patente
    
    def get_marca(self):
        return self.__marca
    
    def get_nombre(self):
        return self.__nombre
    
    def get_kilometraje(self):
        return self.__kilometraje
    
    def __str__(self):
        return f'Patente: {self.__patente}, Marca: {self.__marca}, Nombre: {self.__nombre}, Kilometraje: {self.__kilometraje} km \n'
