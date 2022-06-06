from tkinter import *
from turtle import bgcolor, left, right


imc = Tk()
imc.geometry('800x800')
imc.columnconfigure(0, weight=1)
imc.columnconfigure(1, weight=1)

imc.rowconfigure(0,weight=1)
imc.rowconfigure(1,weight=1)
imc.rowconfigure(2,weight=1)
imc.rowconfigure(3,weight=1)
imc.rowconfigure(4,weight=1)
imc.rowconfigure(5,weight=1)


colorf1 = '#EBEDFF'

colorf2 = '#2C1F2E'


fr1 = Frame(imc,bg=colorf1)
fr1.pack(side=LEFT)


fr2 = Frame(imc,bg = colorf2)
fr2.pack(side=LEFT)

#



def imC():

    res['text'] = x = float( p.get() )/ ( float(alt.get())* float(alt.get()))
   
    if x > 18.5 and x < 25:
        saud['text'] = 'Saudavel'
    else:
        pass

    if x > 25:
        saud['text'] = 'Sobre peso'
    else:
        pass


    if x < 18.5:
        saud['text'] = 'Magro'


def reset():
    saud['text'] = 'você esta...'
    res['text'] = 'resultado'


#========================BACK END=================================
#=========================FRONT END=================================
peso = Label(fr1 ,text ='Peso:',foreground = 'black',background = colorf1,font= 'Arial 25')
peso.grid(column =0,row = 0,sticky=NSEW)

p = Entry(fr1,font='40')
p.grid(row = 0,column = 1,sticky=NSEW)


altura= Label(fr1 ,text ='Altura:',foreground = 'black',background= colorf1,font= 'Arial 25')
altura.grid(column =0,row = 1,sticky=NSEW)

alt = Entry(fr1,font='40')
alt.grid(row = 1,column = 1,sticky=NSEW)

botao = Button(fr2,text='IMC',foreground='white',bg=colorf2,font='Arial 10',command=imC)
botao.grid(row=2,column=1,sticky=NSEW)


res = Label(fr2,text='resultado',bg=colorf2,font='Arial 25',fg='white' )
res.grid(row= 3,column=1,sticky=NSEW)

saud = Label(fr2,text='você esta...',bg=colorf2,font='Arial 25',fg='white' )
saud.grid(row= 4,column=1,sticky=NSEW)


reset = Button(fr2,text='Reset',background=colorf2,foreground='white',font='Arial 10',command=reset)
reset.grid(column = 1,row= 5,sticky = NSEW)


imc.mainloop()
