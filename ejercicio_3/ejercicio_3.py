from tkinter import *
from tokenize import String


# Ventana Principal

ventana_principal=Tk()

ventana_principal.title("IVA")

ventana_principal.geometry("800x500")

ventana_principal.config(bg="black")

ventana_principal.resizable(0,0)



# Funciones

def Calcular():
     E=int(N.get()) % 10
     E1=int(N.get())//10
     E2=(E*1000)
     I=(E1 % 10)
     I1=(E1 // 10)
     I2=(I * 100)
     O=(I1 % 10)
     O1=(I1 // 10)
     O2=(O * 10)

     z=E2 + I2 + O2 + O1

     t_resultado.insert(INSERT,"El número " + N.get() + " de forma inversa es " + str(z) + "\n")


    


                                                                                                        
def Borrar():
   

    t_resultado.delete("1.0" , "end")
    







# Variables 

N=StringVar()

E=StringVar()
E1=StringVar()
E2=StringVar()

I=StringVar()
I1=StringVar()
I2=StringVar()

O=StringVar()
S=StringVar()
O2=StringVar()

Z=StringVar()




# Frames

frame_pre=Frame(ventana_principal ,bg="black" ,width=780 , height=480)
frame_pre.place(x=10 , y=10)

frame_resul=Frame(frame_pre , bg="blue" , width=760 , height=60)
frame_resul.place(x=10 , y=390)


# Etiquetas

entry_1=Label(frame_pre , )
entry_1.config(bg="black" ,  fg="White" , text=" Ingrese Un Número De Cuatro Digitos: ", font=("Arial",15))
entry_1.place(x=120 , y=120)

# Entry

Valor_1=Entry(frame_pre , width=4 , textvariable=N)
Valor_1.config(font=("Arial",20),justify=CENTER)
Valor_1.place(x=558 , y=115)


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