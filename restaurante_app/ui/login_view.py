import tkinter as tk
from tkinter import ttk, messagebox


class LoginView:

    def __init__(
        self,
        root,
        restaurante_servicio,
        mostrar_main
    ):

        self.root = root
        self.servicio = restaurante_servicio
        self.mostrar_main = mostrar_main

        self.crear_interfaz()

    def crear_interfaz(self):

        self.root.configure(
            bg="#f2f4f7"
        )

        contenedor = ttk.Frame(
            self.root,
            padding=30
        )

        contenedor.pack(
            expand=True
        )

        titulo = ttk.Label(
            contenedor,
            text="RESTAURANTE APP",
            font=("Arial", 22, "bold")
        )

        titulo.pack(
            pady=(10, 5)
        )

        subtitulo = ttk.Label(
            contenedor,
            text="Inicio de sesión",
            font=("Arial", 12)
        )

        subtitulo.pack(
            pady=(0, 20)
        )

        formulario = ttk.LabelFrame(
            contenedor,
            text="Acceso",
            padding=20
        )

        formulario.pack(
            padx=20,
            pady=10
        )

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.usuario_entry = ttk.Entry(
            formulario,
            width=30
        )

        self.usuario_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            formulario,
            text="Contraseña:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.contraseña_entry = ttk.Entry(
            formulario,
            width=30,
            show="*"
        )

        self.contraseña_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        boton = ttk.Button(
            formulario,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        )

        boton.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=20
        )

        self.usuario_entry.focus()

    def iniciar_sesion(self):

        usuario = self.usuario_entry.get().strip()

        contraseña = self.contraseña_entry.get()

        if not usuario or not contraseña:

            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese usuario y contraseña."
            )

            return

        valido = self.servicio.validar_usuario(
            usuario,
            contraseña
        )

        if valido:

            self.mostrar_main()

        else:

            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos."
            )