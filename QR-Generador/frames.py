import os
import tkinter as tk
import webbrowser
from tkinter import filedialog

import customtkinter as ct
import logic
from PIL import Image, ImageTk
from tkinterdnd2 import DND_FILES, TkinterDnD

absolutepath = os.path.abspath(__file__)
path, filename = os.path.split(absolutepath)
path = path + "\\"


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QR Total")
        self.geometry("500x460+400+100")
        self.resizable(False, False)

        self.incono = tk.PhotoImage(file=path + "icono.png")
        self.iconphoto(True, self.incono)

        self.inicio = Inicio(self)
        self.inicio.pack(expand=True, fill="both")

        self.crearqr = CrearQr(self)
        self.crearqr2 = CrearQr2(self)
        self.leerqr = LeerQr(self)


class Inicio(tk.Frame):  # Terminada
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
            command=self.crear_qr,
        )

        self.boton_leer = ct.CTkButton(
            self.frame1,
            text="Leer QR",
            font=("Comic Sans MS", 30, "italic"),
            width=210,
            height=50,
            command=self.leer_qr,
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


class CrearQr(tk.Frame): # Terminada
    def __init__(self, parent):
        super().__init__(parent)

        # empezar a crear los widgets
        self.frame1 = tk.Frame(self)

        self.label_titulo = tk.Label(
            self, text="Crear QR", font=("Comic Sans MS", 35, "italic")
        )
        self.label = tk.Label(
            self.frame1,
            text="Link, informacion, celular, etc.",
            font=("Comic Sans MS", 12, "italic"),
        )

        self.entry_info = ct.CTkEntry(
            self.frame1,
            placeholder_text="www.google.com",
            width=300,
            font=("Comic Sans MS", 12, "italic"),
            height=40,
        )
        self.boton_crear = ct.CTkButton(
            self,
            text="Crear",
            font=("Comic Sans MS", 30, "italic"),
            width=210,
            height=50,
            command=self.crear_qr
        )
        self.boton_regresar = ct.CTkButton(
            self,
            text="Regresar",
            font=("Comic Sans MS", 30, "italic"),
            width=210,
            height=50,
            command=self.regresar
        )

        # posicionar los widgets
        self.label_titulo.pack(pady=30)
        self.label.pack(pady=10)
        self.entry_info.pack()
        self.frame1.pack(pady=50)
        self.boton_regresar.pack(pady=10, side="left", padx=20)
        self.boton_crear.pack(pady=10, side="left", padx=20)

    def crear_qr(self):
        if logic.make_qr(self.entry_info.get()):
            self.pack_forget()
            parent = self.master
            parent.crearqr2.pack(expand=True, fill="both")
        else:
            tk.messagebox.showerror("Error", "No se puede crear un QR vacio")

    def regresar(self):
        self.pack_forget()
        parent = self.master
        parent.inicio.pack(expand=True, fill="both")

class CrearQr2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # empezar a crear los widgets
        self.frame1 = tk.Frame(self)

        self.label_titulo = tk.Label(
            self, text="Crear QR", font=("Comic Sans MS", 35, "italic")
        )

        if os.path.exists(path + "QR.png"):
            self.imagen = tk.PhotoImage(file=path + "QR.png")
            self.imagen = self.imagen.subsample(2, 2)
            self.label_imagen = tk.Label(self, image=self.imagen)
        else:
            self.imagen = tk.PhotoImage(file=path + "no_existe.png")
            self.imagen = self.imagen.subsample(9, 9)
            self.label_imagen = tk.Label(self, image=self.imagen)

        self.bind("<Visibility>", self.actualizar)


        self.boton_crear = ct.CTkButton(
            self,
            text="Guardar",
            font=("Comic Sans MS", 30, "italic"),
            width=210,
            height=50,

        )
        self.boton_regresar = ct.CTkButton(
            self,
            text="Regresar",
            font=("Comic Sans MS", 30, "italic"),
            width=210,
            height=50,
            command=self.regresar
        )

        # posicionar los widgets
        self.label_titulo.pack(pady=20)
        self.label_imagen.pack(pady=20)
        self.boton_regresar.pack(side="left", padx=20, pady=10)
        self.boton_crear.pack(side="left", padx=20, pady=10)

    def actualizar(self):
        self.update()
    def regresar(self):

        os.remove(path + "QR.png")
        self.pack_forget()
        parent = self.master
        parent.crearqr.pack(expand=True, fill="both")

    def guardar_como(self):

        def guardar_imagen():
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                image.save(file_path)

    # Carga de imagen de ejemplo (adapta esto a tu generación de imagen)
        image_path = path + "QR.png"
        image = Image.open(image_path)

        root = TkinterDnD.Tk()
        root.title("Guardar Imagen")

    # Agregar aquí la generación de tu imagen en un widget (por ejemplo, en un Label)

    # Botón de guardar
        guardar_btn = tk.Button(root, text="Guardar como", command=guardar_imagen)
        guardar_btn.pack()


        root.mainloop()


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
