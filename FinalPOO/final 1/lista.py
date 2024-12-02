from clasePacientes import Paciente
from clasePacienteAmbulatorio import Ambulatorio
from clasePacienteHospitalizado import Hospitalizado
import csv

class Nodo:
    __paciente: Paciente
    __siguiente: object
    
    def __init__(self, paciente):
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
        print("paciente agregado correctamente")
    def cargar_archivo_csv(self):
        try:
            with open(r'final 1\pacientes.csv', newline='') as archivo:  # Usa r'' para cadena cruda
                reader = csv.reader(archivo, delimiter=';')  # Especifica el delimitador
                next(reader)  # Salta la primera fila (encabezado)
                for fila in reader:
                    print(f"Leyendo fila: {fila}")  # Imprime la fila leída
                    if fila[0] == 'O':
                        unAmbulatorio = Ambulatorio(fila[1], fila[2], fila[3], fila[4], Paciente._Paciente__valorConsulta, fila[5], fila[6], fila[7])
                        self.agregarPaciente(unAmbulatorio)
                    elif fila[0] == 'H':
                        unHospitalizado = Hospitalizado(fila[1], fila[2], fila[3], fila[4], Paciente._Paciente__valorConsulta, fila[5], fila[6], fila[7], int(fila[8]), float(fila[9]))
                        self.agregarPaciente(unHospitalizado)
                print('Archivo cargado exitosamente.')
        except FileNotFoundError:
            print('El archivo no fue encontrado.')
        except Exception as e:
            print('Error:', e)


    
    def nuevo_paciente(self):
        try:
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            email = input('Email: ')
            telefono = input('Telefono: ')
            valorConsulta = 15000
            tipo_paciente = input('Tipo de paciente (O/H): ')
            if tipo_paciente.upper() == 'O':
                historial = input('Historial: ')
                alergia = input('Alergia: ')
                obra_social = input('Obra social: ')
                diagnostico = input('Diagnostico: ')
                unAmbulatorio = Ambulatorio(nombre,apellido,email,telefono,valorConsulta,historial,alergia,obra_social)
                self.agregarPaciente(unAmbulatorio)
            elif tipo_paciente.upper() == 'H':
                habitacion = input('Habitacion: ')
                diagnostico = input('Diagnostico: ')
                fecha_ing = input('Fecha: ')
                cant_dias = int(input('Cant. dias: '))
                imp_CD = input('Importe de conceptos descartables: ')
                unHospitalizado = Hospitalizado(nombre,apellido,email,telefono,valorConsulta,habitacion,fecha_ing,diagnostico,cant_dias,imp_CD)
                self.agregarPaciente(unHospitalizado)
            elif tipo_paciente.upper() == 'P':
                pass
        except:
            print('Error al ingresar datos.')
        
    
    def hospitalizados_ambulatorios(self):
        cont1 = 0
        cont2 = 0
        aux = self.__comienzo  # Usa un auxiliar para recorrer la lista
        while aux is not None:
            if isinstance(aux.get_dato(), Hospitalizado) and aux.get_dato().getDiagnostico().lower() == 'neumonia':
                cont1 += 1
            elif isinstance(aux.get_dato(), Ambulatorio):
                cont2 += 1
            aux = aux.get_sig()
        print(f"La cantidad de pacientes hospitalizados con diagnóstico de neumonía es de {cont1}, y la cantidad de pacientes ambulatorios es de {cont2}")

    def mostrar(self):
        aux = self.__comienzo  # Usa un auxiliar para recorrer la lista
        while aux is not None:
            print(aux.get_dato())
            print("------------------------------------------------")
            aux = aux.get_sig()
    
    def mostrar_paciente_cobrado(self):
        aux = self.__comienzo
        while aux is not None:
            print(f"Al paciente {aux.get_dato().getNombre()} {aux.get_dato().getApellido()} le cobraron: ${aux.get_dato().calcularImporte()}")
            print("------------------------------------------------")
            aux = aux.get_sig()

    def buscar_paciente(self,pos):
        try:
            if pos < 0 or pos >= self.__tope:
                raise IndexError("Posición inválida.")
            aux = self.__comienzo
            for _ in range(pos):
                aux = aux.get_sig()
            print(aux.get_dato())
        except IndexError as e:
            print("Error:", e)
    
    