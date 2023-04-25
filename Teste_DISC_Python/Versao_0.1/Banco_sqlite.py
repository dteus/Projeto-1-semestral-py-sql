#Tkinter - Interface gráfica
# sqlite - Banco de dados
# pandas - Gerenciamento de informações 
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 
import pandas as pd
import datetime as date

#-----------------------------------------------------------------------------------------------------------------------------------------
# #Criando Banco de dados
# conexao = sqlite3.connect("Cadastro_Alunos.db")
# #Estabelece Cursor (mensageiro)
# c = conexao.cursor()

# c.execute('''CREATE TABLE ALUNOS (
#     CPF TEXT NOT NULL,
#     RA INTEGER NOT NULL,
#     NOME TEXT NOT NULL,
#     EMAIL TEXT NOT NULL,
#     CURSO TEXT,
#     LOGIN TEXT,
#     SENHA TEXT,
#     PRIMARY KEY (CPF))
#     ''')

# c.execute('''CREATE TABLE HISTORICO (
#     DATA_H TEXT NOT NULL,
#     DOMINANTE TEXT NOT NULL,
#     INFLUENTE TEXT NOT NULL,
#     ESTAVEL TEXT NOT NULL,
#     CONFORMADO TEXT NOT NULL,
#     CPF TEXT REFERENCES ALUNOS(CPF)ON DELETE CASCADE)
#     ''')
# conexao.commit()
# conexao.close()
# #-----------------------------------------------------------------------------------------------------------------------------------------


#Criando GUI
#Criando Janela 
janela = tk.Tk()

Lista_Cursos = ["Ciências de dados", "Admnistração", "Analise e Desenvolvimento de Sistemas", "Engenharia de Software"] 

#Botao pica.... INCIAR!!!!
def cadastrar():
    conexao = sqlite3.connect('Cadastro_Alunos.db')
    c = conexao.cursor()
    
    c.execute(" INSERT INTO ALUNOS VALUES (:CPF, :RA, :Nome, :Email, :Curso)",
              {
                'CPF':entry_CPF.get(),
                'RA':entry_RA.get(),
                'Nome':entry_Nome.get(),
                'Email':entry_Email.get(),
                'Curso':combobox_curso.get()
              }
              )
    conexao.commit()

    entry_CPF.delete(0,"end")
    entry_RA.delete(0,"end")
    entry_Nome.delete(0,"end")
    entry_Email.delete(0,"end")
    combobox_curso.delete(0,"end")
    conexao.close()
#-----------------------------------------------------------------------------------------------------------------------------------------

def exportar():

    conexao = sqlite3.connect("Cadastro_Alunos.db")
    #Estabelece Cursor (mensageiro)
    c = conexao.cursor()

    c.execute('SELECT * FROM Alunos')
    Alunos_cadastrados = c.fetchall()
    Alunos_cadastrados = pd.DataFrame(Alunos_cadastrados, columns=('CPF','RA','NOME','EMAIL','CURSO'))
    Alunos_cadastrados.to_excel('Alunos_Cadastrados.xlsx')
    conexao.commit()
    conexao.close()


#-----------------------------------------------------------------------------------------------------------------------------------------

#Titulo
janela.title("Questionário DISC")

#Rótulo da janela
label_cadastro = tk.Label(text = "CADASTRO PICA")
label_cadastro.grid(row = 1, column = 0, padx = 50, pady = 20, sticky = "nswe", columnspan =  4)
#-----------------------------------------------------------------------------------------------------------------------------------------
#Rótulo CPF
label_CPF = tk.Label(text = "CPF")
label_CPF.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "nswe", columnspan = 2)
#Input de dados CPF
entry_CPF = tk.Entry()
entry_CPF.grid(row = 2, column=2, padx=10, pady=10, sticky='nswe', columnspan = 2)

#Rótulo RA
label_RA = tk.Label(text = "RA")
label_RA.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "nswe", columnspan = 2)
#Input de dados RA
entry_RA = tk.Entry()
entry_RA.grid(row = 3, column=2, padx=10, pady=10, sticky='nswe', columnspan = 2)

#Rotulo Nome
label_Nome = tk.Label(text= "Nome")
label_Nome.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "nswe", columnspan =  2)
#Input de dados Nome
entry_Nome = tk.Entry()
entry_Nome.grid(row = 4, column=2, padx=10, pady=10, sticky='nswe', columnspan = 2)

#Rotulo Curso
label_curso = tk.Label(text= "Curso")
label_curso.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "nswe", columnspan =  2)
#Input de dados Curso
combobox_curso = ttk.Combobox(values = Lista_Cursos)
combobox_curso.grid(row = 5, column = 2, padx = 10, pady = 10, sticky='nswe', columnspan = 2)

#Rotulo Email
label_Email = tk.Label(text= "Email")
label_Email.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = "nswe", columnspan =  2)
#Input de dados Email
entry_Email = tk.Entry()
entry_Email.grid(row = 6, column=2, padx=10, pady=10, sticky='nswe', columnspan = 2)

#-----------------------------------------------------------------------------------------------------------------------------------------

#Botão prosseguir
botao_pica = tk.Button(text= "Cadastre-me!", command=cadastrar)
botao_pica.grid(row=7, column=4, padx=10, pady=10, sticky='nswe', columnspan = 1)


#Botão Exportar
botao_exportar = tk.Button(text= "Exportar", command=exportar)
botao_exportar.grid(row=8, column=4, padx=10, pady=10, sticky='nswe', columnspan = 1)

#-----------------------------------------------------------------------------------------------------------------------------------------

#Função para abrir a janela
janela.mainloop()
