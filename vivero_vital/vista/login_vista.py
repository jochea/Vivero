
import tkinter as tk
from tkinter import messagebox

class LoginVista:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador

        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        tk.Label(self.frame, text="Iniciar Sesión", font=("Arial", 20)).pack(pady=20)

        tk.Label(self.frame, text="Usuario:").pack()
        self.usuario_entry = tk.Entry(self.frame)
        self.usuario_entry.pack(pady=5)

        tk.Label(self.frame, text="Contraseña:").pack()
        self.clave_entry = tk.Entry(self.frame, show="*")
        self.clave_entry.pack(pady=5)

        tk.Button(self.frame, text="Ingresar", command=self.verificar_credenciales).pack(pady=20)

    def verificar_credenciales(self):
        usuario = self.usuario_entry.get()
        clave = self.clave_entry.get()
        if usuario == "admin" and clave == "1234":
            self.controlador.mostrar_principal()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
