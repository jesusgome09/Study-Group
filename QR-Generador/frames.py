#Aqui se pueden hacer todo a lo que respecta con tkinter
import tkinter as tk
import customtkinter as ct
import logic

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

        #empezar a crear los widgets
        self.entry_info = ct.CTkEntry(self, placeholder_text="Informacion a guardar en el QR")
        self.boton_crear = ct.CTkButton(self, text="Crear QR", command=self.crear_qr)

        #posicionar los widgets
        self.entry_info.pack()
        self.boton_crear.pack()

    def crear_qr(self):
        qr = logic.make_qr(self.entry_info.get())
        print(qr)



window = Window()
frame = Inicio(window)
window.frame = frame
window.mainloop()
