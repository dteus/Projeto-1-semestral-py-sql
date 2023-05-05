
from tkinter import *
import ttkbootstrap as tb
from PIL import Image, ImageTk


#--------------------------------------------------------JANELA PRINCIPAL------------------------------------------------------------------
class Description_Window(tb.Frame):
    def __init__(self, master):
        #Cria o frame MASTER
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        #Adicionando widgets ao frame MASTER
        with open('App/Views/View_0_Description/DISC_Description.txt') as f:
            content = f.read()

        image = tb.PhotoImage(file="App/Views/View_0_Description/bio_logo.png")
        image_label = tb.Label(self, image=image)
        image_label.image = image  # To prevent garbage collection
        canvas = Canvas(root, width=140, height=290)
        canvas.place(x=50,y=100)

        # Add the image to the canvas at position (x, y)
        x = 10
        y = 70
        canvas.create_image(x, y, anchor='nw', image=image)
        # image_label.pack(padx=50,pady=50)
        
        main_frame = tb.LabelFrame(root,
                                text="Descrição", 
                                bootstyle="danger")
        main_frame.place(x=270, y=150)

        descricao = tb.Label(main_frame,
                            text=content,
                            font="Matrix 12 bold",
                            wraplength=500,
                            justify=LEFT)
        descricao.pack(pady=5,padx=10)

            
        entrar_button = tb.Button(main_frame,
                                text="Continuar",
                                bootstyle="primary-outline",
                                command=lambda: self.on_click()
                                )
        entrar_button.pack(padx=10,pady=10)
            
    def on_click(self):
        print("Button Clicked!")

root = tb.Window(themename="superhero")
root.title("DISC-Descrição")
root.geometry("900x500")
frame = Description_Window(root)
frame.pack(expand=False, fill='both')
root.mainloop()
