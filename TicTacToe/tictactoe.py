import tkinter as tk
import customtkinter as ct
import webbrowser


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("500x460+400+100")
        self.resizable(False, False)

        self.inicio = Inicio(self)
        self.inicio.pack(fill="both", expand=True)
        self.juego = Juego(self)



class Inicio(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.titulo = tk.Label(self, text="Tic Tac Toe", font=("Comic Sans MS", 30))
        self.boton_jugar = ct.CTkButton(
            self,
            text="Jugar",
            font=("Comic Sans MS", 20),
            width=200,
            height=50,
            command=self.jugar,
        )
        self.boton_github = ct.CTkButton(
            self,
            text="GitHub",
            font=("Comic Sans MS", 20),
            width=200,
            height=50,
            command=self.github,
        )

        self.titulo.pack(pady=40)
        self.boton_jugar.pack(pady=20)
        self.boton_github.pack(pady=20)

    def jugar(self):
        self.pack_forget()
        parent = self.master
        parent.juego.pack(fill="both", expand=True)

    def github(self):
        webbrowser.open("google.com")


class Juego(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.frame_puntos = tk.Frame(self)
        self.frame_tablero = tk.Frame(self)
        self.frame_botones_left = tk.Frame(self, width=150)
        self.frame_botones_right = tk.Frame(self, width=150)

        self.canvas_tablero = tk.Canvas(
            self.frame_tablero, width=300, height=300
        )
        self.puntos_x = tk.Label(
            self.frame_puntos, text="X: 0", font=("Comic Sans MS", 20)
        )
        self.puntos_o = tk.Label(
            self.frame_puntos, text="O: 0", font=("Comic Sans MS", 20)
        )

        self.boton_x = ct.CTkButton(
            self.frame_botones_left,
            text="X",
            font=("Comic Sans MS", 20),
            width=100,
            height=50,
        )
        self.boton_o = ct.CTkButton(
            self.frame_botones_right,
            text="O",
            font=("Comic Sans MS", 20),
            width=100,
            height=50,
            fg_color='green'
        )

        self.boton_terminar = ct.CTkButton(
            self, text="Terminar", font=("Comic Sans MS", 10), width=100, height=25, command=self.terminar
        )

        # Dibujar líneas verticales del tablero
        for i in range(1, 3):
            x = i * 100
            self.canvas_tablero.create_line(x, 0, x, 300, fill="black", width=2)

        # Dibujar líneas horizontales del tablero
        for i in range(1, 3):
            y = i * 100
            self.canvas_tablero.create_line(0, y, 300, y, fill="black", width=2)

        self.boton1 = tk.Button(
            self.canvas_tablero, width=90, height=90, command=lambda: self.presion(1), font=("Arial", 20)
        )
        self.boton2 = tk.Button(
            self.canvas_tablero, width=90, height=90, command=lambda: self.presion(2), font=("Arial", 20)
        )
        self.boton3 = tk.Button(
            self.canvas_tablero, width=90, height=90, command=lambda: self.presion(3), font=("Arial", 20)
        )
        self.boton4 = tk.Button(
            self.canvas_tablero, width=90, height=90, command=lambda: self.presion(4), font=("Arial", 20)
        )
        self.boton5 = tk.Button(
            self.canvas_tablero, width=90, height=90, command=lambda: self.presion(5), font=("Arial", 20)
        )
        self.boton6 = tk.Button(
            self.canvas_tablero, width=90, height=90, command=lambda: self.presion(6), font=("Arial", 20)
        )
        self.boton7 = tk.Button(
            self.canvas_tablero, width=90, height=90, command=lambda: self.presion(7), font=("Arial", 20)
        )
        self.boton8 = tk.Button(
            self.canvas_tablero, width=90, height=90, command=lambda: self.presion(8), font=("Arial", 20)
        )
        self.boton9 = tk.Button(
            self.canvas_tablero, width=90, height=90, command=lambda: self.presion(9), font=("Arial", 20)
        )

        self.canvas_tablero.create_window(
            50, 50, window=self.boton1, width=90, height=90
        )
        self.canvas_tablero.create_window(
            150, 50, window=self.boton2, width=90, height=90
        )
        self.canvas_tablero.create_window(
            250, 50, window=self.boton3, width=90, height=90
        )

        self.canvas_tablero.create_window(
            50, 150, window=self.boton4, width=90, height=90
        )
        self.canvas_tablero.create_window(
            150, 150, window=self.boton5, width=90, height=90
        )
        self.canvas_tablero.create_window(
            250, 150, window=self.boton6, width=90, height=90
        )

        self.canvas_tablero.create_window(
            50, 250, window=self.boton7, width=90, height=90
        )
        self.canvas_tablero.create_window(
            150, 250, window=self.boton8, width=90, height=90
        )
        self.canvas_tablero.create_window(
            250, 250, window=self.boton9, width=90, height=90
        )

        self.puntos_x.pack(side="left", padx=50)
        self.puntos_o.pack(side="right", padx=50)
        self.frame_puntos.pack(pady=20)
        self.canvas_tablero.pack()
        self.frame_tablero.pack()
        self.boton_x.pack(padx=50)
        self.boton_o.pack(padx=50)
        self.boton_terminar.pack()
        self.frame_botones_left.pack(side="left")
        self.frame_botones_right.pack(side="right")

        self.boton_x.configure(state="disabled")
        self.boton_o.configure(state="disabled")
        self.boton_x.configure(state="normal")

        self.player_actual = 1

        self.plano = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
        }
        self.players = {1: 1, 2: 2}
        self.puntos = {0: 0, 1: 0, 2: 0}

    def resetear(self):
        ubicaciones = {
            1: self.boton1,
            2: self.boton2,
            3: self.boton3,
            4: self.boton4,
            5: self.boton5,
            6: self.boton6,
            7: self.boton7,
            8: self.boton8,
            9: self.boton9,
        }

        for i in range(1, 10):
            self.plano[i] = 0
            ubicaciones[i].configure(text="")
            ubicaciones[i].configure(state="normal")
            ubicaciones[i].configure(bg="#f0f0f6")

    def siguiente(self, player_actual):
        if player_actual == 1:
            self.boton_x.configure(state="disabled", fg_color='#f0f0f6')
            self.boton_o.configure(state="normal",fg_color='#afaff0')
            self.player_actual = 2
        elif player_actual == 2:
            self.boton_o.configure(state="disabled", fg_color='#f0f0f6')
            self.boton_x.configure(state="normal", fg_color='#67ea7a')
            self.player_actual = 1

    def marcar_puntaje(self):
        self.puntos_x.configure(text="X: " + str(self.puntos[1]))
        self.puntos_o.configure(text="O: " + str(self.puntos[2]))

    def algoritmo(self):
        if self.plano[1] == self.plano[2] == self.plano[3] != 0:
            self.puntos[self.plano[1]] += 1
            return True
        elif self.plano[4] == self.plano[5] == self.plano[6] != 0:
            self.puntos[self.plano[4]] += 1
            return True
        elif self.plano[7] == self.plano[8] == self.plano[9] != 0:
            self.puntos[self.plano[7]] += 1
            return True
        elif self.plano[1] == self.plano[4] == self.plano[7] != 0:
            self.puntos[self.plano[1]] += 1
            return True
        elif self.plano[2] == self.plano[5] == self.plano[8] != 0:
            self.puntos[self.plano[2]] += 1
            return True
        elif self.plano[3] == self.plano[6] == self.plano[9] != 0:
            self.puntos[self.plano[3]] += 1
            return True
        elif self.plano[1] == self.plano[5] == self.plano[9] != 0:
            self.puntos[self.plano[1]] += 1
            return True
        elif self.plano[3] == self.plano[5] == self.plano[7] != 0:
            self.puntos[self.plano[3]] += 1
            return True
        else:
            return False

    def boton(self, numero, player):
        ubicaciones = {
            1: self.boton1,
            2: self.boton2,
            3: self.boton3,
            4: self.boton4,
            5: self.boton5,
            6: self.boton6,
            7: self.boton7,
            8: self.boton8,
            9: self.boton9,
        }
        jugador = {1: "X", 2: "O"}
        color = {1: "#afaff0", 2: "#67ea7a"}
        ubicaciones[numero].configure(text=jugador[player], state="disabled", background=color[player])

    def presion(self, numero):
        player = self.player_actual

        if self.plano[numero] == 0:
            self.boton(numero, player)  # listo
            self.plano[numero] = player  # listo
            if self.algoritmo():  # listo
                self.resetear()  # Listo
                self.marcar_puntaje()  # listo
            else:
                self.siguiente(player)  # listo
                if self.plano[1] != 0:
                    if self.plano[2] != 0:
                        if self.plano[3] != 0:
                            if self.plano[4] != 0:
                                if self.plano[5] != 0:
                                    if self.plano[6] != 0:
                                        if self.plano[7] != 0:
                                            if self.plano[8] != 0:
                                                if self.plano[9] != 0:
                                                    self.resetear()
    def terminar(self):
        if tk.messagebox.askquestion("Terminar", "¿Estás seguro de que quieres terminar el juego?") == "yes":
            ganador = "Ambos ganaron!, fue un empate"
            x = self.puntos[1]
            y = self.puntos[2]
            if x > y:
                ganador = "X con " + str(x) + " puntos"
            elif y > x:
                ganador = "O con " + str(y) + " puntos"

            tk.messagebox.showinfo(title="GameOver", message=f"El Gananador es: {ganador}")
            self.resetear()
            self.pack_forget()
            parent = self.master
            parent.inicio.pack(fill="both", expand=True)





def run():
    window = Window()
    frame = Inicio(window)
    window.frame = frame
    window.mainloop()



