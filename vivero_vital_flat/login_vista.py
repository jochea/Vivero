
import tkinter as tk
from tkinter import messagebox

class LoginVista:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador

        self.frame = tk.Frame(root, bg="#e6ffe6")
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Iniciar Sesión", font=("Arial", 22, "bold"), bg="#e6ffe6", fg="#2e8b57").pack(pady=40)

        formulario = tk.Frame(self.frame, bg="#e6ffe6")
        formulario.pack()

        tk.Label(formulario, text="Usuario:", font=("Arial", 12), bg="#e6ffe6").grid(row=0, column=0, pady=10, sticky="e")
        self.usuario_entry = tk.Entry(formulario, width=30, font=("Arial", 12))
        self.usuario_entry.grid(row=0, column=1, pady=10)

        tk.Label(formulario, text="Contraseña:", font=("Arial", 12), bg="#e6ffe6").grid(row=1, column=0, pady=10, sticky="e")
        self.clave_entry = tk.Entry(formulario, show="*", width=30, font=("Arial", 12))
        self.clave_entry.grid(row=1, column=1, pady=10)

        tk.Button(self.frame, text="Ingresar", command=self.verificar_credenciales,
                  bg="#66bb6a", fg="white", font=("Arial", 12), width=20, height=2).pack(pady=30)

    def verificar_credenciales(self):
        usuario = self.usuario_entry.get()
        clave = self.clave_entry.get()
        if usuario == "admin" and clave == "1234":
            self.controlador.mostrar_principal()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
