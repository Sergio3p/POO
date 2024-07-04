import csv
from claseNacimiento import Nacimiento

class gestorN:
    __lista = list

    def __init__(self):
        self.__lista = []

    def cargarNacimiento(self,unNacimiento):
        self.__lista.append(unNacimiento)

    def cargar_Nacimientos_csv(self):
        with open('Nacimientos.csv',newline='') as archivo:
            reader = csv.reader(archivo, delimiter = ';')
            next(reader)
            for fila in reader:
                self.cargarNacimiento(Nacimiento(int(fila[0]),fila[1],fila[2],fila[3],fila[4],float(fila[5])))
        print("archivos 'Nacimientos.scv' cargados con exito")
    
    def mostrarInformacion2(self,dni):
        for mujer in self.__lista:
            if mujer.getDniM() == dni:
                print(f"""
                Tipo de parto: {mujer.getTipoDeParto()}
                Bebé/s:
                Peso:               altura:
                {mujer.getPeso()}   {mujer.getAltura()}""")

    def partosMultiples(self, GM):
        print("MAMAS CON PARTOS MULTIPLES")
        i = 0
        while i < len(self.__lista):
            j = i + 1
            while j < len(self.__lista):
                if i != j and self.__lista[i] == self.__lista[j]:
                    GM.mostrarMama(self.__lista[i].getDniM())
                j += 1
            i += 1
