
import tkinter as tk
from controlador import ControladorApp
from modelo import Invernadero

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Sistema de Gestión de Invernaderos - Vivero Vital")
    root.geometry("900x650")
    root.resizable(False, False)

    app = ControladorApp(root)

    # Cargar 5 invernaderos de ejemplo
    ejemplo = [
        Invernadero("La Esperanza", "500 m²", "Tomate", "Manual", "800 kg", "Ing. Suárez"),
        Invernadero("El Progreso", "300 m²", "Lechuga", "Automatizado", "500 kg", "Tec. Herrera"),
        Invernadero("Flor Verde", "450 m²", "Ornamentales", "Por goteo", "600 plantas", "Ing. Rojas"),
        Invernadero("Sol Vital", "250 m²", "Pimentón", "Manual", "350 kg", "Tec. Peña"),
        Invernadero("Eco Vida", "600 m²", "Hierbas Aromáticas", "Automatizado", "1000 plantas", "Ing. Ortega")
    ]

    app.controlador_datos.extend(ejemplo)
    root.mainloop()
