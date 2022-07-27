from tkinter import *
import math

# Ventana Principal

ventana_principal=Tk()

ventana_principal.title("IVA")

ventana_principal.geometry("800x500")

ventana_principal.config(bg="black")



# Funciones

def Calcular():
    z=pow(int(n.get()) , 1/int(x.get()))
    t_resultado.insert(INSERT, " La raiz de  " + n.get() + " Con Indice de  " + x.get()  + " Es igual a  " + str(z)  + "\n")

def Borrar():
    n.set("")
    x.set("")
    t_resultado.delete("1.0" , "end")
    







# Variables 

n=StringVar()
x=StringVar()
z=StringVar()

# Frames

frame_pre=Frame(ventana_principal ,bg="black" ,width=780 , height=480)
frame_pre.place(x=10 , y=10)

frame_resul=Frame(frame_pre , bg="blue" , width=760 , height=60)
frame_resul.place(x=10 , y=390)


# Etiquetas

entry_1=Label(frame_pre , )
entry_1.config(bg="black" ,  fg="White" , text="Valor del Radicando ", font=("Arial",15))
entry_1.place(x=240 , y=120)

entry_1=Label(frame_pre , )
entry_1.config(bg="black" ,  fg="White" , text="Valor del Indice ", font=("Arial",15))
entry_1.place(x=240 , y=180)




# Entry

Valor_1=Entry(frame_pre , width=9 , textvariable=n)
Valor_1.config(font=("Arial",20),justify=CENTER)
Valor_1.place(x=450, y=120)

Valor_2=Entry(frame_pre , width=9 , textvariable=x)
Valor_2.config(font=("Arial",20),justify=CENTER)
Valor_2.place(x=450, y=180)

# Botones

btn_Cal=Button(frame_pre, width=8, text="Calcular" , command=Calcular)
btn_Cal.config(bg="Blue")
btn_Cal.place(x=558 , y=250)


btn_Bor=Button(frame_pre, width=8, text="Borrar" , command=Borrar)
btn_Bor.config(bg="Blue")
btn_Bor.place(x=117, y=250)


# Area de texto para resultado
t_resultado= Text(frame_resul, width=52 , height=2)
t_resultado.config(bg="blue" , fg="White", font=("Arial" , 20))
t_resultado.pack()


# Mainloop

ventana_principal.mainloop()