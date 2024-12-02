from claseAnuncio import Anuncio
from claseAnuncioAudiovisual import Audiovisual
from claseAnuncioAudio import Audio
from lista import Lista

def agregarAnuncio(GL):
    print("ingrese los datos:")
    titulo = input("ingrese el titulo:")
    duracion=int(input("ingrese la duracion:"))
    fechaCreacion = input("ingrese la fecha de creacion:")
    costoPorSegundo = float(input("ingrese el costo por segundo:"))
    formato = input("ingrese el formato:")
    tipo = int(input("""
                     ingrese el tipo de anuncio:
                     [1] Audio
                     [2] Audiovisual
                     """))
    if tipo == 1:
        canalDeAudio = input("ingrese el canal de audio:")
        unaPublicidad = Audio(titulo,duracion,fechaCreacion,costoPorSegundo,formato,canalDeAudio)
        GL.agregarAnuncioFinal(unaPublicidad)
    else:
        resolucion = int(input("ingrese la resolucion:"))
        unaPublicidad = Audiovisual(titulo,duracion,fechaCreacion,costoPorSegundo,formato,resolucion)
        GL.agregarAnuncioFinal(unaPublicidad)

def menu():
    op = int(input("""
            [0] Salir
            [1] Cargar archivos CSV
            [2] Agregar anuncio
            [3] tipo de anuncio
            [4] buscar por resolucion de video
            [5] mostrar todos los anuncios
            """))
    return op 

if __name__ == '__main__':
 
    GL = Lista()
    op = menu()       
    
    while op != 0:
        if op == 1:
            GL.cargar_archivo_csv()
        elif op == 2:
            agregarAnuncio(GL)
        elif op == 3:
            titulo = str(input("ingrese el titulo a buscar: "))
            GL.buscarAnuncio(titulo)
        elif op == 4:
            res = int(input("ingrese la resolucion: "))    
            GL.buscarResolucion(res)   
        elif op == 5:
            GL.mostrar()
        op = menu()
