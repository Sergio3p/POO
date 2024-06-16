from tkinter import ttk
from tkinter import *
class Aplicacion():
    def __init__(self):
        ventana= Tk()
        ventana.geometry('300x200')
        ventana.configure(bg = 'black')
        ventana.title('Aplicación')
        ttk.Button(ventana, text='Salir', 
        command=ventana.destroy).pack(side=BOTTOM)
        ventana.mainloop()
def  testAPP():
    mi_app = Aplicacion()
if __name__ == '__main__':
    testAPP()