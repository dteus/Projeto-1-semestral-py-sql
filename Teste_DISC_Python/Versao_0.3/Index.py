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
from hashlib import sha256
#--------------------------------------------FUNÇÕES DE LOGIN E REGISTRO------------------------------------------------------------------------------
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
                            command=lambda: Login()
                            )
    entrar_button.pack(padx=10,pady=10)
def Login():
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
        DataBaser.c.execute("""
        SELECT Login, Senha FROM ALUNOS
        WHERE Login = ? and Senha = ?
        """, (Login, Senha))
        #Verifica os logins e senhas
        VerifyLogin = DataBaser.c.fetchone()
        #Tentativa de login
        try:
            if(Login in VerifyLogin and Senha in VerifyLogin):
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
    for widget in main_frame.winfo_children():
         widget.destroy()
    #Retira informações da tela
    
    # Frame que contem entry de login e senha
    main_frame.configure(text="Registro")
    main_frame.place(x=350, y=50)
#---------------------------------
    RALabel = tb.Label(main_frame,
                    text="RA",
                    font="Matrix 12 bold"
                    )
    RALabel.grid(row=1, column=0, padx=10, pady=10)

    RAEntry = tb.Entry(main_frame, bootstyle="primary")
    RAEntry.grid(row=1, column=1, padx=10, pady=10)
#---------------------------------
    NomeLabel = tb.Label(main_frame,
                    text="Nome",
                    font="Matrix 12 bold")
    NomeLabel.grid(row=2, column=0, padx=10, pady=10)

    NomeEntry = tb.Entry(main_frame, bootstyle="primary")
    NomeEntry.grid(row=2, column=1, padx=10, pady=10)
#---------------------------------
    CPFLabel = tb.Label(main_frame,
                    text="CPF",
                    font="Matrix 12 bold")
    CPFLabel.grid(row=3, column=0, padx=10, pady=10)

    CPFEntry = tb.Entry(main_frame, bootstyle="primary")
    CPFEntry.grid(row=3, column=1, padx=10, pady=10)
#---------------------------------
    EmailLabel = tb.Label(main_frame,
                    text="Email",
                    font="Matrix 12 bold")
    EmailLabel.grid(row=4, column=0, padx=10, pady=10)

    EmailEntry = tb.Entry(main_frame, bootstyle="primary")
    EmailEntry.grid(row=4, column=1, padx=10, pady=10)
  #---------------------------------  
    CursoLabel = tb.Label(main_frame,
                    text="Curso",
                    font="Matrix 12 bold")
    CursoLabel.grid(row=5, column=0, padx=10, pady=10)

    CursoCombobox = tb.Combobox(main_frame,
                    text="Curso",
                    font="Matrix 12 bold",
                    values=Lista_Cursos)
    CursoCombobox.grid(row=5, column=1, padx=10, pady=10)
#---------------------------------
    UserLabel = tb.Label(main_frame,
                    text="Usuario",
                    font="Matrix 12 bold")
    UserLabel.grid(row=6, column=0, padx=10, pady=10)
    UserEntry = tb.Entry(main_frame, bootstyle="primary")
    UserEntry.grid(row=6, column=1, padx=10, pady=10)
#---------------------------------
    PassLabel = tb.Label(main_frame,
                    text="Senha",
                    font="Matrix 12 bold")
    PassLabel.grid(row=7, column=0, padx=10, pady=10)
    PassEntry = tb.Entry(main_frame, bootstyle="primary")
    PassEntry.grid(row=7, column=1, padx=10, pady=10)
#---------------------------------
    def RegisterToDataBase():
        RA = RAEntry.get()
        Nome = NomeEntry.get()
        CPF = CPFEntry.get()
        Email = EmailEntry.get()
        Curso = CursoCombobox.get()
        Login = UserEntry.get()
        Senha = PassEntry.get()
        #inserir no banco de dados a senha criptografada
        Senha = len(sha256(b'0').hexdigest())
        DataBaser.c.execute("""
        SELECT Login, RA, CPF, Email FROM ALUNOS
        WHERE Login = ? and RA = ? and CPF = ? and Email = ?
       """, (Login, RA, CPF, Email))
        #Verifica os logins e senhas
        VerifyLogin = DataBaser.c.fetchone()
        #Verificar Cadastro
        if (RA == '' or Nome == '' or CPF =='' or Email=='' or Curso=='' or Login=='' or Senha==''):
            messagebox.showerror(title='Erro de Registro', message="Preencha todos os campos seu CABEÇÃO! ")
        elif(VerifyLogin is not None and RA in VerifyLogin):
            messagebox.showerror(title='Erro de Registro!', message="RA já cadastrado!")
        elif(VerifyLogin is not None and CPF in VerifyLogin):
            messagebox.showerror(title='Erro de Registro!', message="CPF já cadastrado!")
        elif(VerifyLogin is not None and Login in VerifyLogin):
            messagebox.showerror(title='Erro de Registro!', message="Loguin já cadastrado!")
        elif(VerifyLogin is not None and Email in VerifyLogin):
            messagebox.showerror(title='Erro de Registro!', message="Email Já cadastrado")
        else:
            DataBaser.c.execute("""
            INSERT INTO ALUNOS(null, RA, Nome, CPF, Email, Curso, Login, Senha) VALUES(?, ?, ?, ?, ?, ?, ?, ?)
            """, (RA, Nome, CPF, Email, Curso, Login, Senha))
            DataBaser.conexao.commit()
            messagebox.showinfo(title='Registrado!', message="Ta registrado parceiro!!")

    Register = tb.Button(main_frame,
                        text="Registrar",
                        bootstyle="primary-outline",
                        command=lambda: RegisterToDataBase()
                        )
    Register.grid(row=8,column=1,padx=10,pady=5)
    
    GoBack = tb.Button(main_frame,
                        text="Voltar",
                        bootstyle="secondary-outline",
                        command=lambda: Login()
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
icon = PhotoImage(file='bio_logo.png')   
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
                        command=lambda: Login()
                        )
entrar_button.pack(padx=10,pady=10)


#Mantem a Janela
root.mainloop()