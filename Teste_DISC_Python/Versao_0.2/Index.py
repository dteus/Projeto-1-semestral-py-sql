#Sqlite -> Banco de dados
#tkinter -> Interface Gráfica
#tkinter ttk -> funcão do tkinter para facilitar a escrita
#datetime -> Registro de Horário
#PIL -> Configurações para trabalhar com imagens
#DataBaser -> Nome do arquivo de banco de dados
#Hashlib -> Codificador de senhas
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import tkinter.ttk as ttk
import DataBaser 
from hashlib import sha256
#-----------------------------------------------------------------------------------------------------------------------------------------

Lista_Cursos = ["Ciências de dados", "Admnistração", "Analise e Desenvolvimento de Sistemas", "Engenharia de Software"]  

#Criando Janela
janela = Tk()
janela.title("Acesso do Aluno")
janela.geometry("900x600")
janela.configure(background="Black")
janela.resizable(width=False, height=False)
#Carregando imagems
logo = (Image.open("bio_logo.png"))

#Widgets
LeftFrame = Frame(janela, width=350, height= 600, bg="#174da3", relief="raised")
LeftFrame.pack(side=LEFT)

Rightrame = Frame(janela, width=540, height= 600, bg="#174da3", relief="raised")
Rightrame.pack(side=RIGHT)

#Resize Image usando TKIMAGE
resized_image= logo.resize((200,350), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

LogoLabel = Label(LeftFrame, image=new_image, bg="#174da3")
LogoLabel.place(x=70, y=100)

UserLabel = Label(Rightrame, text="Login:", font=('Gothic',20), bg="#174da3", fg="White" )
UserLabel.place(x=5, y=270)

UserEntry = ttk.Entry(Rightrame, width=20)
UserEntry.place(x=125,y=285)

PassLabel = Label(Rightrame, text="Senha:", font=('Gothic',20), bg="#174da3", fg="White")
PassLabel.place(x=5, y=320)


PassEntry = ttk.Entry(Rightrame, width=20, show='*')
PassEntry.place(x=125,y=335)
#Estilo do botao
style_1 = {'fg': 'White', 'bg': '#011126', 'activebackground':
        '#8cbbfa', 'activeforeground': 'Black'}
def Login():
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
            messagebox.showinfo(title="Ohh não!!!", message='Login ou Senha inválidos')


#Botões
LoginButton = Button(Rightrame, text='Entrar', width=30, command=Login)
LoginButton.configure(style_1)
LoginButton.place(x=100, y=400)

def Register():
    # Removendo widget
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    # Inserindo widget cadastro
    RALabel = Label(Rightrame, text='RA:', font=("Century Gothic", 20), bg="#174da3", fg="White")
    RALabel.place(x=5,y=25)
    
    RAEntry = ttk.Entry(Rightrame, width=30)
    RAEntry.place(x=125,y=35)

    NomeLabel = Label(Rightrame, text='Nome:', font=("Century Gothic", 20), bg="#174da3", fg="White")
    NomeLabel.place(x=5,y=75)

    NomeEntry = ttk.Entry(Rightrame, width=30)
    NomeEntry.place(x=125,y=80)

    CPFLabel = Label(Rightrame, text='CPF:', font=("Century Gothic", 20), bg="#174da3", fg="White")
    CPFLabel.place(x=5,y=125)

    CPFEntry = ttk.Entry(Rightrame, width=30)
    CPFEntry.place(x=125,y=130)

    EmailLabel = Label(Rightrame, text='Email:', font=("Century Gothic", 20), bg="#174da3", fg="White")
    EmailLabel.place(x=5,y=175)

    EmailEntry = ttk.Entry(Rightrame, width=45)
    EmailEntry.place(x=125,y=180)

    CursoLabel = Label(Rightrame, text='Curso:', font=("Century Gothic", 20), bg="#174da3", fg="White")
    CursoLabel.place(x=5,y=215)

    CursoBox = ttk.Combobox(Rightrame, values=Lista_Cursos)
    CursoBox.place(x=125,y=225)
    
    def RegisterToDataBase():
        RA = RAEntry.get()
        Nome = NomeEntry.get()
        CPF = CPFEntry.get()
        Email = EmailEntry.get()
        Curso = CursoBox.get()
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
            INSERT INTO ALUNOS(RA, Nome, CPF, Email, Curso, Login, Senha) VALUES(?, ?, ?, ?, ?, ?, ?)
            """, (RA, Nome, CPF, Email, Curso, Login, Senha))
            DataBaser.conexao.commit()
            messagebox.showinfo(title='Registrado!', message="Ta registrado parceiro!!")

    Register =  Button(Rightrame, text='Registrar', width=30, command=RegisterToDataBase)
    Register.configure(style_1)
    Register.place(x=100, y=400)


    def BackToLogin():
        #Removendo botoes
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        RALabel.place(x=5000)
        RAEntry.place(x=5000)
        CursoLabel.place(x=5000)
        CursoBox.place(x=5000)
        CPFLabel.place(x=5000)
        CPFEntry.place(x=5000)
        Back.place(x=5000)
        #Devolvendo os botoes anteriores
        LoginButton.place(x=100, y=400)
        RegisterButton.place(x=180, y=440)
        Register.place(x=5000)


    Back =  Button(Rightrame, text='Voltar', width=10, command=BackToLogin)
    Back.configure(style_1)
    Back.place(x=180, y=440)

RegisterButton = Button(Rightrame, text='Registrar', width=10, command=Register)
RegisterButton.configure(style_1)
RegisterButton.place(x=180, y=440)




janela.mainloop()

