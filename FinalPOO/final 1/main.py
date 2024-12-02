from lista import lista
from clasePacientes import Paciente
def menu():
    op = int(input("""
                   Ingrese una opción:
                   1) Cargar achivo csv de pacientes
                   2) Insertar nuevo paciente
                   3) Mostrar la cantidad de pacientes hospitalizados, cuyo diagnóstico es neumonía; y la cantidad de 
                      pacientes ambulatorios que posee la clínica.
                   4) Mostrar el importe cobrado por la clinica a todos los pacientes
                   5) Ingresar un valor entero que represente una posicion para ver que paciente se encuentra
                   6) Cambiar el valor de consulta
                   0) Salir
                   """))
    return op
if __name__ == '__main__':
    lista = lista()
    op = menu()

    while op != 0:
        if op == 1:
            lista.cargar_archivo_csv()
        elif op == 2:
            lista.nuevo_paciente()
        elif op == 3:
            lista.hospitalizados_ambulatorios()
        elif op == 4:
            lista.mostrar_paciente_cobrado()
        elif op == 5:
            pos = int(input("Ingrese la posición del paciente: "))
            lista.buscar_paciente(pos)
        elif op == 6:
            valor = float(input("Ingrese el nuevo valor de consulta: "))
            lista.cambiar_valor_consulta(valor)
        op = menu()