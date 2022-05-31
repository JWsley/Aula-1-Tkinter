from cgitb import text
from tkinter import *


def subt():
    number['text'] = int(number['text'])-1
    if number['text'] < -10:
        number['text'] ='Passou de -10'
    else:
        pass
    


def soma():
    number['text'] = int(number['text'])+1
    if number['text'] > 10:
        number['text'] ='Passou de 10'
    else:
        pass

def reset():
    number['text'] = 0




#=====================================================


app = Tk()
app.geometry('500x300')
app.config(bg='#7B8285')
app.title('Soma_sub')
app.grid_columnconfigure(1,weight=1)
app.grid_columnconfigure(2,weight=1)
app.grid_columnconfigure(3,weight=1)

app.bind('-',lambda event: diminuir ())
app.bind('+',lambda event: aumentar ())

app.grid_rowconfigure(1, weight=1)


#===================Grid das margens===========
app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(4,weight=1)
app.grid_rowconfigure(0,weight=1)


#====================BACK_END========================
#-------------------------------------------------------
#===================Front_end========================

titulo = Label(app, text='SOMA/SUB',background='#7B8285',foreground='#6e2c29',font='Arial 40')
titulo.grid(row=0,column=2, sticky=NSEW)


botao1 = Button(app,text='-',foreground='white',background='black',font='Arial 40',command=subt)
botao1.grid(row=1,column=1, sticky=NSEW)

number = Label(app, text='0',background='#7B8285',foreground='white',font='Arial 40')
number.grid(row=1,column=2, sticky=NSEW)

botao2 = Button(app,text='+',foreground='white',background='black',font='Arial 40',command=soma)
botao2.grid(row=1,column=3, sticky=NSEW)

botao3 = Button(app,text='Reset',foreground='white',background='black',font='Arial 40',command=reset)
botao3.grid(row=4,column=2, sticky=NSEW)







margin1 = Label(app,background='#7B8285').grid(column=0,stick=NS)
margin2 = Label(app,background='#7B8285').grid(column=4,stick=NS)


app.mainloop()