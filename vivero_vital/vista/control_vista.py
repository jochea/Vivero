
import tkinter as tk

class ControlVista:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador

        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Control de Invernaderos", font=("Arial", 18)).pack(pady=10)

        self.lista_frame = tk.Frame(self.frame)
        self.lista_frame.pack()

        self.mostrar_invernaderos()

        tk.Button(self.frame, text="Volver", command=self.volver).pack(pady=10)

    def mostrar_invernaderos(self):
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        for idx, inv in enumerate(self.controlador.controlador_datos):
            texto = f"{inv.nombre} - {inv.tipo_cultivo} - {inv.sistema_riego} - Responsable: {inv.responsable}"
            tk.Label(self.lista_frame, text=texto).grid(row=idx, column=0, sticky='w', padx=10, pady=5)
            tk.Button(self.lista_frame, text="Eliminar", command=lambda i=idx: self.eliminar(i)).grid(row=idx, column=1, padx=5)

    def eliminar(self, index):
        del self.controlador.controlador_datos[index]
        self.mostrar_invernaderos()

    def volver(self):
        self.frame.destroy()
        self.controlador.mostrar_principal()
