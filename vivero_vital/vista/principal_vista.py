
import tkinter as tk
from vista.registro_vista import RegistroVista
from vista.control_vista import ControlVista

class PrincipalVista:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador

        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Panel Principal", font=("Arial", 20)).pack(pady=20)

        tk.Button(self.frame, text="Registrar Invernadero", width=25, command=self.mostrar_registro).pack(pady=10)
        tk.Button(self.frame, text="Control de Invernaderos", width=25, command=self.mostrar_control).pack(pady=10)
        tk.Button(self.frame, text="Cerrar Sesión", width=25, command=self.controlador.mostrar_login).pack(pady=10)

    def mostrar_registro(self):
        self.frame.destroy()
        RegistroVista(self.root, self.controlador)

    def mostrar_control(self):
        self.frame.destroy()
        ControlVista(self.root, self.controlador)
