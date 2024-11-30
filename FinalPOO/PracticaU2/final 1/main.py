from lista import lista

def menu():
    op = int(input("""}
                   Ingrese una opción:
                   1) Cargar achivo csv de pacientes
                   0) Salir
                   """))
    return op
if __name__ == '__main__':
    lista = lista()
    op = menu()

    while op != 0:
        if op == 1:
            lista.cargar_archivo_csv()
        op = menu()