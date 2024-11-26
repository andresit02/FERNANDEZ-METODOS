import tkinter as tk  
from tkinter import ttk, messagebox  

def centrar_ventana(ventana, ancho=800, alto=400):  
    """Función para centrar una ventana en la pantalla."""  
    ventana.update_idletasks()  
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)  
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)  
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")  
    ventana.resizable(False, False)  

def crear_ventana_principal():  
    """Crea la ventana principal con los campos de entrada y botones."""  
    ventana = tk.Tk()  
    ventana.title("Simulador de Ahorro con Interés Compuesto")  
    centrar_ventana(ventana, 800, 600)  

    # Etiquetas y campos de entrada  
    campos = {}  
    etiquetas = [  
        "DEPÓSITO INICIAL:",  
        "TASA DE INTERÉS ANUAL:",  
        "APORTE PERIÓDICO:",  
        "NÚMERO DE PERÍODOS:",
        "PERIÓDO DE CAPITALIZACIÓN"
    ]  
    row = 0  
    for etiqueta in etiquetas:  
        label = tk.Label(ventana, text=etiqueta)  
        label.grid(row=row, column=0, padx=5, pady=5, sticky="w")  
        entry = tk.Entry(ventana)  
        entry.grid(row=row, column=1, padx=5, pady=5)  
        campos[etiqueta] = entry  
        row += 1  

    # Botón para iniciar la simulación  
    boton_simular = tk.Button(ventana, text="INICIAR SIMULACIÓN")  
    boton_simular.grid(row=len(etiquetas), column=0, columnspan=2, pady=20)  

    return ventana, campos, boton_simular  

def mostrar_resultados(historial):  
    """Muestra los resultados en una nueva ventana."""  
    ventana_resultados = tk.Toplevel()  
    ventana_resultados.title("Resultados de la Simulación")  
    centrar_ventana(ventana_resultados)  

    # Crear Treeview para mostrar resultados  
    tree = ttk.Treeview(  
        ventana_resultados,  
        columns=("Periodo", "Aporte", "Capital Actual", "Ganancia", "Capital Final"),  
        show="headings"  
    )  

    # Configuración de encabezados  
    encabezados = ["Periodo", "Aporte", "Capital Actual", "Ganancia", "Capital Final"]  
    for encabezado in encabezados:  
        tree.heading(encabezado, text=encabezado)  
        tree.column(encabezado, anchor="center", width=150)  
     
    # Agregar los datos al Treeview  
    for fila in historial:  
        tree.insert("", tk.END, values=fila)  

    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)