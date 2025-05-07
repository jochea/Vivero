
import tkinter as tk
from registro_vista import RegistroVista
from control_vista import ControlVista

class PrincipalVista:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador

        self.frame = tk.Frame(root, bg="#e6ffe6")
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Panel Principal", font=("Arial", 22, "bold"), bg="#e6ffe6", fg="#2e8b57").pack(pady=30)

        btn_frame = tk.Frame(self.frame, bg="#e6ffe6")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Registrar Invernadero", width=30, height=2,
                  font=("Arial", 12), bg="#66bb6a", fg="white",
                  command=self.mostrar_registro).pack(pady=10)

        tk.Button(btn_frame, text="Control de Invernaderos", width=30, height=2,
                  font=("Arial", 12), bg="#43a047", fg="white",
                  command=self.mostrar_control).pack(pady=10)

        tk.Button(btn_frame, text="Cerrar Sesión", width=30, height=2,
                  font=("Arial", 12), bg="#e57373", fg="white",
                  command=self.controlador.mostrar_login).pack(pady=10)

    def mostrar_registro(self):
        self.frame.destroy()
        RegistroVista(self.root, self.controlador)

    def mostrar_control(self):
        self.frame.destroy()
        ControlVista(self.root, self.controlador)
