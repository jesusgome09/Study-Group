import os
import tkinter as tk
import webbrowser
from tkinter import filedialog

from PIL import Image
import customtkinter as ct
import logic


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
        self.leerqr2 = LeerQr2(self)


class Inicio(tk.Frame):  
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
            command=self.github,
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
        webbrowser.open("https://github.com/jesusgome09/Study-Group/tree/main/QR-Generador")


class CrearQr(tk.Frame):
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


        self.imagen = tk.PhotoImage(file=path + "no_existe.png")
        self.imagen = self.imagen.subsample(2, 2)
        self.label_imagen = tk.Label(self, image=self.imagen)


        self.bind("<Visibility>", self.actualizar)


        self.boton_crear = ct.CTkButton(
            self,
            text="Guardar",
            font=("Comic Sans MS", 30, "italic"),
            width=210,
            height=50,
            command=self.guardar_como

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

    def actualizar(self, event):
        self.imagen = tk.PhotoImage(file=path + "QR.png")
        self.imagen = self.imagen.subsample(2, 2)
        self.label_imagen.configure(image=self.imagen, width=200, height=200)


    def regresar(self):

        os.remove(path + "QR.png")
        self.pack_forget()
        parent = self.master
        parent.crearqr.pack(expand=True, fill="both")

    def guardar_como(self):

        image_path = path + "QR.png"
        image = Image.open(image_path)

        sile_pat = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], initialfile="codigo_qr.png")
        if sile_pat:
            image.save(sile_pat)
        else:
            tk.messagebox.showerror("Error", "No se pudo guardar la imagen")


class LeerQr(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Empezar a crear los widgets

        self.frame1 = tk.Frame(self)

        self.titulo = tk.Label(
            self, text="Leer QR", font=("Comic Sans MS", 35, "italic")
        )

        self.parrafo = tk.Label(
            self, text="Adjuntar imagen del QR", font=("Comic Sans MS", 15, "italic")
        )

        self.boton_adjuntar = ct.CTkButton(
            self,
            text="adjuntar",
            font=("Comic Sans MS", 20, "italic"),
            command=self.adjuntar,
        )
        self.boton_regresar = ct.CTkButton(
            self.frame1,
            text="Regresar",
            font=("Comic Sans MS", 30, "italic"),
            width=210,
            height=50,
            command=self.regresar,
        )

        self.boton_leer_qr = ct.CTkButton(
            self.frame1,
            text="Leer",
            font=("Comic Sans MS", 30, "italic"),
            width=210,
            height=50,
            command=self.leer,
        )
        self.label = tk.Label(
            self,
            text="",
        )
        # Posicionar los widgets

        self.titulo.pack(pady=30)
        self.parrafo.pack(pady=20)
        self.boton_adjuntar.pack()
        self.label.pack(pady=10)
        self.frame1.pack(side="bottom",pady=20)
        self.boton_regresar.pack(pady=10, side="left", padx=20)
        self.boton_leer_qr.pack(pady=10, side="right", padx=20)
        self.boton_leer_qr.configure(state="disabled")

    def regresar(self):
        self.pack_forget()
        parent = self.master
        parent.inicio.pack(expand=True, fill="both")

    def leer(self):
        self.label.configure(text="")
        self.boton_adjuntar.configure(state="disabled")

        self.pack_forget()
        parent = self.master
        parent.leerqr2.pack(expand=True, fill="both")

    def adjuntar(self):
        file_ = filedialog.askopenfilename(filetypes=[(".png", "*")])
        if file_:
            self.label.configure(text=file_)
            self.boton_leer_qr.configure(state="normal")
            with open((path+"direccion.txt"), 'w') as f:
                f.write(file_)

class LeerQr2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Empezar a crear los widgets
        self.bind("<Visibility>", self.actualizar)


        self.titulo = tk.Label(
            self, text="Leer QR", font=("Comic Sans MS", 35, "italic")
        )
        imagen = tk.PhotoImage(file=path + "no_existe.png")
        imagen = imagen.subsample(7, 7)
        self.label_imagen = tk.Label(self, image=imagen)

        self.label_info = tk.Label(
            self,
            text="",
        )

        self.boton_regresar = ct.CTkButton(
            self,
            text="Volver al inicio",
            font=("Comic Sans MS", 30, "italic"),
            width=210,
            height=50,
            command=self.volver,
        )

        # Posicionar los widgets

        self.titulo.pack(pady=30)
        self.label_imagen.pack(pady=10)
        self.label_info.pack(pady=10)
        self.boton_regresar.pack(pady=10, padx=20)

    def volver(self):
        self.pack_forget()
        parent = self.master
        parent.inicio.pack(expand=True, fill="both")

    def actualizar(self, event):
        with open(path+"direccion.txt", 'r') as f:
            direccion = f.read()
        os.remove(path+"direccion.txt")

        self.imagen = tk.PhotoImage(file=direccion)
        self.imagen = self.imagen.subsample(2, 2)
        self.label_imagen.configure(image=self.imagen, width=200, height=200)

        self.label_info.configure(text=logic.read_qr(direccion))
        #self.label_info.configure(text='informacion relevante')

def run():
    window = Window()
    frame = Inicio(window)
    window.frame = frame
    window.mainloop()
