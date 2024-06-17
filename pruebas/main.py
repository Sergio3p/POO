import tkinter as tk
from tkinter import *
from tkinter import ttk,font,simpledialog, messagebox              # Sirve para mandar el mensaje de "perdiste" al usuario.
import random                                             # Porque son aleatorios los botones que se apretarán.
import time                                               # Para las pausas entre cada ronda.
import winsound                                           # Para ejecutar sonidos al apretar los botones.
import json
from functools import partial
from datetime import datetime

from claseJugador import Jugador
from claseObjectEncoder import ObjectEncoder
from manejadorJSON import Manejador

class SimonDice:
    __ventana: object
    __secuencia: list
    __marcador: int
    __fecha: datetime
    __puntajeRecord: int
    __contador: int
    __juegoInicial: bool
    __colores: list
    __jugador: Jugador
    __manejador: Manejador
    __encoder: ObjectEncoder

    def __init__(self):
        self.__ventana = tk.Tk()            # Se crea una ventana y se le asigna un nuevo constructor de Tk para crear el nuevo frame.
        self.__secuencia = []               # Lista donde se almacenará el ORDEN de los colores conforme se fueron encendiendo.
        self.__marcador = 0                 # Para saber cuántos puntos lleva el usuario ganando.
        self.__puntajeRecord = 0             # En caso de que se llegue a superar el récord del juego.
        self.__contador = 0                 # Permite avanzar a través de la lista.
        self.__juegoInicial = False         # Indica en qué momento el usuario apretó el botón "INICIAR".
        self.__colores = ["Verde", "Rojo", "Amarillo", "Azul"]
        self.__ventana.title("Simón Dice")
        self.__ventana.geometry("400x400")
        self.__nombreUsuario = simpledialog.askstring("Nombre", "Ingrese su nombre:")
        self.__fecha = datetime.now()
        self.__encoder = ObjectEncoder()
        self.__manejador = Manejador()
        self.barraOpciones()
        self.iniciarBotones()               # Se llama a un método que se encargará de INICIAR la INTERFAZ GRÁFICA.
        self.__ventana.configure(background="#f0f0f0")
        self.__ventana.mainloop()           # Indica que va a iniciar el CICLO PRINCIPAL del juego.
        
    # INTERFAZ GRÁFICA DEL JUEGO
    #def setNombre(self,unNombre):


    def iniciarBotones(self):
        self.__botonVerde = Button(self.__ventana, command=partial(self.presionar, "Verde"), background="#008080", highlightthickness=20, relief="raised")
        self.__botonVerde.place(relx=0.29, rely=0.25, relheight=0.45, relwidth=0.4, anchor=tk.CENTER) # Permite colocar el botón.

        self.__botonRojo = Button(self.__ventana, command=partial(self.presionar,"Rojo"), background="#ff0000", highlightthickness=20, relief="raised")
        self.__botonRojo.place(relx=0.72, rely=0.25, relheight=0.45, relwidth=0.4, anchor=tk.CENTER)  # Se cambia la posición de cada botón.

        self.__botonAmarillo = Button(self.__ventana, command=partial(self.presionar, "Amarillo"), background="#ffff00", highlightthickness=20, relief="raised")
        self.__botonAmarillo.place(relx=0.29, rely=0.73, relheight=0.45, relwidth=0.4, anchor=tk.CENTER)

        self.__botonAzul = Button(self.__ventana, command=partial(self.presionar,"Azul"), background="#0080ff", highlightthickness=20, relief="raised")
        self.__botonAzul.place(relx=0.72, rely=0.73, relheight=0.45, relwidth=0.4, anchor=tk.CENTER)

        self.__botonIniciar = Button(self.__ventana, command=self.iniciar, bg="white", text="INICIAR") # "bg" es "background".
        # Como no se manda parámetros en el command, se pone directamente el método que se va a ejecutar.
        
        self.__botonIniciar.place(relx=0.505, rely=0.45, relheight=0.1, relwidth=0.2, anchor=tk.N)
        self.__etiqueta = Label(self.__ventana, text="\nMarcador:  0\nMayor puntaje:  0") # Se coloca en 0 porque ya se sabe en qué valor INICIA.
        self.__etiqueta.place(relx=0.5, rely=0, anchor=tk.N)
    
    def barraOpciones(self):
        # Crear la barra de menú principal
        barra_menu = Menu(self.__ventana)
        
        # Crear el menú "Archivo"
        archivo_menu = Menu(barra_menu, tearoff=0)
        archivo_menu.add_command(label="ver puntajes", command=self.mostrarPuntajes)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.__ventana.quit)
        barra_menu.add_cascade(label="Puntajes", menu=archivo_menu)
        
        # Crear el menú "Ayuda"
        ayuda_menu = Menu(barra_menu, tearoff=0)
        #ayuda_menu.add_command(text="Acerca de", command=self.mostrarInfo)
        barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)
        
        # Asignar la barra de menú a la ventana principal
        self.__ventana.config(menu=barra_menu)


    def presionar(self, color):          # Se ejecuta en el momento en que el usuario presione el botón de alguno de los colores.
        if self.__juegoInicial == True:    # Sólo se revisa en qué momento el usuario aprieta los botones cuando esta variable sea igual a True.
            if len(self.__secuencia) >= self.__contador - 1: # Ya que el contador va en una posición adelantada.
                if self.__secuencia[self.__contador] == color: # Color es el parámetro enviado por cada botón al ser presionado (usuario atinó al botón).
                    self.__contador += 1               # Para que vaya avanzando
                    if color == "Verde":
                        self.sonido(600, 500)
                    elif color == "Rojo":
                        self.sonido(500, 500)
                    elif color == "Amarillo":
                        self.sonido(700, 500)
                    elif color == "Azul":
                        self.sonido(800, 500)
                    self.revisarTurno() # Llama a esta función para saber si este botón que presionó el usuario fue el último o faltan más.
                    self.__etiqueta.config(text="\nMarcador: " + str(self.__marcador) + "\nMayor puntaje: " + str(self.__puntajeRecord)) # Se cambia la etiqueta luego de que el usuario presionó los botones

                else:                   # Si el usuario se equivocó al presionar un botón (DEBE TERMINAR EL JUEGO)
                    self.finalizar()

    def finalizar(self):
        #messagebox.showinfo("Perdiste mogo", "\nPuntaje: " + str(self.__marcador))
        if self.__marcador > self.__puntajeRecord:   # Se establece un nuevo récord en caso de ser así.
            self.__puntajeRecord = self.__marcador
        self.__etiqueta.config(text="\nMarcador: " + str(self.__marcador) + "\nMayor puntaje: " + str(self.__puntajeRecord))

        self.__ventanaPerdiste = Toplevel(self.__ventana)
        self.__ventanaPerdiste.title("Perdiste mogo")
        self.__ventanaPerdiste.geometry('300x150')
        label = tk.Label(self.__ventanaPerdiste, text=f"\nPuntaje: {self.__marcador}")
        label.pack(pady=10)
    
    #JEISON
        boton_reiniciar = ttk.Button(self.__ventanaPerdiste, text="REINICIAR JUEGO", command=self.reiniciarJuego)
        boton_reiniciar.pack(side=tk.LEFT, padx=20, pady=20)
        boton_salir = ttk.Button(self.__ventanaPerdiste, text='SALIR', command=quit)
        boton_salir.pack(side=tk.RIGHT, padx=20, pady=20)
        self.cargarPuntajes()
        
                
        #self.__botonReiniciar = Button(self.__ventana, command=self.reiniciarJuego, bg="white", text="REINICIAR JUEGO")
        #self.__botonReiniciar.place(relx=0.505, rely=0.45, relheight=0.1, relwidth=0.25, anchor=tk.N)


    def reiniciarJuego(self):
        # SE RESETEAN LOS ATRIBUTOS
        self.__juegoInicial = False # Para que el usuario no siga jugando y deba presionar el botón de INICIAR para volver a jugar.
        self.__ventanaPerdiste.destroy()
        self.__nombreUsuario = simpledialog.askstring("Nombre", "Ingrese su nombre:")
        self.__fecha = datetime.now()
        self.__botonIniciar.after(1600, self.iniciar)
        
        


    def iniciar(self):                   # Lo que hace es REINICIAR todos los valores, ya sea para la 1era, 2da, 3ra o 4ta vez de iniciar el juego.
        self.__contador = 0
        self.__marcador = 0
        self.__secuencia = []
        self.__juegoInicial = True       # True porque el juego inició.
        self.__etiqueta.config(text="\nMarcador: " + str(self.__marcador) + "\nMayor puntaje: " + str(self.__puntajeRecord))
        self.__botonIniciar.destroy()
        self.crearColor()                # Método para que el usuario EMPIECE A JUGAR.

    def revisarTurno(self):
        if len(self.__secuencia) == self.__contador:  # El contador va aumentando conforme el usuario va jugando (cuando hace un punto).
            self.__contador = 0                       # Se setea en 0 porque se iniciará de nuevo.
            self.__marcador += 1                      # Aumenta el marcador porque el usuario apretó los botones correctamente (tiene un punto más).
            self.__botonIniciar.after(1000, self.crearColor)
            # El método after, después de la cantidad de MILISEGUNDOS (1000, 1 segundo), llamará a un método que AUMENTARÁ LA DIFICULTAD al añadir un color más.

    def crearColor(self):                      # Método para que permite generar un nuevo color para aumentar la dificultad dentro del juego. 
        if self.__juegoInicial == True:          # Chequea si el juego está iniciado o no.
            i = 0                              # Variable que recorre todo el arreglo.
#            self.__botonIniciar.destroy()

            while i < len(self.__secuencia):
                if self.__secuencia[i] == "Verde":
                    self.cambioColorBoton(self.__botonVerde, "white", "#008080", 500, 500)
                elif self.__secuencia[i] == "Rojo":
                    self.cambioColorBoton(self.__botonRojo, "white", "#ff0000", 500, 500)
                elif self.__secuencia[i] == "Amarillo":
                    self.cambioColorBoton(self.__botonAmarillo, "white", "#ffff00", 500, 500)
                elif self.__secuencia[i] == "Azul":
                    self.cambioColorBoton(self.__botonAzul, "white", "#0080ff", 500, 500)

                i += 1

# PARA AUMENTAR DIFICULTAD
                time.sleep(0.1)                 # Para que no vaya tan rápido, 1 segundo de diferencia en la animación de recorrer las posiciones.

            aleatorio = random.randrange(0, 4)  # Rango de 0 a 4. Dependiendo del número aleatorio es el botón que se va a encender.
            self.__secuencia.append(self.__colores[aleatorio]) 
            # Al arreglo que está guardando el número de los colores se le agrega un nuevo elemento de una posición random en el arreglo de colores.

            if self.__secuencia[i] == "Verde":    # Como es un nuevo botón y el usuario debe saber qué boton se iluminó
                self.cambioColorBoton(self.__botonVerde, "white", "#008080", 500, 500)
            elif self.__secuencia[i] == "Rojo":
                self.cambioColorBoton(self.__botonRojo, "white", "#ff0000", 500, 500)
            elif self.__secuencia[i] == "Amarillo":
                self.cambioColorBoton(self.__botonAmarillo, "white", "#ffff00", 500, 500)
            elif self.__secuencia[i] == "Azul":
                self.cambioColorBoton(self.__botonAzul, "white", "#0080ff", 500, 500)
            # Primero recorre todas las posiciones del arreglo y después agrega un nuevo color.

    def cambioColorBoton(self, boton, colorCambio, colorInicial, frecuencia, duracion):#Los últimos 2 parámetros sirven para el sonido al apretar un botón.
        boton.configure(bg=colorCambio)
        self.__ventana.update()               # Para actualizar el fondo porque hubo un cambio de color, y quiero mostrarlo.
        self.sonido(frecuencia, duracion)     # El beep suena al hacer el cambio de color.
        boton.configure(bg=colorInicial)      # Lo manda a su color original.
        self.__ventana.update()               # Se actualiza la ventana para ver ese cambio.
        

    def sonido(self, frecuencia, duracion):
        winsound.Beep(frecuencia, duracion)   # La frecuencia determina la tonalidad del sonido (si es alto o bajo), la duración, cuántos segundos durará.
    
    def cargarPuntajes(self):
        nombre = self.__nombreUsuario
        puntaje = self.__marcador
        fecha = self.__fecha

        datos = Jugador(nombre,puntaje,fecha,nivel="")
        self.__manejador.agregarJugador(datos)
        d = self.__manejador.toJSON()
        self.__encoder.guardarJSONArchivo(d,'pysimonpuntajes.json')

    def mostrarPuntajes(self):
        ventana_puntajes = Toplevel(self.__ventana)
        ventana_puntajes.title("Galería de puntajes")
        ventana_puntajes.geometry('400x300')

        # Etiqueta de título
        label_titulo = Label(ventana_puntajes, text="Puntajes de Jugadores", font=("Arial", 16))
        label_titulo.pack(pady=10)

        # Mostrar puntajes de cada jugador
        for jugador in self.__manejador.mostrarDatos():  # Suponiendo que tengas un método en Manejador para obtener la lista de jugadores
            label_jugador = Label(ventana_puntajes, text=f"{jugador.getNombre()} - Puntaje: {jugador.getPuntaje()}")
            label_jugador.pack()

        # Botón para cerrar la ventana
        boton_cerrar = Button(ventana_puntajes, text="Cerrar", command=ventana_puntajes.destroy)
        boton_cerrar.pack(pady=20)


if __name__ == '__main__':
    test = SimonDice()