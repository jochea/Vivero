
import tkinter as tk
from registro_vista import RegistroVista

class ControlVista:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador

        self.frame = tk.Frame(root, bg="#e6ffe6")
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Control de Invernaderos", font=("Arial", 20, "bold"), bg="#e6ffe6", fg="#2e8b57").pack(pady=20)

        self.lista_frame = tk.Frame(self.frame, bg="#e6ffe6")
        self.lista_frame.pack()

        self.mostrar_invernaderos()

        tk.Button(self.frame, text="Volver", command=self.volver,
                  bg="#e57373", fg="white", font=("Arial", 12), width=20).pack(pady=15)

    def mostrar_invernaderos(self):
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        for idx, inv in enumerate(self.controlador.controlador_datos):
            bg_color = "#ffffff" if idx % 2 == 0 else "#f0fff0"
            card = tk.Frame(self.lista_frame, bg=bg_color, pady=10, padx=10, bd=1, relief="solid")
            card.pack(fill="x", padx=20, pady=5)

            texto = f"Nombre: {inv.nombre} | Cultivo: {inv.tipo_cultivo} | Riego: {inv.sistema_riego} | Responsable: {inv.responsable}"
            tk.Label(card, text=texto, bg=bg_color, font=("Arial", 11)).pack(anchor="w")

            btns = tk.Frame(card, bg=bg_color)
            btns.pack(anchor="e", pady=5)

            tk.Button(btns, text="Editar", bg="#4caf50", fg="white", font=("Arial", 10), width=10,
                      command=lambda i=idx: self.editar(i)).pack(side="left", padx=5)
            tk.Button(btns, text="Eliminar", bg="#c62828", fg="white", font=("Arial", 10), width=10,
                      command=lambda i=idx: self.eliminar(i)).pack(side="left", padx=5)

    def eliminar(self, index):
        del self.controlador.controlador_datos[index]
        self.mostrar_invernaderos()

    def editar(self, index):
        self.frame.destroy()
        RegistroVista(self.root, self.controlador, index_editar=index)

    def volver(self):
        self.frame.destroy()
        self.controlador.mostrar_principal()
