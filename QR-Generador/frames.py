import tkinter as tk
import customtkinter as ct
import logic
import webbrowser
import os

absolutepath = os.path.abspath(__file__)
path, filename = os.path.split(absolutepath)
path = path + "\\"


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QR Total")
        self.geometry("500x500+400+100")
        self.resizable(False, False)
        self.iconbitmap(path + "qr.ico")

        self.inicio = Inicio(self)
        self.inicio.pack(expand=True, fill="both")

        self.crearqr = CrearQr(self)
        self.leerqr = LeerQr(self)


class Inicio(tk.Frame): # Terminada
    def __init__(self, parent):
        super().__init__(parent)

        # empezar a crear los widgets

        self.frame1 = tk.Frame(self)

        self.titulo = tk.Label(
            self, text="QR Total", font=("Comic Sans MS", 40, "italic")
        )

        self.boton_crear = ct.CTkButton(
            self.frame1,
            text="Crear QR",
            font=("Comic Sans MS", 30, "italic"),
            width=210,
            height=50,
            command=self.crear_qr
        )

        self.boton_leer = ct.CTkButton(
            self.frame1,
            text="Leer QR",
            font=("Comic Sans MS", 30, "italic"),
            width=210,
            height=50,
            command=self.leer_qr
        )

        self.boton_github = ct.CTkButton(
            self.frame1,
            text="GitHub",
            font=("Comic Sans MS", 30, "italic"),
            width=210,
            height=50,
        )

        # posicionar los widgets
        self.titulo.pack(padx=40, pady=20)
        self.frame1.pack(fill="x", pady=40)
        self.boton_crear.pack(padx=20, pady=14)
        self.boton_leer.pack(padx=20, pady=14)
        self.boton_github.pack(padx=20, pady=14)

    def crear_qr(self):
        self.pack_forget()
        parent = self.master
        parent.crearqr.pack(expand=True, fill="both")

    def leer_qr(self):
        self.pack_forget()
        parent = self.master
        parent.leerqr.pack(expand=True, fill="both")

    def github(self):
        webbrowser.open("google.com")


class CrearQr(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # empezar a crear los widgets
        self.label_titulo = tk.Label(self, text="Crear QR", font=("Comic Sans MS", 35, "italic"))
        self.label = tk.Label(self, text="Link, informacion, celular, etc.", font=("Comic Sans MS", 12, "italic"))

        self.entry_info = ct.CTkEntry(
            self, placeholder_text="www.google.com"
        )
        self.boton_crear = ct.CTkButton(self, text="Crear QR", command=self.crear_qr)

        # posicionar los widgets
        self.label_titulo.pack()
        self.label.pack()
        self.entry_info.pack()
        self.boton_crear.pack()

    def crear_qr(self):
        qr = logic.make_qr(self.entry_info.get())
        print(qr)




class LeerQr(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Empezar a crear los widgets

        self.titulo = tk.Label(
            self, text="Leer QR", font=("Comic Sans MS", 35, "italic")
        )

        self.parrafo = tk.Label(
            self, text="Adjuntar imagen del QR", font=("Comic Sans MS", 20, "italic")
        )

        self.boton_regresar = ct.CTkButton(
            self, text="Regresar", font=("Comic Sans MS", 14)
        )

        self.boton_leer_qr = ct.CTkButton(self, text="Leer", font=("Comic Sans MS", 14))

        # Posicionar los widgets

        self.titulo.pack()
        self.parrafo.pack()
        self.boton_regresar.pack()
        self.boton_leer_qr.pack()

        # aqui los llamas con un .pack()
        # El pack es para posicionar los widgets y mostrarlos sin el no los veras
        # El pack tiene parametros como:
        # padx: para el padding en el eje x
        # pady: para el padding en el eje y
        # side: para posicionarlo en el lado que quieras, puede ser "left", "right", "top", "bottom"
        # fill: para que se llene el espacio que tiene disponible, puede ser "x", "y", "both"
        # expand: para que se expanda el widget, puede ser True o Falsess



def run():
    window = Window()
    frame = Inicio(window)
    window.frame = frame
    window.mainloop()

run()
