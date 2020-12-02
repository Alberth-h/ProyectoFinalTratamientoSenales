from tkinter import *
import numpy as np
import pyaudio
import wave
from PIL import ImageTk, Image
import time

#ventana
ventana = Tk()
ventana.geometry("700x1000")
ventana.title("Pan con lechita")

#variablas str
strAfinacion= StringVar()
strAviso = StringVar()
strFrec= StringVar()

#Formato de audio de microfono
PROFUNDIDAD_BITS = pyaudio.paInt16
CANALES = 1
FRECUENCIA_MUESTREO = 44100
SEGUNDOS_GRABACION= 3

#Tamamaño de CHUNK
CHUNK = 2048

window= np.blackman(CHUNK)

#Funcion de inicio
def inicio():

    #Funcion de analisis
    def analisis(stream):
        data = stream.read(CHUNK, exception_on_overflow=False)
        waveData = wave.struct.unpack("%dh"%(CHUNK),data )
        npData = np.array(waveData)
        dataEntrada = npData * window
        fftData = np.abs(np.fft.rfft(dataEntrada))

        indiceFrecuenciaDominante = fftData[1:].argmax() + 1
        
        y0, y1, y2 = np.log(fftData[indiceFrecuenciaDominante-1: indiceFrecuenciaDominante+2])
        x1 = (y2 - y0) * 0.5 / (2 * y1 - y2 -y0)
        frecuenciaDominante = (indiceFrecuenciaDominante+x1)*FRECUENCIA_MUESTREO/CHUNK
        freq = str(frecuenciaDominante)
        
        strFrec.set(freq)

        margen = 20
        margenAfin= 2.0

        #6ta Mi
        if frecuenciaDominante > 82.4 - margen and frecuenciaDominante < 82.4 + margen:
            Aviso= "6ta Mi - Frecuencia de 82.4 Hz"
            if frecuenciaDominante >82.4 - margenAfin and frecuenciaDominante < 82.4 + margenAfin:
                Afinacion = "Afinacion correcta"
            elif frecuenciaDominante < 82.4 + margenAfin:
                Afinacion = "Es necesario apretar la cuerda"
            else:
                Afinacion = "Es necesario aflojar la cuerda"

        #5ta La
        elif frecuenciaDominante > 110.0 - margen and frecuenciaDominante < 110.0 + margen:
            Aviso= "5ta La - Frecuencia de 110.0 Hz"
            if frecuenciaDominante >110.0 - margenAfin and frecuenciaDominante < 110.0 + margenAfin:
                Afinacion = "Afinacion correcta"
            elif frecuenciaDominante < 110.0 + margenAfin:
                Afinacion = "Es necesario apretar la cuerda"
            else:
                Afinacion = "Es necesario aflojar la cuerda"

        #4ta Re
        elif frecuenciaDominante > 146.83 - margen and frecuenciaDominante < 146.83 + margen:
            Aviso= "4ta Re - Frecuencia de 146.83 Hz"
            if frecuenciaDominante >146.83 - margenAfin and frecuenciaDominante < 146.83 + margenAfin:
                Afinacion = "Afinacion correcta"
            elif frecuenciaDominante < 146.83 + margenAfin:
                Afinacion = "Es necesario apretar la cuerda"
            else:
                Afinacion = "Es necesario aflojar la cuerda"
        
        #3ta Sol
        elif frecuenciaDominante > 196.0 - margen and frecuenciaDominante < 196.0 + margen:
            Aviso= "3ra Sol - Frecuencia de 196.0 Hz"
            if frecuenciaDominante >196.0 - margenAfin and frecuenciaDominante < 196.0 + margenAfin:
                Afinacion = "Afinacion correcta"
            elif frecuenciaDominante < 196.0 + margenAfin:
                Afinacion = "Es necesario apretar la cuerda"
            else:
                Afinacion = "Es necesario aflojar la cuerda"

        #2ta Si
        elif frecuenciaDominante > 246.94- margen and frecuenciaDominante < 246.94 + margen:
            Aviso= "2da Si - Frecuencia de 246.94 Hz"
            if frecuenciaDominante >246.94 - margenAfin and frecuenciaDominante < 246.94 + margenAfin:
                Afinacion = "Afinacion correcta"
            elif frecuenciaDominante < 246.94 + margenAfin:
                Afinacion = "Es necesario apretar la cuerda"
            else:
                Afinacion = "Es necesario aflojar la cuerda"

        #1ta Mi
        elif frecuenciaDominante > 329.63 - margen and frecuenciaDominante < 329.63  + margen:
            Aviso= "1ra Mi - Frecuencia de 329.63 Hz"
            if frecuenciaDominante >329.63  - margenAfin and frecuenciaDominante < 329.63  + margenAfin:
                Afinacion = "Afinacion correcta"
            elif frecuenciaDominante < 329.63  + margenAfin:
                Afinacion = "Es necesario apretar la cuerda"
            else:
                Afinacion = "Es necesario aflojar la cuerda"
        
        #En caso de que no se reconozca
        else:
            Aviso = "Volver a intentar"
            Afinacion = "No se reconoce la frecuencia"

        strAviso.set(Aviso)
        strAfinacion.set(Afinacion)

    if __name__=="__main__":
   
        p = pyaudio.PyAudio()
        stream = p.open(format=PROFUNDIDAD_BITS, channels=CANALES, rate=FRECUENCIA_MUESTREO, input=True, frames_per_buffer=CHUNK)
        
        for i in range(0, int(FRECUENCIA_MUESTREO * SEGUNDOS_GRABACION / CHUNK)):
            analisis(stream)

        stream.stop_stream()
        stream.close()
        p.terminate()

        
lbl1 = Label(ventana, text="El afinador")
lbl1.pack()

lbl2 = Label(ventana, textvariable=strAviso)
lbl2.pack()

lbl3 = Label(ventana, textvariable=strFrec)
lbl3.pack()

lbl4 = Label(ventana,textvariable=strAfinacion)
lbl4.pack()

boton = Button(ventana, text="Escuchar", command=inicio)
boton.pack()

#img = ImageTk.PhotoImage(Image.open("walter.gif"))
#panel = Label(ventana, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")

frames = [PhotoImage(file='walter.gif',format = 'gif -index %i' %(i)) for i in range(25)] 

def update(ind): 
    frame = frames[ind] 
    ind += 1 
    label.configure(image=frame) 
    ventana.after(25, update, ind)

label = Label(ventana) 
label.pack() 
ventana.after(0, update, 0) 

ventana.mainloop()