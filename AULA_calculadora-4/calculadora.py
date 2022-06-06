from cgitb import text
from tkinter import *





'''
def um():
   info['text'] +=  '1'

def dois():
   info['text'] +=  '2'

def tres():
   info['text'] +=  '3'

def quatro():
   info['text'] +=  '4'

def cinco():
   info['text'] += '5'

def seis():
   info['text'] += '6'

def sete():
   info['text'] += '7'

def oito():
   info['text'] += '8'

def nove():
   info['text'] +=  '9'

def zero():
   info['text'] += '0'
   '''


def dado(valor):
   info['text'] += valor
        

def clear():
    info['text'] = ''


''''
entrada = '1.21 + 3*4+10-11/79'
entrada_mod1 = entrada.replace('+',|).replace('-',|).replace('/',|).replace('*',|)
entradas_mod2 = entrada_mod1.split('|')
print(entrada)
print(entrada_mod1)
print(entrada_mod2)

'''

def resu():
   x = info['text']
   x_mod_1 = x.replace('+','|').replace('-','|').replace('*','|').replace('/','|')
   x_mod_2 = x_mod_1.split('|')

   c = 0


   for i in range(len(x_mod_2)):
      print (x_mod_2[i].replace('.','1',1).isnumeric())
      if not x_mod_2[i].replace('.','1',1).isnumeric():
         c = 1
      break


   if c == 0: 
      resu = eval(info['text'])  
      info['text'] = str(resu)
   else:
      info['text'] = 'Operação invalida.'


def delet():
   info['text'] = info['text'][:-1]


calc = Tk()
calc.geometry('600x600')
calc.config(bg='black')
calc.columnconfigure( 0,weight=1)
calc.columnconfigure( 1,weight=1)
calc.columnconfigure( 2,weight=1)
calc.columnconfigure( 3,weight=1)

calc.rowconfigure(0,weight=1)
calc.rowconfigure(1,weight=1)
calc.rowconfigure(2,weight=1)
calc.rowconfigure(3,weight=1)
calc.rowconfigure(4,weight=1)
calc.rowconfigure(5,weight=1)


corL = '#20BC19'
colorB = '#4D4640'

carcolor = '#262322'
#+==================================================================
#                  DADOS

info = Label(calc,text='',font='Arial 40',foreground=corL,background='black')
info.grid(column=0,row=0,columnspan=4)
#=================================================================
#========================================================================
#              LINHA 1

btn7 = Button(calc,text = '7',background=colorB,font='Arial 40',foreground=corL,command=lambda:dado('7'))
btn7.grid(column=0,row=1,sticky=NSEW)

btn8 = Button(calc,text = '8',background=colorB,font='Arial 40',foreground=corL,command=lambda:dado('8'))
btn8.grid(column=1,row=1,sticky=NSEW)

btn9 = Button(calc,text = '9',background=colorB,font='Arial 40',foreground=corL,command=lambda:dado('9'))
btn9.grid(column=2,row=1,sticky=NSEW)

mult = Button(calc,text='*',background=carcolor,font='Arial 40',foreground=corL,command=lambda:dado('*'))
mult.grid(column= 3,row= 1,sticky=NSEW)



#========================================================================
#              LINHA 2

btn4 = Button(calc,text = '4',background=colorB,font='Arial 40',foreground=corL,command=lambda:dado('4'))
btn4.grid(column=0,row=2,sticky=NSEW)

btn5 = Button(calc,text = '5',background=colorB,font='Arial 40',foreground=corL,command=lambda:dado('5'))
btn5.grid(column=1,row=2,sticky=NSEW)

btn6 = Button(calc,text= '6',background=colorB,font='Arial 40',foreground=corL,command=lambda:dado('6'))
btn6.grid(column=2,row=2,sticky=NSEW)

divi = Button(calc,text='/',background=carcolor,font='Arial 40',foreground=corL,command=lambda:dado('/'))
divi.grid(column= 3,row= 2,sticky=NSEW)
#========================================================================
#              LINHA 3

btn3 = Button(calc,text= '3',background=colorB,font='Arial 40',foreground=corL,command=lambda:dado('3'))
btn3.grid(column=0,row=3,sticky=NSEW)

btn2 = Button(calc,text= '2',background=colorB,font='Arial 40',foreground=corL,command=lambda:dado('2'))
btn2.grid(column=1,row=3,sticky=NSEW)


btn1 = Button(calc,text= '1',background=colorB,font='Arial 40',foreground=corL,command=lambda:dado('1'))
btn1.grid(column=2,row=3,sticky=NSEW)

soma = Button(calc,text='+',background=carcolor,font='Arial 40',foreground=corL,command=lambda:dado('+'))
soma.grid(column=3,row= 3,sticky=NSEW)

#========================================================================
#              LINHA 4



btn0 = Button(calc,text='0',background=colorB,font='Arial 40',foreground=corL,command=lambda:dado('0'))
btn0.grid(column=0,row=4,sticky=NSEW)
igu = Button(calc,text= '=',background=carcolor,font='Arial 40',foreground=corL,command=resu)
igu.grid(column=1,row=4,sticky=NSEW)
ponto = Button(calc,text='.',background=carcolor,font='Arial 40',foreground=corL,command=lambda:dado('.'))
ponto.grid(column=2,row=4,sticky=NSEW)

menos = Button(calc,text='-',background=carcolor,font='Arial 40',foreground=corL,command=lambda:dado('-'))
menos.grid(column=3,row=4,sticky=NSEW)

#===============================================================================

#+===============================================================================
#               LINHA 5

dell = Button(calc,text='DEL',background=carcolor,font='Arial 40',foreground=corL,command=delet)
dell.grid(column=0,row=5,sticky=NSEW)

c = Button(calc,text='C',background=carcolor,font='Arial 40',foreground=corL,command=clear)
c.grid(column=1,row=5,sticky=NSEW)
par1 = Button(calc,text='(',background=carcolor,font='Arial 40',foreground=corL,command=lambda:dado('('))
par1.grid(column=2,row=5,sticky=NSEW)
par2 = Button(calc,text=')',background=carcolor,font='Arial 40',foreground=corL,command=lambda:dado(')'))
par2.grid(column=3,row=5,sticky=NSEW)

#==================================================================================



calc.bind('0', lambda event:dado('0'))
calc.bind('1', lambda event:dado('1'))
calc.bind('2', lambda event:dado('2'))
calc.bind('3', lambda event:dado('3'))
calc.bind('4', lambda event:dado('4'))
calc.bind('5', lambda event:dado('5'))
calc.bind('6', lambda event:dado('6'))
calc.bind('7', lambda event:dado('7'))
calc.bind('8', lambda event:dado('8'))
calc.bind('9', lambda event:dado('9'))
calc.bind('*', lambda event:dado('*'))
calc.bind('+', lambda event:dado('+'))
calc.bind('-', lambda event:dado('-'))
calc.bind('/', lambda event:dado('/'))
calc.bind('.', lambda event:dado('.'))
calc.bind('(', lambda event:dado('('))
calc.bind(')', lambda event:dado(')'))
calc.bind('C', lambda event:clear())
calc.bind('<Return>', lambda event:resu())










'''''
[     ]
7 8 9 *
4 5 6 /
1 2 3 +
0 = . -
Del C ()

'''


calc.mainloop()
