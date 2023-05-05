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
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to the sys.path list
sys.path.append(parent_dir)
# Now we can import MyClass from utils.py
from utils import View_Description

#--------------------------------------------------------JANELA PRINCIPAL------------------------------------------------------------------
root = tb.Window(themename="superhero")

#Configurações da janela
root.title("Teste Comportamental DISC")
root.geometry("900x500")
root.resizable(width=False, height=False)   

print(type(View_Description))

#Mantem a Janela
root.mainloop()