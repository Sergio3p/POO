import tkinter as tk
from tkinter import *
from tkinter import ttk, simpledialog, messagebox,font
import random
import time
import winsound
import json
from functools import partial
from datetime import datetime

from claseJugador import Jugador  # Importa la clase Jugador desde claseJugador.py
from claseObjectEncoder import ObjectEncoder  # Importa el ObjectEncoder para JSON
from manejadorJSON import Manejador  # Importa el Manejador para los puntajes

class SimonDice:
    def __init__(self):
        self.__ventana = tk.Tk()
        self.__secuencia = []
        self.__marcador = 0
        self.__puntajeRecord = 0
        self.__contador = 0
        self.__juegoInicial = False
        self.__colores = ["Verde", "Rojo", "Amarillo", "Azul"]
        self.__ventana.title("Simón Dice")
        self.__nombreUsuario = simpledialog.askstring("Nombre", "Ingrese su nombre:")
        self.barraOpciones()
        self.elegirDificultad()
        self.canvas = tk.Canvas(self.__ventana, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        #TEMPORIZADOR
        self.__timer = None                                                     
        self.__nivel = None  # Variable para almacenar el nivel seleccionado                
        self.__tiempoRestante = 15

        self.__encoder = ObjectEncoder()
        self.__manejador = Manejador()
        self.leerPuntajes()

        self.__presionado = False
        self.barraOpciones()
        self.iniciarBotones()

        #self.crearControlesNivel()
        #self.crearControlesNivel()  # Agregar controles para seleccionar el nivel
        self.__ventana.configure(background="#f0f0f0")
        self.__ventana.mainloop()
   
   #BOTONES
   
    def crear_boton_canvas(self, x, y, width, height, color, text, command):
        button = self.canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline="")
        button_text = self.canvas.create_text(x + width / 2, y + height / 2, text=text, fill="white")
        
        self.canvas.tag_bind(button, "<Enter>", partial(self.on_enter, button))
        self.canvas.tag_bind(button_text, "<Enter>", partial(self.on_enter, button))
        self.canvas.tag_bind(button, "<Leave>", partial(self.on_leave, button))
        self.canvas.tag_bind(button_text, "<Leave>", partial(self.on_leave, button))
        self.canvas.tag_bind(button, "<Button-1>", command)
        self.canvas.tag_bind(button_text, "<Button-1>", command)
        
        return button, button_text

    def on_enter(self, button, event):
        self.canvas.itemconfig(button, outline="black")

    def on_leave(self, button, event):
        self.canvas.itemconfig(button, outline="")

    def iniciarBotones(self):
        self.__ventana.update_idletasks()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        width = 0.4 * canvas_width
        height = 0.4 * canvas_height
        
        # Centrar botones
        x1, y1 = (0.1 * canvas_width, 0.1 * canvas_height)
        x2, y1 = (0.55 * canvas_width, 0.1 * canvas_height)
        x1, y2 = (0.1 * canvas_width, 0.55 * canvas_height)
        x2, y2 = (0.55 * canvas_width, 0.55 * canvas_height)

        self.__botonVerde, self.__textoVerde = self.crear_boton_canvas(x1, y1, width, height, "#008080", "Verde", partial(self.presionar, "Verde"))
        self.__botonRojo, self.__textoRojo = self.crear_boton_canvas(x2, y1, width, height, "#ff0000", "Rojo", partial(self.presionar, "Rojo"))
        self.__botonAmarillo, self.__textoAmarillo = self.crear_boton_canvas(x1, y2, width, height, "#ffff00", "Amarillo", partial(self.presionar, "Amarillo"))
        self.__botonAzul, self.__textoAzul = self.crear_boton_canvas(x2, y2, width, height, "#0080ff", "Azul", partial(self.presionar, "Azul"))
        
        self.__botonIniciar = tk.Button(self.__ventana, command=self.iniciar, bg="white", text="INICIAR", font=("Comic Sans MS", 10))
        self.__botonIniciar.place(relx=0.505, rely=0.46, relheight=0.1, relwidth=0.2, anchor=tk.N)
        self.__etiqueta = tk.Label(self.__ventana, text="\nMarcador: 0\nMayor puntaje: 0", font=("Comic Sans MS", 10))       
        self.__etiqueta.pack()
    def barraOpciones(self):
        barra_menu = Menu(self.__ventana)
        
        archivo_menu = Menu(barra_menu, tearoff=0)
        archivo_menu.add_command(label="ver puntajes", command=self.mostrarPuntajes)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.__ventana.quit)
        barra_menu.add_cascade(label="Puntajes", menu=archivo_menu)
        
        ayuda_menu = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)
        
        self.__ventana.config(menu=barra_menu)

    def presionar(self, color, event=None):
        if not self.__presionado and self.__juegoInicial:
            self.__presionado = True
            if len(self.__secuencia) >= self.__contador - 1:
                if self.__secuencia[self.__contador] == color:
                    self.__contador += 1
                    if color == "Verde":
                        self.sonido(600, 500)
                    elif color == "Rojo":
                        self.sonido(500, 500)
                    elif color == "Amarillo":
                        self.sonido(700, 500)
                    elif color == "Azul":
                        self.sonido(800, 500)
                    self.revisarTurno()
                else:
                    self.finalizar()
            self.__presionado = False
        if self.__nivel != "Principiante":        
            self.__tiempoRestante = 15

    def finalizar(self):
        self.pausar_temporizador()
        self.__tiempoRestante = 15
        if self.__marcador > self.__puntajeRecord:
            self.__puntajeRecord = self.__marcador

        self.__ventanaPerdiste = tk.Toplevel(self.__ventana)
        self.__ventanaPerdiste.title("Perdiste")
        self.__ventanaPerdiste.geometry('300x150')
        label = tk.Label(self.__ventanaPerdiste, text=f"\nPuntaje: {self.__marcador}")
        label.pack(pady=10)

        boton_reiniciar = ttk.Button(self.__ventanaPerdiste, text="REINICIAR JUEGO", command=self.reiniciarJuego)
        boton_reiniciar.pack(side=tk.LEFT, padx=20, pady=20)
        boton_salir = ttk.Button(self.__ventanaPerdiste, text='SALIR', command=self.__ventana.quit)
        boton_salir.pack(side=tk.RIGHT, padx=20, pady=20)
        self.cargarPuntajes()

    def reiniciarJuego(self):
        self.__juegoInicial = False
        self.__ventanaPerdiste.destroy()
        self.__nombreUsuario = simpledialog.askstring("Nombre", "Ingrese su nombre:")
        self.elegirDificultad()
        self.__botonIniciar.after(1600, self.iniciar)
        
    def iniciar(self):
        self.__contador = 0
        self.__marcador = 0
        self.__secuencia = []
        self.__juegoInicial = True
        self.__etiqueta.config(text=f"\nMarcador: {self.__marcador}\nMayor puntaje: {self.__puntajeRecord}")
        self.__botonIniciar.destroy()
        self.crearColor()

    def revisarTurno(self):
        if len(self.__secuencia) == self.__contador:
            self.__contador = 0
            self.__marcador += 1
            self.__etiqueta.config(text=f"\nMarcador: {self.__marcador}\nMayor puntaje: {self.__puntajeRecord}")
            self.__botonIniciar.after(1000, self.crearColor)

    def crearColor(self):
        self.pausar_temporizador()
        if self.__juegoInicial:
            if self.__nivel == "Super Experto":
                aleatorio1 = random.randrange(0, 4)
                aleatorio2 = random.randrange(0, 4)
                self.__secuencia.append(self.__colores[aleatorio1])
                self.__secuencia.append(self.__colores[aleatorio2])
            else:
                aleatorio = random.randrange(0, 4)
                self.__secuencia.append(self.__colores[aleatorio])
            
            self.mostrarSecuencia()
        

    def mostrarSecuencia(self):
        for i, color in enumerate(self.__secuencia):
            self.__ventana.after(i * 600, self.resaltarColor, color)
        self.__ventana.after(len(self.__secuencia) * 600, self.reanudar_temporizador)
        

    def resaltarColor(self, color):
        if color == "Verde":
            self.cambioColorBoton(self.__botonVerde, "white", "#008080", 300, 300)
        elif color == "Rojo":
            self.cambioColorBoton(self.__botonRojo, "white", "#ff0000", 300, 300)
        elif color == "Amarillo":
            self.cambioColorBoton(self.__botonAmarillo, "white", "#ffff00", 300, 300)
        elif color == "Azul":
            self.cambioColorBoton(self.__botonAzul, "white", "#0080ff", 300, 300)

    def cambioColorBoton(self, boton, color_inicial, color_final, tiempo_inicial, tiempo_final):
        self.canvas.itemconfig(boton, fill=color_inicial)
        self.__ventana.after(tiempo_inicial, lambda: self.canvas.itemconfig(boton, fill=color_final))
        self.__ventana.update()

    def sonido(self, frecuencia, duracion):
        winsound.Beep(frecuencia, duracion)

    def mostrarPuntajes(self):
    # Crear la ventana de puntajes
        fuente = font.Font(font='Verdana 10', weight='normal')
        ventana_puntajes = tk.Toplevel(self.__ventana)
        ventana_puntajes.title("Puntajes de Jugadores")
        ventana_puntajes.geometry('600x300')

        # Crear un LabelFrame para contener los puntajes
        labelFramePuntajes = tk.LabelFrame(ventana_puntajes, text='Galería de puntajes:', font=fuente, borderwidth=2, relief='raised', padx=5, pady=5)
        labelFramePuntajes.pack(fill="both", expand="yes", padx=10, pady=10)

        # Crear un Treeview para mostrar los puntajes
        tree = ttk.Treeview(labelFramePuntajes, columns=("Nombre", "Puntaje", "Fecha", "Hora", "Nivel"), show='headings')
        tree.heading("Nombre", text="Nombre")
        tree.heading("Puntaje", text="Puntaje")
        tree.heading("Fecha", text="Fecha")
        tree.heading("Hora", text="Hora")
        tree.heading("Nivel", text="Nivel")

        # Configurar el ancho de las columnas
        tree.column("Nombre", width=50)
        tree.column("Puntaje", width=50)
        tree.column("Fecha", width=50)
        tree.column("Hora", width=50)
        tree.column("Nivel", width=50)
        tree.pack(fill="both", expand=True)

        # Agregar los puntajes al Treeview
        for jugador in self.__manejador.mostrarJugador():
            nombre = jugador.getNombre()
            puntaje = jugador.getPuntaje()
            fecha = jugador.getFecha().strftime('%Y-%m-%d')
            hora = jugador.getHora().strftime('%H:%M:%S')
            nivel = jugador.getNivel()
            tree.insert("", tk.END, values=(nombre,puntaje, fecha,hora,nivel))

        # Botón para cerrar la ventana
        boton_cerrar = tk.Button(ventana_puntajes, text="Cerrar", command=ventana_puntajes.destroy)
        boton_cerrar.pack(pady=20)

    def leerPuntajes(self):
        try:
            diccionario = self.__encoder.leerJSONArchivo('pysimonpuntajes.json')
            self.__manejador = self.__encoder.decodificarDiccionario(diccionario)
        except FileNotFoundError:
            pass  # Manejar el caso donde el archivo no existe


    def cargarPuntajes(self):
        nombre = self.__nombreUsuario
        puntaje = self.__marcador
        nivel = self.__nivel
        fecha = datetime.now()
        hora = datetime.now()

        datos = Jugador(nombre,puntaje,fecha,hora,nivel)
        self.__manejador.agregarJugador(datos)
        d = self.__manejador.toJSON()
        self.__encoder.guardarJSONArchivo(d,'pysimonpuntajes.json')

    def elegirDificultad(self):
        ventanaElegirDificultad = tk.Toplevel()
        ventanaElegirDificultad.title("Elegir dificultad")
        ventanaElegirDificultad.geometry('400x200')  # Ajustar el tamaño de la ventana

        label = tk.Label(ventanaElegirDificultad, text="Seleccione una dificultad:", font=("Comic Sans MS", 10))
        label.place(relx=0.5, rely=0.17, anchor=tk.CENTER)
        labelFrameSeleccione = ttk.LabelFrame(ventanaElegirDificultad, text='Elija una opción', borderwidth=2, relief='raised', padding=5)
        labelFrameSeleccione.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Lista de opciones para el OptionMenu
        opciones = ['Dificultad', 'Principiante', 'Experto', 'Super Experto']

        # Variable para almacenar la opción seleccionada
        opcionSeleccionada = tk.StringVar(ventanaElegirDificultad)
        opcionSeleccionada.set(opciones[0])                       # Opción por defecto, no se puede elegir.
        opcionMenu = ttk.OptionMenu(labelFrameSeleccione, opcionSeleccionada, *opciones)
        opcionMenu.pack(padx=20, pady=10)
        botonConfirmar = ttk.Button(ventanaElegirDificultad, text="Confirmar", command=partial(self.confirmarDificultad, ventanaElegirDificultad, opcionSeleccionada))
        botonConfirmar.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

        self.centrarVentana(ventanaElegirDificultad)
        ventanaElegirDificultad.resizable(False, False)

    def centrarVentana(self, ventana):
        ventana.update_idletasks()  # Asegura que las dimensiones de la ventana son correctas.
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)       # División entera.
        ventana.geometry(f'{ancho}x{alto}+{x}+{y}') 

    def confirmarDificultad(self, ventanaElegirDificultad, opcion):
        dificultad = opcion.get()
        self.__nivel = dificultad        
        ventanaElegirDificultad.destroy()
        self.__ventana.deiconify()

    #TEMPORIZADOR

    def iniciar_temporizador(self):
        self.__tiempoRestante = 15
        self.actualizar_temporizador()

    def actualizar_temporizador(self):
        if self.__tiempoRestante > 0 and self.__juegoInicial and not self.__pausado:    # Si no está pausado.
            print("Tiempo restante: " + str(self.__tiempoRestante))
            self.__tiempoRestante -= 1
            #self.__labTimer.config(text=f"Tiempo restante: {self.__tiempoRestante}")
            self.__ventana.after(1000, self.actualizar_temporizador)                   # Actualiza el temporizador después de 1 segundo.
       
        elif self.__pausado:            # Si está pausado.
            self.__tiempoRestante = 15

        elif self.__tiempoRestante == 0:
            self.finalizar()

    # Función para pausar el temporizador - FUNCIONA.
    def pausar_temporizador(self):
        self.__pausado = True
        print("Temporizador pausado")

    # Función para reanudar el temporizador
    def reanudar_temporizador(self):
        self.__pausado = False
        self.iniciar_temporizador()


if __name__ == "__main__":
    SimonDice()
