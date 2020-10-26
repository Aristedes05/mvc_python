import tkinter as tk
from tkinter import ttk
from vista.interfaz import Notebook_listado

class Aplicacion(ttk.Frame):

    def __init__(self,ventana_principal):
        super().__init__(ventana_principal)
        ventana_principal.title("Este es la ventana principal")
        ventana_principal.resizable(False,False)



    
ventana_principal = tk.Tk()
app = Aplicacion(ventana_principal)
app.mainloop()