#Sqlite -> Banco de dados
#tkinter -> Interface Gráfica
#tkinter ttk -> funcão do tkinter para facilitar a escrita
#datetime -> Registro de Horário
#PIL -> Configurações para trabalhar com imagens
#DataBaser -> Nome do arquivo de banco de dados
#Hashlib -> Codificador de senhas
from tkinter import *
import ttkbootstrap as tb
import sys
import os.path
# Get the parent directory of the current file
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
# Add the parent directory to the sys.path list
sys.path.append(parent_dir)

from utils import *


#--------------------------------------------------------JANELA PRINCIPAL------------------------------------------------------------------
class Main_Window(tb.Frame):
    def __init__(self):
        super().__init__()
        #Configurações da janela
        root = tb.Window(themename="superhero")
        root.title("Teste Comportamental DISC")
        root.geometry("900x500")
        root.resizable(width=False, height=False) 
        Description_Frame = Description_Window(self)
        Description_Frame.pack()  

class Description_Window(tb.Frame):
    def __init__(self, parent):
        #Cria o frame MASTER
        super().__init__(parent)
        #Adicionando widgets ao frame MASTER
        with open('App/Views/DISC_Description.txt') as f:
            content = f.read()

        image = tb.PhotoImage(file="App/Views/bio_logo.png")
        image_label = tb.Label(self, image=image)
        image_label.image = image  # To prevent garbage collection
        canvas = Canvas(self, width=140, height=290)
        canvas.place(x=50,y=100)
        # Add the image to the canvas at position (x, y)
        x = 10
        y = 70
        canvas.create_image(x, y, anchor='nw', image=image)
        # image_label.pack(padx=50,pady=50)
        
        main_frame = tb.LabelFrame(self,
                                text="Descrição", 
                                bootstyle="danger")
        main_frame.place(x=270, y=150)

        descricao = tb.Label(self,
                            text=content,
                            font="Matrix 12 bold",
                            wraplength=500,
                            justify=LEFT)
        descricao.pack(pady=5,padx=10)
      
        entrar_button = tb.Button(self,
                                text="Continuar",
                                bootstyle="primary-outline",
                                command=continuar_login
                                )
        entrar_button.pack(padx=10,pady=10)

if __name__ == "__main__":
# Create an instance of the main window and start the main event loop
    main_window = Main_Window()
    main_window.mainloop()
