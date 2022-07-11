#Importamos la biblioteca para crear la interfase de la aplicacion
from tkinter import ttk
from tkinter import * #traigo todos los elementos de la biblioteca

#importamos el modulo de conexion con la base de datos Sqlite antes instalada
import sqlite3


class Productos:
    
    #conectar la base de datos SQlite
    bdNombre='database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Aplicación de Productos')
        
        #creamos un contenedor
        frame=LabelFrame(self.wind, text ='Registrar un Nuevo Producto')
        frame.grid(row=0, column=0, columnspan=3, pady=10)

        #crear la caja de texto Nombre
        Label(frame, text='Nombre:').grid(row=1,column=0)
        self.nombre=Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row=1, column=1)

        #crear la caja de texto Precio
        Label(frame, text='Precio:').grid(row=2,column=0)
        self.precio=Entry(frame)
        self.precio.grid(row=2, column=1)

        #crear boton para guardar
        ttk.Button(frame,text='Guardar').grid(row=3,columnspan=2,sticky=W+E)#sticky establece el ancho del boton de oeste a este.

        #Crear una tabla 
        self.tabla=ttk.Treeview(height=10,columns=2)
        self.tabla.grid(row=4,column=0,columnspan=2)
        self.tabla.heading('#0',text='Nombre',anchor=CENTER)
        self.tabla.heading('#1',text='Precio',anchor=CENTER)

        #consultamos los datos de los productos para mostrar en la tabla
        self.Obtener_Productos()

    #creo una funcion que conecte a la base de datos mientras este en esta clase
    def Ejecutar_Consulta(self, Consulta, Parametros=()):
        with sqlite3.connect(self.bdNombre) as conn:
            cursor=conn.cursor()
            resultado=cursor.execute(Consulta,Parametros)
            conn.commit()
        return resultado

    def Obtener_Productos(self):
        #Limpiando la tabla
        registros=self.tabla.get_children()
        for elemento in registros:
            self.tabla.delete(elemento)
        #Consultando los datos
        Consulta='SELECT * FROM productos ORDER BY Nombre ASC'
        filas=self.Ejecutar_Consulta(Consulta)
        #llenando los datos
        for Fila in filas:
            print(Fila)

if __name__== '__main__':
    window = Tk()
    applicacion=Productos(window)
    window.mainloop()
