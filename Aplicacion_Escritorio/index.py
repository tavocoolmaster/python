#Importamos la biblioteca para crear la interfase de la aplicacion
from tkinter import ttk
from tkinter import * #traigo todos los elementos de la biblioteca

#imporamos el modulo de conexion con la base de datos Sqlite antes instalada
import sqlite3

class Productos:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Aplicación de Productos')

if __name__== '__main__':
    window = Tk()
    application=Productos(window)
    window.mainloop()
