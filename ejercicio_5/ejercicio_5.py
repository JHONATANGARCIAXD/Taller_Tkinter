

from cmath import pi
import math
from sre_constants import IN
from tkinter import *




# Ventana Principal

ventana_principal=Tk()

ventana_principal.title("AREA Y PERIMETRO")

ventana_principal.geometry("800x500")

ventana_principal.config(bg="black")



# Funciones

def Calcular():
    P=math.pi * int(N.get())
    P1= P * 2
    A=math.pi * int(N.get()) 
    A1= A * int(N.get())
  
    t_resultado.insert(INSERT," El area con radio de " + N.get() + " es igual a: " + str(A1) + " y el perimetro es igual a: "  + str(P1) + "\n") 






def Borrar():
    N.set("")
    t_resultado.delete("1.0" , "end")
    





# Variables 

N=StringVar()
P=StringVar()
A=StringVar()
P1=StringVar()
A1=StringVar()



# Frames

frame_pre=Frame(ventana_principal ,bg="black" ,width=780 , height=480)
frame_pre.place(x=10 , y=10)

frame_resul=Frame(frame_pre , bg="blue" , width=760 , height=60)
frame_resul.place(x=10 , y=390)


# Etiquetas

entry_1=Label(frame_pre , )
entry_1.config(bg="black" ,  fg="White" , text=" Valor del Radio: ", font=("Arial",15))
entry_1.place(x=240 , y=120)

# Entry

Valor_1=Entry(frame_pre , width=8, textvariable=N)
Valor_1.config(font=("Arial",20),justify=CENTER)
Valor_1.place(x=400 , y=120)


# Botones

btn_Cal=Button(frame_pre, width=8, text="Calcular" , command=Calcular)
btn_Cal.config(bg="Blue" , fg="White")
btn_Cal.place(x=558 , y=250)


btn_Bor=Button(frame_pre, width=8, text="Borrar" , command=Borrar)
btn_Bor.config(bg="Blue" , fg="White")
btn_Bor.place(x=117, y=250)


# Area de texto para resultado
t_resultado= Text(frame_resul, width=69 , height=2)
t_resultado.config(bg="Black" , fg="White", font=("Arial" , 15))
t_resultado.pack()


# Mainloop

ventana_principal.mainloop()