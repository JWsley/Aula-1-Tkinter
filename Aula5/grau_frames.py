from tkinter import *
from turtle import back
 
 
grau =  Tk()
grau.geometry('400x400')
grau.columnconfigure(0, weight=1)
grau.columnconfigure(1, weight=1)
grau.rowconfigure(0,weight=1)
grau.rowconfigure(1,weight=1)


fc1 ='#CEF2E5'
fc2 = '#2E2D22'

fr1  = Frame(grau,background=fc1)
fr2  = Frame(grau,background=fc2)

fr1.pack()
fr2.pack()




def fah():
    resu['text']  = (float(entrada.get()) * 1.8) + 32
# F = C*1.8 + 32
#+===============Back end======
#==========================================
#=================FRONT END

#

celsio = Label(fr1,text='C°:',font='Arial 25',background=fc1)

celsio.grid(row=0,column=0)

entrada = Entry(fr1,font='40')

entrada.grid(row=0,column=1)

botao = Button(fr2,text = 'Converter °F',font='40',bg=fc2,fg='white',command=fah)

botao.grid(row=1,column=0)

resu= Label(fr2,text='0',font='40',bg=fc2,foreground='white')

resu.grid(row=1,column=1)

grau.mainloop()
