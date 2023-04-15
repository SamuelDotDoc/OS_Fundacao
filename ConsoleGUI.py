import random
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def MainConsole():
    root.destroy()

    main = Tk()
    main.title("Console")
    main.geometry("600x500")
    main.iconbitmap("Images/favicon.ico")

    mainframe = Frame(main, bg="Black")
    mainframe.place(relheight=1, relwidth=1)

    label = Label(mainframe, bg="Black",
                  text=
                  "---------------------------------------------------------------------------------------------------"
                  "\nPROMPT DE COMANDO 001 F1980 5MHZ"
                  "\nUNIDADE DE MONITORAMENTO E REGISTRO DE ENTIDADES"
                  "\nTERMINAL " + str(random.randint(1, 50)) + " - USUÁRIO CONFIGURADO PARA AGENTES"
                  "\n--------------------------------------------------------------------------------------------------"
                  "\nO que deseja fazer?\n"
                  "\n<1> Acessar banco de dados de entidades"
                  "\n<2> Procurar por agentes no banco de dados"
                  "\n<3> Sair do console",
                  font=("System", 15), fg="White", justify="left")
    label.pack(anchor="nw", expand=True)

    alt = Entry(mainframe, bg="Black", fg="White", font=("System", 10))
    alt.pack(side="left", anchor="sw", fill="x", expand=True)

    button = Button(mainframe, text="ENVIAR", bg="gray", font=("System", 10), command=lambda: RespMain(alt.get()))
    button.pack(side="left", anchor="sw")

def RespMain(alt):
    if (alt == '1' or alt == '2' or alt == '3'):
        if (alt == '1'):
            ConsoleEntidades()
        elif (alt == '2'):
            ConsoleAgentes()
        else:
            messagebox.showinfo("","Saindo do console...")
            quit()
    else:
        messagebox.showinfo("ERRO!", "Responda com uma alternativa válida.")

def LogOn(usuario, senha):
    senha = senha + "\n"
    d = {}
    with open("Files\Login.txt") as file:
        for line in file:
            (key, val) = line.split(": ")
            d[key] = val
    file.close()
    if usuario in d:
        if (senha == d.get(usuario)):
            messagebox.showinfo("ACESSO CONFIRMADO!", "Bem vindo agente " + usuario + "!")
            MainConsole()
        else:
            messagebox.showinfo("ACESSO NEGADO", "Usuario ou senha incorretos")
    else:
        messagebox.showinfo("ACESSO NEGADO", "Usuario ou senha incorretos")

def ConsoleEntidades():
    entidades = Tk()
    entidades.title("Console")
    entidades.geometry("600x500")
    entidades.iconbitmap("Images/favicon.ico")

    mainframe = Frame(entidades, bg="Black")
    mainframe.place(relheight=1, relwidth=1)

    label = Label(mainframe, bg="Black",
                  text=
                  "---------------------------------------------------------------------------------------------------"
                  "\nPROMPT DE COMANDO 001 F1980 5MHZ"
                  "\nUNIDADE DE MONITORAMENTO E REGISTRO DE ENTIDADES"
                  "\nTERMINAL " + str(random.randint(1, 50)) + " - USUÁRIO CONFIGURADO PARA AGENTES"
                  "\n--------------------------------------------------------------------------------------------------"
                  "\nQue entidade deseja pesquisar?\n"
                  "\n<1> Pesquisar por entidade"
                  "\n<2> Registrar Entidade",
                  font=("System", 15), fg="White", justify="left")
    label.pack(anchor="nw", expand=True)

    alt = Entry(mainframe, bg="Black", fg="White", font=("System", 10))
    alt.pack(side="left", anchor="sw", fill="x", expand=True)

    button = Button(mainframe, text="ENVIAR", bg="gray", font=("System", 10), command=lambda: RespEntidade(alt.get()))
    button.pack(side="left", anchor="sw")

def RespEntidade(alt):
    if (alt == '1' or alt == '2'):
        if (alt == '1'):
            PesquisarEntidade()
        elif (alt == '2'):
            RegistraEntidadeGUI()
    else:
        messagebox.showinfo("ERRO","Responda com uma alternativa válida.")

def RegistraEntidadeGUI():
    registro = Tk()
    registro.title("Console")
    registro.geometry("600x500")
    registro.iconbitmap("Images/favicon.ico")

    mainframe = Frame(registro, bg="Black")
    mainframe.place(relheight=1, relwidth=1)

    informe = Label(mainframe, bg="Black", text="Por favor informe:", font=("System", 10), fg="White")
    informe.place(rely=0.3, relx=0.4)

    numIdLabel = Label(mainframe, bg="Black", text="Código de identificação", font=("System", 10), fg="White")
    numIdLabel.place(rely=0.35, relx=0.22)

    numId = Entry(mainframe, bg="Black", fg="White", font=("System", 10))
    numId.place(rely=0.35, relx=0.52)

    classeLabel = Label(mainframe, bg="Black", text="Classe do objeto", font=("System", 10), fg="White")
    classeLabel.place(rely=0.4, relx=0.25)

    classe = Entry(mainframe, bg="Black", fg="White", font=("System", 10))
    classe.place(rely=0.4, relx=0.52)

    indicativosLabel = Label(mainframe, bg="Black", text="Indicativos de sua presença", font=("System", 10), fg="White")
    indicativosLabel.place(rely=0.45, relx=0.2)

    indicativos = Entry(mainframe, bg="Black", fg="White", font=("System", 10))
    indicativos.place(rely=0.45, relx=0.52)

    descricaoLabel = Label(mainframe, bg="Black", text="Descrição do objeto", font=("System", 10), fg="White")
    descricaoLabel.place(rely=0.5, relx=0.24)

    descricao = Entry(mainframe, bg="Black", fg="White", font=("System", 10))
    descricao.place(rely=0.5, relx=0.52)

    registrar = Button(mainframe, text="REGISTRAR", bg="gray", font=("System", 10),
                       command=lambda: ConfirmarEntidade(numId.get(), classe.get(), indicativos.get(), descricao.get()))
    registrar.place(rely=0.55, relx=0.42)

def ConfirmarEntidade(numId, classe, indicativos, descricao):
    confirmacao = Tk()
    confirmacao.title("Console")
    confirmacao.geometry("250x200")
    confirmacao.iconbitmap("Images/favicon.ico")

    mainframe = Frame(confirmacao, bg="Black")
    mainframe.place(relheight=1, relwidth=1)

    confirmarLabel = Label(mainframe, bg="Black", text="Confirme o registro..."
                                                       "\n Código do objeto: " + str(numId) +
                                                       "\n Classe do objeto: " + str(classe) +
                                                       "\n Indicativos do objeto: " + str(indicativos) +
                                                       "\n Descrição do objeto: " + str(descricao),
                           font=("System", 10), fg="White", wraplength=150)
    confirmarLabel.pack()

    cancelar = Button(mainframe, text="CANCELAR", bg="gray", font=("System", 10), command=lambda: confirmacao.destroy())
    cancelar.place(rely=0.7, relx=0.15)

    registrar = Button(mainframe, text="REGISTRAR", bg="gray", font=("System", 10),
                       command=lambda: RegistraEntidade(numId, ("Classe - " + classe, "Indicativos - " + indicativos, "Descricao - " + descricao)),)
    registrar.place(rely=0.7, relx=0.5)

def PesquisarEntidade():
    def Resp(alt, d):
        if alt in d:
            labelframe = LabelFrame(mainframe, text=alt)
            labelframe.place(relx=0, rely=0.1)
            entidade = Label(labelframe, text=str(d[alt]),
                          bg="Black", fg="White", font=("System", 10), justify="left", wraplength=590)
            entidade.pack()
        else:
            messagebox.showinfo("ERRO", "Entidade não encontrada!")

    search = Tk()
    search.title("Console")
    search.geometry("600x500")
    search.iconbitmap("Images/favicon.ico")

    mainframe = Frame(search, bg="Black")
    mainframe.place(relheight=1, relwidth=1)

    d = {}
    with open("Files\Entidades.txt") as file:
        for line in file:
            (key, val) = line.split(": ")
            d[key] = val
    label = Label(mainframe, text="Qual entidade deseja pesquisar?\n" + str(d.keys()).strip('{'),
                  bg="Black", fg="White", font=("System", 10), justify="left", wraplength=590)
    label.pack(anchor="nw", expand=True)

    alt = Entry(mainframe, bg="Black", fg="White", font=("System", 10))
    alt.pack(side="left", anchor="sw", fill="x", expand=True)

    button = Button(mainframe, text="ENVIAR", bg="gray", font=("System", 10), command =lambda: Resp(alt.get(), d))
    button.pack(side="left", anchor="sw")

    file.close()

def RegistraEntidade(key, val):
    messagebox.showinfo("ENTIDADE REGISTRADA!", "ENTIDADE REGISTRADA, POR FAVOR FECHE AS JANELAS!")
    Entidade = {
        key : val
    }
    file = open("Files\Entidades.txt", "a")
    file.writelines(str(Entidade).strip("{}") + "\n")
    file.close()

def ConsoleAgentes():
    def Resp(alt, d):
        if alt in d:
            labelframe = LabelFrame(mainframe, text=alt)
            labelframe.place(relx=0, rely=0.2)
            entidade = Label(labelframe, text=str(d[alt]),
                          bg="Black", fg="White", font=("System", 10), justify="left", wraplength=600)
            entidade.pack()
        else:
            messagebox.showinfo("ERRO", "Agente não encontrado!")
    agente = Tk()
    agente.title("Console")
    agente.geometry("600x500")
    agente.iconbitmap("Images/favicon.ico")

    mainframe = Frame(agente, bg="Black")
    mainframe.place(relheight=1, relwidth=1)

    label = Label(mainframe, bg="Black",
                  text=
                  "---------------------------------------------------------------------------------------------------"
                  "\nPROMPT DE COMANDO 001 F1980 5MHZ"
                  "\nUNIDADE DE MONITORAMENTO E REGISTRO DE ENTIDADES"
                  "\nTERMINAL " + str(random.randint(1, 50)) + " - USUÁRIO CONFIGURADO PARA AGENTES"
                  "\n--------------------------------------------------------------------------------------------------",
                  font=("System", 15), fg="White", justify="left")
    label.pack(anchor="nw", expand=True)

    d = {}
    with open("Files\Agentes.txt") as file:
        for line in file:
            (key, val) = line.split(": ")
            d[key] = val
    label = Label(mainframe, text="Digite o nome do agente que deseja pesquisar...\n" + str(d.keys()).strip('{'),
                  bg="Black", fg="White", font=("System", 10), justify="left", wraplength=590)
    label.pack(anchor="nw", expand=True)

    alt = Entry(mainframe, bg="Black", fg="White", font=("System", 10))
    alt.pack(side="left", anchor="sw", fill="x", expand=True)

    button = Button(mainframe, text="ENVIAR", bg="gray", font=("System", 10), command=lambda: Resp(alt.get(), d))
    button.pack(side="left", anchor="sw")

    file.close()


root = Tk()
root.title("Console")
root.geometry("600x500")
root.iconbitmap("Images/favicon.ico")

frame = Frame(root, bg="Black")
frame.place(relheight=1, relwidth=1)

img = ImageTk.PhotoImage(Image.open("Images/IconeFundacao.png"))

frameimage = Label(frame, bg="Black", image=img)
frameimage.place(rely=0.1,relx=0.24)

usuarioLabel = Label(frame, bg="Black", text="Usuario", font=("System",10), fg="White")
usuarioLabel.place(rely=0.64,relx=0.3)

senhaLabel = Label(frame, bg="Black", text="Senha", font=("System",10), fg="White")
senhaLabel.place(rely=0.69,relx=0.3)

usuarioEntry = Entry(frame, bg="Black", fg="White", font=("System", 10))
usuarioEntry.place(rely=0.64,relx=0.4)

senhaEntry = Entry(frame, bg="Black", fg="White", font=("System", 10), show="*")
senhaEntry.place(rely=0.69, relx=0.4)

LogIn = Button(frame, text="ENTRAR", bg="gray", font=("System", 10), command=lambda: LogOn(usuarioEntry.get(), senhaEntry.get()))
LogIn.place(rely=0.75, relx=0.45)

root.mainloop()