
import tkinter as tk
from tkinter import ttk
from modelo import Invernadero

class RegistroVista:
    def __init__(self, root, controlador, index_editar=None):
        self.root = root
        self.controlador = controlador
        self.index_editar = index_editar
        self.editando = index_editar is not None

        self.frame = tk.Frame(root, bg="#e6ffe6")
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Registro de Invernadero", font=("Arial", 20, "bold"), bg="#e6ffe6", fg="#2e8b57").pack(pady=20)

        self.campos = {}
        etiquetas = ["Nombre", "Superficie", "Tipo de Cultivo", "Capacidad de Producción", "Responsable"]
        for etiqueta in etiquetas:
            tk.Label(self.frame, text=etiqueta + ":", bg="#e6ffe6", font=("Arial", 12)).pack()
            entrada = tk.Entry(self.frame, width=40, font=("Arial", 12))
            entrada.pack(pady=5)
            self.campos[etiqueta] = entrada

        tk.Label(self.frame, text="Sistema de Riego:", bg="#e6ffe6", font=("Arial", 12)).pack()
        self.sistema_riego_var = tk.StringVar()
        self.sistema_riego_var.set("Manual")
        opciones_riego = ["Manual", "Automatizado", "Por goteo"]
        self.menu_riego = ttk.OptionMenu(self.frame, self.sistema_riego_var, opciones_riego[0], *opciones_riego)
        self.menu_riego.config(width=37)
        self.menu_riego.pack(pady=5)

        if self.editando:
            inv = self.controlador.controlador_datos[self.index_editar]
            self.campos["Nombre"].insert(0, inv.nombre)
            self.campos["Superficie"].insert(0, inv.superficie)
            self.campos["Tipo de Cultivo"].insert(0, inv.tipo_cultivo)
            self.sistema_riego_var.set(inv.sistema_riego)
            self.campos["Capacidad de Producción"].insert(0, inv.capacidad)
            self.campos["Responsable"].insert(0, inv.responsable)

        boton_frame = tk.Frame(self.frame, bg="#e6ffe6")
        boton_frame.pack(pady=20)

        tk.Button(boton_frame, text="Guardar", bg="#66bb6a", fg="white", font=("Arial", 12), width=15,
                  command=self.guardar).grid(row=0, column=0, padx=10)
        tk.Button(boton_frame, text="Cancelar", bg="#e57373", fg="white", font=("Arial", 12), width=15,
                  command=self.volver).grid(row=0, column=1, padx=10)

    def guardar(self):
        datos = {campo: entrada.get() for campo, entrada in self.campos.items()}
        sistema = self.sistema_riego_var.get()

        nuevo = Invernadero(
            nombre=datos["Nombre"],
            superficie=datos["Superficie"],
            tipo_cultivo=datos["Tipo de Cultivo"],
            sistema_riego=sistema,
            capacidad=datos["Capacidad de Producción"],
            responsable=datos["Responsable"]
        )

        if self.editando:
            self.controlador.controlador_datos[self.index_editar] = nuevo
        else:
            self.controlador.controlador_datos.append(nuevo)

        self.volver()

    def volver(self):
        self.frame.destroy()
        self.controlador.mostrar_principal()
