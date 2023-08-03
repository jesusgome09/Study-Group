#Aqui se pueden hacer todo a lo que respecta con tkinter
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QR Total")
        self.geometry("500x500")
        self.resizable(False, False)
        self.config(bg="black")
        self.frame = Inicio(self)
        self.frame.pack(expand=True, fill="both")

        inicio = Inicio(self)
        inicio.pack(expand=True, fill="both")

class Inicio(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

window = Window()
frame = Inicio(window)
window.frame = frame
window.mainloop()
