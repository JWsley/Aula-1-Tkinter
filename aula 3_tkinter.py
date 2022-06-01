from tkinter import *




def imcc():
    imc = Tk()
    imc.geometry('800x800')
    imc.rowconfigure(0, weight=1)
    imc.rowconfigure(1, weight=1)
    imc.rowconfigure(2, weight=1)
    imc.rowconfigure(3, weight=1)
    imc.rowconfigure(4, weight=1)
    
    
    
    imc.columnconfigure(0,weight=1)
    imc.columnconfigure(1,weight=1)
    imc.columnconfigure(2,weight=1)


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




    #========================BACK END================================#
    #=========================FRONT END=================================
    peso = Label(imc ,text ='Peso:',foreground = 'black',font= 'Arial 25')
    peso.grid(column =0,row = 0,sticky=NSEW)

    p = Entry(imc,font='40')
    p.grid(row = 0,column = 1,sticky=NSEW)


    altura= Label(imc ,text ='Altura:',foreground = 'black',font= 'Arial 25')
    altura.grid(column =0,row = 1,sticky=NSEW)

    alt = Entry(imc,font='40')
    alt.grid(row = 1,column = 1,sticky=NSEW)

    botao = Button(imc,text='IMC',foreground='black',command=imC)
    botao.grid(row=2,column=1,sticky=NSEW)


    res = Label(imc,text='resultado',font='Arial 25' )
    res.grid(row= 3,column=1,sticky=NSEW)

    saud = Label(imc,text='você esta...',font='Arial 25' )
    saud.grid(row= 4,column=1,sticky=NSEW)




    imc.mainloop()





#=======================    FAHRENHEIT  ==================================

def fahren():
    grau =  Tk()
    grau.geometry('400x400')
    grau.columnconfigure(0, weight=1)
    grau.columnconfigure(1, weight=1)


    grau.rowconfigure(0,weight=1)
    grau.rowconfigure(1,weight=1)



    def fah():
        resu['text']  = (float(entrada.get()) * 1.8) + 32



    # F = C*1.8 + 32
    #+===============Back end======
    #==========================================
    #=================FRONT END
    celsio = Label(grau,text='C°:',font='Arial 25')
    celsio.grid(row=0,column=0)


    entrada = Entry(grau,font='40')
    entrada.grid(row=0,column=1)

    botao = Button(grau,text = 'Converter °F',font='40',command=fah)
    botao.grid(row=1,column=0)


    resu= Label(grau,text='0',font='40')
    resu.grid(row=1,column=1)



    grau.mainloop()



#===========================PAGINA PRINCIPAL=========================#

al3 = Tk()
al3.geometry('800x800')
al3.columnconfigure(0, weight=1)
al3.columnconfigure(1, weight=1)
al3.columnconfigure(2, weight=1)

al3.rowconfigure(1,weight=1)
al3.rowconfigure(2,weight=1)




text = Label(al3,text='ESCOLHA A FUNÇÃO',font='200')
text.grid(row=1,column=1,sticky=NSEW)


cont = Label(al3,text='',font='40')
cont.grid(row=1,column=0,sticky=NSEW)


btn1 = Button(al3,text='IMC',font='Arial 12', bg='#240A09',fg='white',command=imcc)
btn1.grid(row=2,column=0,sticky=NSEW)


btn2 = Button(al3,text='F°',font='Arial 12',bg='#240A09',fg='white',command=fahren)
btn2.grid(row=2,column=2,sticky=NSEW)



#===========================================================================



















al3.mainloop()