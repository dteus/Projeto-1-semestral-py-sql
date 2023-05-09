from tkinter import *
import ttkbootstrap as tb
from tkinter import messagebox
#--------------------------------------------------------JANELA PRINCIPAL------------------------------------------------------------------
class Login_Window(tb.Frame):
    def __init__(self, master):
        #Cria o frame MASTER
        super().__init__(master)
        self.master = master
        self.create_widgets()


    def create_widgets(self):

        #Adicionando widgets ao frame MASTER
        image = tb.PhotoImage(file="App/Views/bio_logo.png")
        image_label = tb.Label(self, image=image)
        image_label.image = image  # To prevent garbage collection
        canvas = Canvas(root, width=140, height=290)
        canvas.place(x=50,y=100)
        # Add the image to the canvas at position (x, y)
        x = 10
        y = 70
        canvas.create_image(x, y, anchor='nw', image=image)
        # image_label.pack(padx=50,pady=50)
        
        # Frame que contem entry de login e senha
        main_frame = tb.LabelFrame(root,
                                text="Login", 
                                bootstyle="danger")
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
        Login = tb.Button(main_frame,
                        text="Entrar",
                        bootstyle="primary-outline",
                        command=lambda: self.Login_conferir()
                        )
        Login.grid(row=2,column=1,padx=10,pady=5)
        
        GoBack = tb.Button(main_frame,
                            text="Voltar",
                            bootstyle="secondary-outline",
                            command=lambda: self.main_page()
                            )
        GoBack.grid(row=2,column=0,padx=10,pady=5)

        Registrar = tb.Button(main_frame,
                            text="Não sou cadastrado",
                            bootstyle="warning-outline",
                            command=lambda: self.Register()
                            )
        Registrar.grid(row=3,column=1,padx=10,pady=5)

  
    def Register(self):
        print("Button Clicked!")

    def main_page(self):
        print("Button Clicked!")

    def Login_conferir(self):
        print("Button Clicked!")

        #Acessa Login e Senha
        # Login = self.UserEntry.get()
        # Senha = self.PassEntry.get()
        
        # c = sqlite3.coonect('Database/Cadastro_Alunos.db')
        # try:
        #     validate_login = c.execute("SELECT LOGIN, SENHA FROM ALUNOS WHERE LOGIN = 'Login'")
        #     if validate_login == (Login, Senha):
        #         messagebox.showinfo(title="Logado!", message="Ta dentro meu parceiro!!!")    
        # except:
        #     if len(c.execute("SELECT LOGIN FROM ALUNOS WHERE LOGIN = 'Login'")) > 0:
        #         messagebox.showerror(title="Erro de login", message='Login não cadastrado')
        # else:
        #     messagebox.showerror(title="Erro de login", message='Senha Incorreta')
    


root = tb.Window(themename="superhero")
root.title("DISC-Descrição")
root.geometry("900x500")
frame = Login_Window(root)
frame.pack(expand=False, fill='both')
root.mainloop()
