from cgitb import text
import numbers
from string import whitespace
from tkinter import *
from tokenize import Number
from turtle import color

from setuptools import Command


def resu(): 
   

    if n1.get().isnumeric() and n2.get().isnumeric ():
        resultado['text'] = float(n1.get()) + float( n2.get())
    else:
        resultado['text'] = 'valor invalido'
    



#|================BACK-END===============================\

#+=======================================================

#|================FRONT-END===============================\

conta = Tk()

conta.geometry('600x600+100+300')
conta.maxsize(width=1000,height=1000)
conta.minsize(width=400, height=200)
conta.config(bg='#8A887B')



titulo = Label(conta, text= "CALCULO",font='Arial 40',bg ='#8A887B',foreground='white' )
titulo.place(x = 300 ,y=60)
linha = Label(conta, background='black')
linha.pack(ipadx=1000,pady =150)




text1 = Label(conta, text='Digite o primeiro numero:',font="Arial 20",bg='#8A887B',foreground='white')
text1.place(x=20,y=200)
n1 =  Entry(conta,font='Arial 15', foreground='#480C0D')
n1.place(y=240,x=20)

text2 = Label(conta, text='Digite o Segundo numero:',font="Arial 20",bg='#8A887B',foreground='white')
text2.place(x=20,y=280)
n2 =  Entry(conta,font='Arial 15', foreground='#480C0D')
n2.place(y=320,x=20)


botao = Button(conta,text='SOMA',background='#480C0D',foreground='white',font='Arial 40',command=resu)
botao.place(y=390 ,x=300)



resultado = Label(conta,text='resultado',background='#8A887B',foreground='#480C0D',font='Arial 40')
resultado.place(x=300,y=500)



conta.mainloop()