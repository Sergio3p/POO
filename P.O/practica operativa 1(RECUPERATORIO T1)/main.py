from gestorMAMA import gestorMM
from gestorNacimiento import gestorN

def menu():
    op = int(input("""
    [0]Salir
    [1]Cargar archivos
    [2]Mostrar datos
    [3]Mostrar los datos de la/s mamá/s que han tenido parto múltiple
    """))
    return op

if __name__ == "__main__":

    GM = gestorMM()
    GN = gestorN()
    op = menu()

    while op != 0:
        if op == 1:
            GN.cargar_Nacimientos_csv()
            GM.archivos_mamas_csv()
        elif op == 2:
            GM.mostrarInformacion(GN)            
        elif op == 3:
            GN.partosMultiples(GM)

        op = menu()
