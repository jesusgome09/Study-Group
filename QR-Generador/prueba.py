from PIL import Image, ImageTk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog
import os
import tkinter as tk

absolutepath = os.path.abspath(__file__)
path, filename = os.path.split(absolutepath)
path = path + "\\"



def guardar_imagen():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        image.save(file_path)

    # Carga de imagen de ejemplo (adapta esto a tu generación de imagen)
image_path = path + "no_existe.png"
image = Image.open(image_path)

root = TkinterDnD.Tk()
root.title("Guardar Imagen")

    # Agregar aquí la generación de tu imagen en un widget (por ejemplo, en un Label)

    # Botón de guardar
guardar_btn = tk.Button(root, text="Guardar como", command=guardar_imagen)
guardar_btn.pack()


root.mainloop()
