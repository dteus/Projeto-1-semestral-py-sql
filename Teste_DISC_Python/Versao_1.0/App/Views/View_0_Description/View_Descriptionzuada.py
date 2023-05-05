import tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='white')
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Add widgets to the frame
        label = tk.Label(self, text="Hello, World!", font=("Arial", 16))
        label.pack(pady=10)
        image = tk.PhotoImage(file="path/to/image.png")
        image_label = tk.Label(self, image=image)
        image_label.image = image  # To prevent garbage collection
        image_label.pack(pady=10)
        button = tk.Button(self, text="Click me!", command=self.on_click)
        button.pack(pady=10)

    def on_click(self):
        # Handle button click event
        print("Button clicked!")

root = tk.Tk()
root.title("My App")
frame = MyFrame(root)
frame.pack(expand=True, fill='both')
root.mainloop()
