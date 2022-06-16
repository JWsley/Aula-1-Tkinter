import tkinter
from tkinter import *
from random import *
from tkinter import ttk
lista = []


# ========================================= LOGIN DO FUNCIONÁRIO========================================================
def login1():
    f1.forget()
    f2.pack()


# =================================FORMATAÇÕES DAS ENTRADAS DO CADASTRO DE CLIENTES=====================================
def format_cpf(event=None):
    text = cpf.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym == "BackSpace":
        return

    for i in range(len(text)):

        if text[i].isnumeric():
            if i in [2, 5]:
                new_text += text[i] + "."
            elif i == 8:
                new_text += text[i] + "-"
            else:
                new_text += text[i]

    cpf.delete(0, "end")
    cpf.insert(0, new_text)


def format_data(event=None):
    text = data.get().replace("/", "")[:8]
    new_text = ""

    if event.keysym == "BackSpace":
        return

    for i in range(len(text)):

        if text[i].isnumeric():
            if i in [1, 3]:
                new_text += text[i] + "/"
            else:
                new_text += text[i]

    data.delete(0, "end")
    data.insert(0, new_text)


def format_tel(event=None):
    text = tele.get().replace("(", "").replace(")", "").replace("", "")[:12]
    new_text = ""

    if event.keysym == "BackSpace":
        return

    for i in range(len(text)):

        if text[i].isnumeric():
            if i in [0]:
                new_text += "(" + text[i]
            elif i in [2]:
                new_text += text[i] + ")"
            elif i in [7]:
                new_text += text[i] + "-"
            else:
                new_text += text[i]

    tele.delete(0, "end")
    tele.insert(0, new_text)


#'AC-','AL-''AM-','BA-','ES-','GO-','MA-','MG-','PA-','RJ-','RS-','SP-','TC-'

def rg_format(event = None):
    text = rg.get().replace(".", "").replace('AC-','').replace('AL-','').replace('AM-','').replace('BA-','').replace('ES-','').replace('GO-','').replace('MA-','').replace('MG-','').replace('PA-','').replace('RJ-','').replace('RS-','').replace('SP-','').replace('TC-','')[:9]
    new_text = ""

    if event.keysym == "BackSpace":
        return

    for i in range(len(text)):

        if text[i].isnumeric():
            if i in [2,5]:
                new_text +=  text[i] +"."
            elif i ==0:
                new_text+= cb.get() + text[i]
            
            else:
                new_text += text[i]
    rg.delete(0, "end")
    rg.insert(0, new_text)
    




   

# ==========================================TELA DE CADASTRO DE CLIENTES================================================
# =========================================Apenas funcionários tem acesso===============================================
def cadastro_cliente():
    f2.forget()
    f4.pack()


# =============================FUNÇÃO PARA ARMAZENAR AS INFORMAÇÕES DOS CLIENTES NO VETOR===============================
def armazena():
    global lista, nome, cpf
    lista.append(nome.get())
    lista.append(cpf.get())
    print(lista)


# =================================================LOGIN DO CLIENTE=====================================================
def login2():
    f1.forget()
    f3.pack()


# ==================================TELA DE MENU DE OPIÇÕES DE OPERAÇÃO BANCÁRIA========================================
def menu():
    f3.forget()
    f5.pack()


def saque():
    f5.forget()
    f6.pack()


def depos():
    f5.forget()
    f7.pack()


def transfe():
    f5.forget()
    f8.pack()


def extrato():
    f5.forget()
    f9.pack()


def saldo():
    f5.forget()
    f10.pack()


# ================================================JANELA PRINCIPAL======================================================
primeira = Tk()
primeira.title('Seleção')
primeira.geometry('990x600+200+200')
primeira.resizable(width=False, height=False)

# ===============================================CRIAÇÃO DE FRAMES======================================================
f1 = Frame(primeira)
f1.pack()
f2 = Frame(primeira)
f3 = Frame(primeira)
f4 = Frame(primeira)
f5 = Frame(primeira)
f6 = Frame(primeira)
f7 = Frame(primeira)
f8 = Frame(primeira)
f9 = Frame(primeira)
f10 = Frame(primeira)

# =====================================DEFINIR IMAGEM DE FUNDO DO PRIMEIRO FRAME========================================
lab_inicial = Label(f1)
lab_inicial.pack()

# ============================================WIDGETS DO PRIMEIRO FRAME=================================================
b1 = Button(f1, text='Funcionário', command=login1)
b1.pack()
b2 = Button(f1, text='Cliente', command=login2)
b2.pack()

# =====================================DEFINIR IMAGEM DE FUNDO DO SEGUNDO FRAME=========================================
lab_login1 = Label(f2, text='Funcionário')
lab_login1.pack()

# ============================================WIDGETS DO SEGUNDO FRAME==================================================
ra = Entry(f2, font=("Calibri", 15), justify=CENTER)
ra.pack()
sh1 = Entry(f2, font=("Calibri", 15), justify=CENTER, show='*')
sh1.pack()
b3 = Button(f2, text='Seguir',  command=cadastro_cliente)
b3.pack()
b4 = Button(f2, text='Voltar', command=lambda: [f2.forget(), f1.pack()])
b4.pack()

# ======================================DEFINIR IMAGEM DE FUNDO DO QUARTO FRAME=========================================
lab_cadastro = Label(f4, text='Cadastro')
lab_cadastro.pack()

# =============================================WIDGETS DO QUARTO FRAME==================================================
nome = Entry(f4, font=("Calibri", 15), justify=CENTER)
nome.pack()

cpf = Entry(f4, font=("Calibri", 15), justify=CENTER)
cpf.bind("<KeyRelease>", format_cpf)
cpf.pack()


#=====================================================MENU DO RG==========================================================

estados =['AC-','AL-''AM-','BA-','ES-','GO-','MA-','MG-','PA-','RJ-','RS-','SP-','TC-']

cb = ttk.Combobox(f4,values=estados)
cb.set('MG-')
cb.pack()


#==========================================================================================================================
rg = Entry(f4, font=("Calibri", 15), justify=CENTER)
rg.bind("<KeyRelease>", rg_format)
rg.pack()

data = Entry(f4, font=("Calibri", 15), justify=CENTER)
data.bind("<KeyRelease>", format_data)
data.pack()

tele = Entry(f4, font=("Calibri", 15), justify=CENTER)
tele.bind("<KeyRelease>", format_tel)
tele.pack()

email = Entry(f4, font=("Calibri", 15), justify=CENTER)
email.pack()

radioVale = tkinter.IntVar()
se1 = Radiobutton(f4, text='Feminino', variable=radioVale, value=1)
se1.pack()

se2 = Radiobutton(f4, text='Masculino', variable=radioVale, value=2)
se2.pack()

rua = Entry(f4, font=("Calibri", 15), justify=CENTER)
rua.pack()

num = Entry(f4, font=("Calibri", 15), justify=CENTER)
num.pack()

bai = Entry(f4, font=("Calibri", 15), justify=CENTER)
bai.pack()

cidi = Entry(f4, font=("Calibri", 15), justify=CENTER)
cidi.pack()

cep = Entry(f4, font=("Calibri", 15), justify=CENTER)
cep.pack()

us1 = Entry(f4, font=("Calibri", 15), justify=CENTER)
us1.pack()

sh2 = Entry(f4, font=("Calibri", 15), justify=CENTER)
sh2.pack()

cont = Label(f4, text=str(00 + random()))

b15 = Button(f4, text='Nova Conta', command=lambda: cont.pack())
b15.pack()

b5 = Button(f4, command=armazena)
b5.pack()

b8 = Button(f4, text='Voltar', command=lambda: [f4.forget(), f2.pack()])
b8.pack()

# ======================================DEFINIR IMAGEM DE FUNDO DO TERCEIRO FRAME=======================================
lab_login2 = Label(f3, text='Cliente')
lab_login2.pack()

# ============================================WIDGETS DO TERCEIRO FRAME=================================================
us2 = Entry(f3, font=("Calibri", 15), justify=CENTER)
us2.pack()
sh3 = Entry(f3, font=("Calibri", 15), justify=CENTER, show='*')
sh3.pack()
b6 = Button(f3, text='Seguir', command=menu)
b6.pack()
b7 = Button(f3, text='Voltar', command=lambda: [f3.forget(), f1.pack()])
b7.pack()

# =======================================DEFINIR IMAGEM DE FUNDO DO QUINTO FRAME========================================
lab_menu = Label(f5, text='Menu')
lab_menu.pack()

# =============================================WIDGETS DO QUINTO FRAME==================================================
b9 = Button(f5, text='Saque', command=saque)
b9.pack()
b10 = Button(f5, text='Deposito', command=depos)
b10.pack()
b11 = Button(f5, text='Transferência', command=transfe)
b11.pack()
b12 = Button(f5, text='Extrato', command=extrato)
b12.pack()
b13 = Button(f5, text='Saldo', command=saldo)
b13.pack()
b14 = Button(f5, text='Voltar', command=lambda: [f5.forget(), f3.pack()])
b14.pack()

# ======================================DEFINIR IMAGEM DE FUNDO DO SEXTO FRAME==========================================
lab_saque = Label(f6, text='Saque')
lab_saque.pack()

# =============================================WIDGETS DO SEXTO FRAME===================================================
saqva = Entry(f6, font=("Calibri", 15), justify=CENTER)
saqva.pack()
saq = Button(f6, text='Saquar')
saq.pack()
saqv = Button(f6, text='Voltar', command=lambda: [f6.forget(), f5.pack()])
saqv.pack()

# =====================================DEFINIR IMAGEM DE FUNDO DO SETIMO FRAME==========================================
lab_depos = Label(f7, text='Deposito')
lab_depos.pack()

# ============================================WIDGETS DO SETIMO FRAME===================================================
deposva = Entry(f7, font=("Calibri", 15), justify=CENTER)
deposva.pack()
deposit = Button(f7, text='Depositar')
deposit.pack()
deposv = Button(f7, text='Voltar', command=lambda: [f7.forget(), f5.pack()])
deposv.pack()

# =====================================DEFINIR IMAGEM DE FUNDO DO OITAVO FRAME==========================================
lab_transfe = Label(f8, text='Transferência')
lab_transfe.pack()

# =============================================WIDGETS DO OITAVO FRAME==================================================
transfva = Entry(f8, font=("Calibri", 15), justify=CENTER)
transfva.pack()
transfconut = Entry(f8, font=("Calibri", 15), justify=CENTER)
transfconut.pack()
transf = Button(f8, text='Transferir')
transf.pack()
transfv = Button(f8, text='Voltar', command=lambda: [f8.forget(), f5.pack()])
transfv.pack()

# ======================================DEFINIR IMAGEM DE FUNDO DO NONO FRAME===========================================
lab_extrato = Label(f9, text='Extrato')
lab_extrato.pack()

# =============================================WIDGETS DO NONO FRAME====================================================
extrava = Label(f9, text='')
extrava.pack()
extra = Button(f9, text='Imprimir')
extra.pack()
extrav = Button(f9, text='Voltar', command=lambda: [f9.forget(), f5.pack()])
extrav.pack()

# ======================================DEFINIR IMAGEM DE FUNDO DO DECIMO FRAME=========================================
lab_saldo = Label(f10, text='Saldo')
lab_saldo.pack()

# ===========================================WIDGETS DO DECIMO FRAME====================================================
saldva = Label(f10, text='')
saldva.pack()
saldv = Button(f10, text='Voltar', command=lambda: [f10.forget(), f5.pack()])
saldv.pack()

primeira.mainloop()
