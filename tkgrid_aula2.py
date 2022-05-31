from sqlite3 import Row
from tkinter import *



janela = Tk()
janela.geometry('500x600')
janela.title('Grid testes')
janela.config(bg='#7B8285')
janela.grid_rowconfigure(0,weight=1)
janela.grid_rowconfigure(1,weight=1)
janela.grid_rowconfigure(2,weight=1)
janela.grid_columnconfigure(0,weight=1)
janela.grid_columnconfigure(1,weight=1)
janela.grid_columnconfigure(2,weight=1)
##




btn1 = Button(janela,text='1',background = 'black' , foreground='white',font='Arial 50')
btn2 = Button(janela,text='2',background = 'black' , foreground='white',font='Arial 50')
btn3 = Button(janela,text='3',background = 'black' , foreground='white',font='Arial 50')
btn4 = Button(janela,text='4',background = 'black' , foreground='white',font='Arial 50')
btn5 = Button(janela,text='5',background = 'black' , foreground='white',font='Arial 50')
btn6 = Button(janela,text='6',background = 'black' , foreground='white',font='Arial 50')
btn7 = Button(janela,text='7',background = 'black' , foreground='white',font='Arial 50')
btn8 = Button(janela,text='8',background = 'black' , foreground='white',font='Arial 50')
btn9 = Button(janela,text='9',background = 'black' , foreground='white',font='Arial 50')





btn1.grid(row=0,column=0, sticky=NSEW)
btn2.grid(row=0,column=1, sticky=NSEW)
btn3.grid(row=0,column=2, sticky=NSEW)
btn4.grid(row=1,column=0, sticky=NSEW)
btn5.grid(row=1,column=1, sticky=NSEW)
btn6.grid(row=1,column=2, sticky=NSEW)
btn7.grid(row=2,column=0, sticky=NSEW)
btn8.grid(row=2,column=1, sticky=NSEW)
btn9.grid(row=2,column=2, sticky=NSEW)
janela.mainloop()

























