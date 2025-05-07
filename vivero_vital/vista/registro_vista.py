
import tkinter as tk
from modelo.invernadero_modelo import Invernadero

class RegistroVista:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador

        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Registro de Invernadero", font=("Arial", 18)).pack(pady=10)

        self.campos = {}
        etiquetas = ["Nombre", "Superficie", "Tipo de Cultivo", "Sistema de Riego", "Capacidad de Producción", "Responsable"]
        for etiqueta in etiquetas:
            tk.Label(self.frame, text=etiqueta + ":").pack()
            entrada = tk.Entry(self.frame, width=40)
            entrada.pack(pady=3)
            self.campos[etiqueta] = entrada

        tk.Button(self.frame, text="Guardar", command=self.guardar).pack(pady=10)
        tk.Button(self.frame, text="Cancelar", command=self.volver).pack()

    def guardar(self):
        datos = {campo: entrada.get() for campo, entrada in self.campos.items()}
        nuevo = Invernadero(
            nombre=datos["Nombre"],
            superficie=datos["Superficie"],
            tipo_cultivo=datos["Tipo de Cultivo"],
            sistema_riego=datos["Sistema de Riego"],
            capacidad=datos["Capacidad de Producción"],
            responsable=datos["Responsable"]
        )
        self.controlador.controlador_datos.append(nuevo)
        self.volver()

    def volver(self):
        self.frame.destroy()
        self.controlador.mostrar_principal()
