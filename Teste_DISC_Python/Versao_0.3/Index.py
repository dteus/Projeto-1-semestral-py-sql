#Sqlite -> Banco de dados
#tkinter -> Interface Gráfica
#tkinter ttk -> funcão do tkinter para facilitar a escrita
#datetime -> Registro de Horário
#PIL -> Configurações para trabalhar com imagens
#DataBaser -> Nome do arquivo de banco de dados
#Hashlib -> Codificador de senhas
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as tb
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import DataBaser 
import bcrypt
import sqlite3
#--------------------------------------------FUNÇÕES DE LOGIN & REGISTRO  E VALIDAÇÕES------------------------------------------------------------------------------

def validar_RA(input):
    if len(input) > 8:
        return False
    elif input.isdigit():
        return True 
    
    elif input == "":
        return False

    else:
        return False
    
def validar_CPF(input):
    if len(input) > 11:
        return False
    elif input.isdigit():
        return True 
    
    elif input == "":
        return False

    else:
        return False
        
def validar_Nome(input):
    if (input.isalpha()+' '):
        return True 
    
    elif input == "":
        return False

    else:
        return False


#Hash da senha
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')
#Verificar Senha
def validate_login(username, password):
    if username not in DataBaser.c.execute("""select"""):
        return False
    
    hashed_password = DataBaser[username].encode('utf-8')
    print(f'senha testando{hashed_password} e {DataBaser[username]}')
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# for Widgets in main_frame.winfo_children(): 
#     Widgets.destroy()
def main_page():
    for widget in main_frame.winfo_children():
         widget.destroy()
         
    main_frame.configure(text="Descrição")
    main_frame.place(x=270, y=50)

    descricao = tb.Label(main_frame,
                        text=Descricao_texto,
                        font="Matrix 12 bold",
                        wraplength=500,
                        justify=LEFT)
    descricao.pack(pady=5,padx=10)
        
    entrar_button = tb.Button(main_frame,
                            text="Continuar",
                            bootstyle="primary-outline",
                            command=lambda: Pagina_Login()
                            )
    entrar_button.pack(padx=10,pady=10)

def Pagina_Login():
    for widget in main_frame.winfo_children():
         widget.destroy()
    #Retira informações da tela
    
    # Frame que contem entry de login e senha
    main_frame.configure(text="Login")
    main_frame.place(x=350, y=130)
    
    UserLabel = tb.Label(main_frame,
                    text="Usuario",
                    font="Matrix 12 bold")
    UserLabel.grid(row=0, column=0, padx=10,pady=2)

    UserEntry = tb.Entry(main_frame,
                        bootstyle="primary")
    UserEntry.grid(row=0,column=1,padx=5,pady=1)

    PassLabel = tb.Label(main_frame,
                    text="Senha",
                    font="Matrix 12 bold",
                    )
    PassLabel.grid(row=1,column=0,padx=10,pady=2)

    PassEntry = tb.Entry(main_frame,
                         bootstyle="primary",
                         show="*")
    PassEntry.grid(row=1,column=1, padx=10,pady=20)
    
    def Login_conferir():
        #Acessa Login e Senha
        Login = UserEntry.get()
        Senha = PassEntry.get()
        #Tentativa de login
        try:
            if validate_login(Login, Senha) == True:
                messagebox.showinfo(title="Logado!", message="Ta dentro meu parceiro!!!")    
        except:
                messagebox.showerror(title="Ohh não!!!", message='Login ou Senha inválidos')
    
    Login = tb.Button(main_frame,
                        text="Entrar",
                        bootstyle="primary-outline",
                        command=lambda: Login_conferir()
                        )
    Login.grid(row=2,column=1,padx=10,pady=5)
    
    GoBack = tb.Button(main_frame,
                        text="Voltar",
                        bootstyle="secondary-outline",
                        command=lambda: main_page()
                        )
    GoBack.grid(row=2,column=0,padx=10,pady=5)

    Registrar = tb.Button(main_frame,
                        text="Não sou cadastrado",
                        bootstyle="warning-outline",
                        command=lambda: Register()
                        )
    Registrar.grid(row=3,column=1,padx=10,pady=5)

def Register():
    #Retira informações da tela
    for widget in main_frame.winfo_children():
         widget.destroy()
    
    # Frame que contem entry de registro
    main_frame.configure(text="Registro")
    main_frame.place(x=350, y=50)
#---------------------------------  ENTRADA DE  RA
    RALabel = tb.Label(main_frame,
                    text="RA",
                    font="Matrix 12 bold"
                    )
    RALabel.grid(row=1, column=0, padx=10, pady=10)

    RAEntry = tb.Entry(main_frame, bootstyle="primary")
    RAEntry.grid(row=1, column=1, padx=10, pady=10)

    reg = root.register(validar_RA)
  
    RAEntry.config(validate ="key", 
         validatecommand =(reg, '%P'))
#---------------------------------  ENTRADA DE   NOME 
    NomeLabel = tb.Label(main_frame,
                    text="Nome",
                    font="Matrix 12 bold")
    NomeLabel.grid(row=2, column=0, padx=10, pady=10)

    NomeEntry = tb.Entry(main_frame, bootstyle="primary")
    NomeEntry.grid(row=2, column=1, padx=10, pady=10)

    reg = root.register(validar_Nome)
  
    NomeEntry.config(validate ="key", 
         validatecommand =(reg, '%P'))
#---------------------------------  ENTRADA DE CPF
    CPFLabel = tb.Label(main_frame,
                    text="CPF",
                    font="Matrix 12 bold")
    CPFLabel.grid(row=3, column=0, padx=10, pady=10)

    CPFEntry = tb.Entry(main_frame, bootstyle="primary")
    CPFEntry.grid(row=3, column=1, padx=10, pady=10)
    
    reg = root.register(validar_CPF)
  
    CPFEntry.config(validate ="key", 
         validatecommand =(reg, '%P'))
#---------------------------------    ENTRADA DE EMAIL
    EmailLabel = tb.Label(main_frame,
                    text="Email",
                    font="Matrix 12 bold")
    EmailLabel.grid(row=4, column=0, padx=10, pady=10)

    EmailEntry = tb.Entry(main_frame, bootstyle="primary")
    EmailEntry.grid(row=4, column=1, padx=10, pady=10)
  #---------------------------------   ENTRADA DE CURSO
    CursoLabel = tb.Label(main_frame,
                    text="Curso",
                    font="Matrix 12 bold")
    CursoLabel.grid(row=5, column=0, padx=10, pady=10)

    CursoCombobox = tb.Combobox(main_frame,
                    text="Curso",
                    font="Matrix 12 bold",
                    values=Lista_Cursos)
    CursoCombobox.grid(row=5, column=1, padx=10, pady=10)
#---------------------------------   ENTRADA DE USUARIO
    UserLabel = tb.Label(main_frame,
                    text="Usuario",
                    font="Matrix 12 bold")
    UserLabel.grid(row=6, column=0, padx=10, pady=10)
    UserEntry = tb.Entry(main_frame, bootstyle="primary")
    UserEntry.grid(row=6, column=1, padx=10, pady=10)
#---------------------------------    ENTRADA DE SENHA
    PassLabel = tb.Label(main_frame,
                    text="Senha",
                    font="Matrix 12 bold")
    PassLabel.grid(row=7, column=0, padx=10, pady=10)
    PassEntry = tb.Entry(main_frame, bootstyle="primary")
    PassEntry.grid(row=7, column=1, padx=10, pady=10)
#---------------------------------  FUNÇÃO QUE VERIFICA OS DADOS E OS REGISTRA NO BANCO
    def RegisterToDataBase():
        RA = RAEntry.get()
        Nome = NomeEntry.get().upper()
        CPF = CPFEntry.get()
        Email = EmailEntry.get()
        Curso = CursoCombobox.get()
        Login = UserEntry.get()
        Senha = PassEntry.get()
         
        Senha = hash_password(Senha) 
        print(Senha)
        #Armazena as inforamções em um vetor para o banco de dados usar
        try: 
            DataBaser.c.execute("""INSERT INTO ALUNOS VALUES(?,?,?,?,?,?,?) """,
                                (CPF, RA, Nome, Email, Curso, Login, Senha))
            DataBaser.conexao.commit()
        except sqlite3.IntegrityError: 
            messagebox.showerror(title="Erro!", message="Registro já existe")

        # #Se nada falha registra usuario no banco de dados
        # else:
        #     DataBaser.c.execute("""
        #     INSERT INTO ALUNOS(CPF, RA, Nome, Email, Curso, Login, Senha) VALUES( ?, ?, ?, ?, ?, ?, ?)
        #     """, (CPF, RA, Nome, Email, Curso, Login, Senha))
        #     #Commita as mudanças para que seja possivel logar imediatamente após o registro
        #     DataBaser.conexao.commit()
        #     messagebox.showinfo(title='Registrado!', message="Ta registrado parceiro!!")

    Register = tb.Button(main_frame,
                        text="Registrar",
                        bootstyle="primary-outline",
                        command=lambda: RegisterToDataBase()
                        )
    Register.grid(row=8,column=1,padx=10,pady=5)
    
    GoBack = tb.Button(main_frame,
                        text="Voltar",
                        bootstyle="secondary-outline",
                        command=lambda: Pagina_Login()
                        )
    GoBack.grid(row=8,column=0,padx=10,pady=5) 

#--------------------------------------------------------JANELA PRINCIPAL------------------------------------------------------------------

Lista_Cursos = ["Ciências de dados","Farmácia", "Ciência e Tecnologia"," Engenharia de bioprocessos e biotecnologia","Engenharia de software", "Admnistração", "Analise e Desenvolvimento de Sistemas"]  
Descricao_texto = 'DISC é uma metodologia para fazer a avaliação comportamental a fim de identificar os perfis dominantes de uma pessoa. O método DISC compreende que existem quatro perfis de comportamentos que predominam entre os indivíduos: dominância, influência, estabilidade e conformidade.'
#Inicializa a janela
root = tb.Window(themename="superhero")

#Configurações da janela
root.title("Teste Comportamental DISC")
root.geometry("900x500")
root.resizable(width=False, height=False)   
#Icone da janela
icon = PhotoImage(file='./bio_logo.png')   
root.tk.call('wm', 'iconphoto', root._w, icon)

#Imagem Biopark
logo = (Image.open("bio_logo.png"))
resized_image= logo.resize((200,275), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
LogoLabel = Label(image=new_image)
LogoLabel.place(x=70,y=100)

#Frame descrição - 
main_frame = tb.LabelFrame(root,
                                text="Descrição", 
                                bootstyle="danger")
main_frame.place(x=270, y=50)

descricao = tb.Label(main_frame,
                    text=Descricao_texto,
                    font="Matrix 12 bold",
                    wraplength=500,
                    justify=LEFT)
descricao.pack(pady=5,padx=10)

    
entrar_button = tb.Button(main_frame,
                        text="Continuar",
                        bootstyle="primary-outline",
                        command=lambda: Pagina_Login()
                        )
entrar_button.pack(padx=10,pady=10)


#Mantem a Janela
root.mainloop()