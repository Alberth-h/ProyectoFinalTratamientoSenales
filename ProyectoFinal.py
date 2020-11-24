import sys 
from tkinter import *
from tkinter.filedialog import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

principal = Tk()
principal.title("Afinacion de guitarra")
principal.geometry("700x1000")

str5ta = StringVar()
str5ta.set("5ta(La) - 110 Hz")

strFrecuenciaActual_lbl = StringVar()
strFrecuenciaActual_lbl.set("Frecuencia Actual")

strFrecuenciaActual = StringVar()
strFrecuenciaActual.set("114.6 Hz")

strEstado = StringVar()
strEstado.set("<- Es necesario aflojar la cuerda")

def iniciar():
    lbl5ta = Label(principal, textvariable=str5ta)
    lbl5ta.pack()
    
    lblFrecuenciaActual_lbl = Label(principal, textvariable=strFrecuenciaActual_lbl)
    lblFrecuenciaActual_lbl.pack()

    lblFrecuenciaActual = Label(principal, textvariable=strFrecuenciaActual)
    lblFrecuenciaActual.pack()

    lblEstado = Label(principal, textvariable=strEstado)
    lblEstado.pack()

btnIniciar = Button(principal, text="Iniciar", command=iniciar)
btnIniciar.pack()

mainloop()