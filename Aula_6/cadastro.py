from binascii import crc32
from tkinter import *
from turtle import left

colorbg1 = '#082629'
colorbg2 = '#0B0729'

cletra = '#F7F8EE'
fore = '#5E0401'

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







#=======================================================================================
#===================== FRAME 1 ========= ============================= =================
#==============================================================#
title = Label(frdados,text='     DADOS PESSOAIS',font='Arial 20',foreground=cletra,bg = colorbg2)
title.grid(row=0,columnspan=4,sticky=NSEW)


nome = Label(frdados,text=' Nome:',bg=colorbg2,foreground=cletra,font='Arial 10')
nome.grid(row=1,column=1,sticky=NSEW)

n = Entry(frdados,font='Arial 10',foreground=cletra,bg=colorbg1)
n.grid(row=1,column=2,sticky=NSEW)

DataNsc = Label(frdados,text=' Data NAsc:',bg=colorbg2,foreground=cletra,font='Arial 10')
DataNsc.grid(row=2,column=1,sticky=NSEW)

d = Entry(frdados,font='Arial 10',foreground=cletra,bg=colorbg1)
d.grid(row=2,column=2,sticky=NSEW)


cpf = Label(frdados,text=' CPF:',bg=colorbg2,foreground=cletra,font='Arial 10')
cpf.grid(row=3,column=1,sticky=NSEW)

cp = Entry(frdados,font='Arial 10',foreground=cletra,bg=colorbg1)
cp.grid(row=3,column=2,sticky=NSEW)

telf = Label(frdados,text=' Telefone:',bg=colorbg2,foreground=cletra,font='Arial 10')
telf.grid(row=4,column=1,sticky=NSEW)

tel = Entry(frdados,font='Arial 10',foreground=cletra,bg=colorbg1)
tel.grid(row=4,column=2,sticky=NSEW)


espaco = Label(frdados,text=' ',bg=colorbg2)
espaco.grid(column=0,rowspan=4,sticky=NSEW)

espaco2 = Label(frdados,text=' ',bg=colorbg2)
espaco2.grid(column=3,rowspan=4,sticky=NSEW)



#=======================================================================================
#===================== FRAME 2 ========= ============================= =================
#==============================================================#

'''
rua [                                     ]n°
bairro[                 ]cidade[          ]UF:
'''

ender = Label(frender,text=' Endereço',font='Arial 20',foreground=cletra,bg = colorbg2)
ender.grid(row=0,columnspan=4,sticky=NSEW)

rua = Label(frender,text=' Rua:',bg=colorbg2,foreground=cletra,font='Arial 10')
rua.grid(row=1,column=1,sticky=NSEW)

r = Entry(frender,font='Arial 10',foreground=cletra,bg=colorbg1,width=40)
r.grid(row=1,column=2,sticky=NSEW)

c3 = Label(frender,text='',background=colorbg2)
c3.grid(row=1,column=3)

c4 = Label(frender,text='',background=colorbg2)
c4.grid(row=1,column=4)

num = Label(frender,text=' N°:',bg=colorbg2,foreground=cletra,font='Arial 10')
num.grid(row=1,column=5)


n = Entry(frender,font='Arial 10',foreground=cletra,bg=colorbg1)
n.grid(row=1,column=6,sticky=NSEW)


barro = Label(frender,text=' Bairro:',bg=colorbg2,foreground=cletra,font='Arial 10')
barro.grid(row=2,column=1,sticky=NSEW)

b = Entry(frender,font='Arial 10',foreground=cletra,bg=colorbg1)
b.grid(row=2,column=2,sticky=NSEW)

cidade = Label(frender,text=' Cidade:',bg=colorbg2,foreground=cletra,font='Arial 10')
cidade.grid(row=2,column=3,sticky=NSEW)

cid = Entry(frender,font='Arial 10',foreground=cletra,bg=colorbg1)
cid.grid(row=2,column=4,sticky=NSEW)

ufc = Label(frender,text=' UF:',bg=colorbg2,foreground=cletra,font='Arial 10')
ufc.grid(row=2,column=5,sticky=NSEW)

uf = Entry(frender,font='Arial 10',foreground=cletra,bg=colorbg1)
uf.grid(row=2,column=6,sticky=NSEW)


espaco = Label(frender,text=' ',bg=colorbg2)
espaco.grid(column=0,rowspan=2,sticky=NSEW)

espaco2 = Label(frender,text=' ',bg=colorbg2)
espaco2.grid(column=7,rowspan=2,sticky=NSEW)


#=======================================================================================
#===================== FRAME 3 ========= ============================= =================
#==============================================================#

btn1 = Button(frbotao,text='GRAVAR',bg=colorbg2,fg=cletra)
btn1.grid(row =0,column=1,sticky=NSEW)

btn2 = Button(frbotao,text='LISTAR DADOS',bg=colorbg2,fg=cletra)
btn2.grid(row =0,column=2,sticky=NSEW)


espaco = Label(frbotao,text=' ',bg=colorbg2)
espaco.grid(column=0,rowspan=1,sticky=NSEW)

espaco2 = Label(frbotao,text=' ',bg=colorbg2)
espaco2.grid(column=3,rowspan=1,sticky=NSEW)


dado.mainloop()
