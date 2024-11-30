from clasePacientes import Paciente
from clasePacienteAmbulatorio import Ambulatorio
from clasePacienteHospitalizado import Hospitalizado
import csv

class Nodo:
    __paciente: Paciente
    __siguiente: object
    
    def __init__(self, paciente, siguiente):
        self.__paciente = paciente
        self.__siguiente = None

    def get_dato(self):
        return self.__paciente
    
    def get_sig(self):
        return self.__siguiente
    
    def set_sig(self, valor):
        self.__siguiente = valor

class lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_dato()
            self.__actual = self.__actual.get_sig()
            return dato
    
    def agregarPaciente(self,paciente):
        nodo = Nodo(paciente)
        nodo.set_sig(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def cargar_archivo_csv(self):
        try:
            with open('final 1\pacientes.csv',newline='') as archivo:
                reader = csv.reader(archivo)
                next(reader)
                for fila in reader:
                    if fila[0] == 'O':
                        unAmbulatorio = Ambulatorio(*fila)
                        self.agregarPaciente(unAmbulatorio)
                    elif fila[0] == 'H':
                        unHospitalizado = Hospitalizado(*fila)
                        self.agregarPaciente(unHospitalizado)
                print('Archivo cargado exitosamente.')
        except FileNotFoundError:
            print('El archivo no fue encontrado.')
        except Exception as e:
            print('Error:', e)
        