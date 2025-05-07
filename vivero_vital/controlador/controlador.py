
import tkinter as tk
from vista.login_vista import LoginVista
from vista.principal_vista import PrincipalVista

class ControladorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vivero Vital")
        self.root.geometry("800x600")
        self.controlador_datos = []
        self.mostrar_login()

    def mostrar_login(self):
        self.limpiar_ventana()
        self.vista_actual = LoginVista(self.root, self)

    def mostrar_principal(self):
        self.limpiar_ventana()
        self.vista_actual = PrincipalVista(self.root, self)

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()
