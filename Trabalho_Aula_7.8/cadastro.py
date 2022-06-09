
import tkinter
from cgitb import text
from hashlib import new
from tkinter import *


colorbg1 = '#082629'
colorbg2 = '#0B0729'

cletra = '#F7F8EE'
fore = '#5E0401'




#=========  =========== ======== ======== ==================== ==== ====== ==== ===== ===== =======
#======== ======== ===== FORMATAÇ ÕES ========= ====== ==== ====== ====== ======= ==== ====== =======
#==== ====== =========== ======== ========== ======== ======= =======#
 


def cpfconfig(event = None):
    
    text = cp.get().replace('.','').replace('-','')[:11]
    new_text =""

    if event.keysym.lower() == 'Backspace':return

    for c in range(len(text)):

        if not text[c] in '0123456789': continue 
            
        if c in [2,5]: 
            new_text += text[c] + '.'
        elif c == 8: 
            new_text += text[c] + '-'
        else: 
           new_text += text[c]
                 


        cp.delete(0, "end")
        cp.insert(0, new_text)


def dateConfig (event = None):

    data = d.get().replace('/','')[:8]
    new_date = ""
    
    if event.keysym.lower() == "backspace": return

    for c in range(len(data)):

        if not data[c] in '0132456789':continue
        
        if  c in [1,3]:
            new_date += data[c] + '/'
        else:
            new_date += data[c]


    d.delete(0,"end")
    d.insert(0, new_date)

##=========== =======  ============== ========= ============== ======== =====  ======= ##
 
dado = Tk()
dado.geometry('1000x500+500+250')
dado.title('Cadastro')
dado.configure(bg=colorbg2)
dado.maxsize(width=1000,height=500)
dado.minsize(width=1000,height=500)


frdados = Frame(dado,bg = colorbg2)
frdados.pack(side=TOP,anchor=W)

frdados.columnconfigure(0,weight=1)
frdados.columnconfigure(1,weight=1)
frdados.columnconfigure(2,weight=1)
frdados.columnconfigure(3,weight=1)

frdados.rowconfigure(0,weight=1)
frdados.rowconfigure(1,weight=1)
frdados.rowconfigure(2,weight=1)
frdados.rowconfigure(3,weight=1)
frdados.rowconfigure(4,weight=1)



frender = Frame(dado,bg=colorbg2)
frender.pack(side=TOP,anchor=W)

frender.columnconfigure(0,weight=1)
frender.columnconfigure(1,weight=1)
frender.columnconfigure(2,weight=1)
frender.columnconfigure(3,weight=1)
frender.columnconfigure(4,weight=1)
frender.columnconfigure(5,weight=1)
frender.columnconfigure(6,weight=1)
frender.columnconfigure(7,weight=1)

frdados.rowconfigure(0,weight=1)
frdados.rowconfigure(1,weight=1)



frbotao = Frame(dado,bg=colorbg2)
frbotao.pack(side=TOP,anchor=W)







#=== ======= ============  =============== =============== ========== ==========  ======= =======
#===================== FRAME 1 ========= =========== ========== ======== =================
#======== ==== ======== =======  ===========  ======== =========== =====# 
 
title = Label(frdados,text='     DADOS PESSOAIS',font='Arial 20',foreground=cletra,bg = colorbg2,borderwidth=3)
title.grid(row=0,columnspan=4,sticky=NSEW)


nome = Label(frdados,text=' Nome:',bg=colorbg2,foreground=cletra,font='Arial 10',borderwidth=3)
nome.grid(row=1,column=1,sticky=NSEW)


n = Entry(frdados,font='Arial 10',foreground=cletra,bg=colorbg1,borderwidth=3)
n.grid(row=1,column=2,columnspan = 5,sticky=NSEW)


cpf = Label(frdados,text=' CPF:',bg=colorbg2,foreground=cletra,font='Arial 10',borderwidth=3)
cpf.grid(row=2,column=1,sticky=NSEW)

cp = Entry(frdados,font='Arial 10',foreground=cletra,bg=colorbg1,borderwidth=3)
cp.grid(row=2,column=2,sticky=NSEW)
cp.bind("<KeyRelease>",cpfconfig)

telf = Label(frdados,text=' Telefone:',bg=colorbg2,foreground=cletra,font='Arial 10',borderwidth=3)
telf.grid(row=2,column=3,sticky=NSEW)

tel = Entry(frdados,font='Arial 10',foreground=cletra,bg=colorbg1)
tel.grid(row=2,column=4,sticky=NSEW)




DataNsc = Label(frdados,text=' Data Nasc:',bg=colorbg2,foreground=cletra,font='Arial 10',borderwidth=3)
DataNsc.grid(row=2,column=5,sticky=NSEW)

d = Entry(frdados,font='Arial 10',foreground=cletra,bg=colorbg1,borderwidth=3)
d.grid(row=2,column=6,sticky=NSEW)
d.bind("<KeyRelease>",dateConfig)




espaco = Label(frdados,text=' ',bg=colorbg2,borderwidth=3)
espaco.grid(column=0,rowspan=2,sticky=NSEW)

espaco2 = Label(frdados,text=' ',bg=colorbg2,borderwidth=3)
espaco2.grid(column=7,rowspan=2,sticky=NSEW)

genero = Label(frdados,text='Sexo:',bg=colorbg2,foreground=cletra,font='Arial 10',borderwidth=3)
genero.grid(row=3,column=1)



radiovale = tkinter.IntVar()

m = Radiobutton(frdados,text='Masculino',background=colorbg2,foreground='white',value=1,variable=radiovale,borderwidth=3)
m.grid(row=3,column=2)
f = Radiobutton(frdados,text='feminino',background=colorbg2,foreground= 'white',value=2,variable=radiovale,borderwidth=3)
f.grid(row=3,column=3)


 
#==== ====== ============ =================  =========== ================== ======= ======== ====
#=== ==== ======= ======= FRAME 2 ========= ======== ========= ====== ====== =================
#== ======== ======== ===== ==============  === ========= ===== ==== ====#
  
'''
rua [                                     ]n°
bairro[                 ]cidade[          ]UF:
'''

ender = Label(frender,text=' Endereço',font='Arial 20',foreground=cletra,bg = colorbg2,borderwidth=3)
ender.grid(row=0,columnspan=4,sticky=NSEW)

rua = Label(frender,text=' Rua:',bg=colorbg2,foreground=cletra,font='Arial 10',borderwidth=3)
rua.grid(row=1,column=1,sticky=NSEW)

r = Entry(frender,font='Arial 10',foreground=cletra,bg=colorbg1,width=40,borderwidth=3)
r.grid(row=1,column=2,columnspan=5,sticky=NSEW)

num = Label(frender,text=' N°:',bg=colorbg2,foreground=cletra,font='Arial 10',borderwidth=3)
num.grid(row=1,column=5)


n = Entry(frender,font='Arial 10',foreground=cletra,bg=colorbg1,borderwidth=3)
n.grid(row=1,column=6,sticky=NSEW)


barro = Label(frender,text=' Bairro:',bg=colorbg2,foreground=cletra,font='Arial 10',borderwidth=3)
barro.grid(row=2,column=1,sticky=NSEW)

b = Entry(frender,font='Arial 10',foreground=cletra,bg=colorbg1,borderwidth=3)
b.grid(row=2,column=2,sticky=NSEW)

cidade = Label(frender,text=' Cidade:',bg=colorbg2,foreground=cletra,font='Arial 10',borderwidth=3)
cidade.grid(row=2,column=3,sticky=NSEW)

cid = Entry(frender,font='Arial 10',foreground=cletra,bg=colorbg1,borderwidth=3)
cid.grid(row=2,column=4,sticky=NSEW)

ufc = Label(frender,text=' UF:',bg=colorbg2,foreground=cletra,font='Arial 10',borderwidth=3)
ufc.grid(row=2,column=5,sticky=NSEW)

uf = Entry(frender,font='Arial 10',foreground=cletra,bg=colorbg1,borderwidth=3)
uf.grid(row=2,column=6,sticky=NSEW)


espaco = Label(frender,text=' ',bg=colorbg2,borderwidth=3)
espaco.grid(column=0,rowspan=2,sticky=NSEW)

espaco2 = Label(frender,text=' ',bg=colorbg2,borderwidth=3)
espaco2.grid(column=7,rowspan=2,sticky=NSEW)


#=== ========= ============== ============  ===== ==== ====== === ===== ===  =========  =============
#=== ==== ======= ======= FRAME 3 ========= ====== === ========== ========== ========== =======
#======== === ===== ===== ================= ============== =======#
 
btn1 = Button(frbotao,text='GRAVAR',bg=colorbg2,fg=cletra,borderwidth=3)
btn1.grid(row =0,column=1,sticky=NSEW)

btn2 = Button(frbotao,text='LISTAR DADOS',bg=colorbg2,fg=cletra,borderwidth=3)
btn2.grid(row =0,column=2,sticky=NSEW)


espaco = Label(frbotao,text=' ',bg=colorbg2,borderwidth=3)
espaco.grid(column=0,rowspan=1,sticky=NSEW)

espaco2 = Label(frbotao,text=' ',bg=colorbg2,borderwidth=3)
espaco2.grid(column=3,rowspan=1,sticky=NSEW)


dado.mainloop()
