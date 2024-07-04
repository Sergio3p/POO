from gestorCliente import GestorC
from gestorFarmacia import GestorF


def menu():
    op = int(input("""
    [0]Salir
    [1]Cargar archivos
    [2]Actualizar Saldo
    [3]Informar si tuvo movimientos en abril
    [4]Ordenar por numero de cuentas
    """))
    return op

if __name__ == "__main__":

    GC = GestorC()
    GF = GestorF()
    op = menu()

    while op != 0:
        if op == 1:
            GC.cargarCliente_CSV()
            GF.cargarMovimientos_csv()
        elif op == 2:
            GC.actualizarSaldo(GF,GC)      
        elif op == 3:
            GC.movimientosAbril(GF)
        elif op == 4:
            GF.ordenar()
        op = menu()