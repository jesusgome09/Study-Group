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
        self.config(bg="white")
        self.inicio = Inicio(self)
        self.inicio.pack(expand=True, fill="both")

class Inicio(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #empezar a crear los widgets
        self.titulo = tk.Label(self, text="QR Total", font=("Comic Sans MS", 35, 'italic'))
        self.boton_crear = ct.CTkButton(self, text="Crear QR")
        self.boton_leer = ct.CTkButton(self, text="Leer QR")
        self.boton_github = ct.CTkButton(self, text="GitHub")

        #posicionar los widgets
        self.titulo.pack(padx=10, pady=10)
        self.boton_crear.pack(padx=10, pady=10)
        self.boton_leer.pack(padx=10, pady=10)
        self.boton_github.pack(padx=10, pady=10)

class CrearQr(tk.Frame):
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

    # Leer Qr

class leer_qr(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Empezar a crear los widgets

        self.label = tk.Label(self, text="Leer QR", font=("Comic Sans MS", 35, 'italic'))
        self.label = tk.Label(self, text="Adjuntar imagen del QR", font=("Comic Sans MS", 20, 'italic'))
        self.boton_leer = ct.CTkButton(self, text="Regresar")
        self.boton_leer = ct.CTkButton(self, text="Leer")

        # Posicionar los widgets

        self.label.pack()
        self.boton_leer.pack()

        #aqui los llamas con un .pack()
        # El pack es para posicionar los widgets y mostrarlos sin el no los veras
        # El pack tiene parametros como:
        # padx: para el padding en el eje x
        # pady: para el padding en el eje y
        # side: para posicionarlo en el lado que quieras, puede ser "left", "right", "top", "bottom"
        # fill: para que se llene el espacio que tiene disponible, puede ser "x", "y", "both"
        # expand: para que se expanda el widget, puede ser True o Falsess

    def leer_qr(self):
        qr = logic.read_qr()
        print(qr)





window = Window()
frame = Inicio(window)
window.frame = frame
window.mainloop()
