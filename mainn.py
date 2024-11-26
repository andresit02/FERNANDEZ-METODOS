from interfazz import crear_ventana_principal, mostrar_resultados  
import tkinter as tk  
from tkinter import messagebox, ttk  

class AhorroConInteresCompuesto:  
    def __init__(self, deposito_inicial, tasa_interes_anual, aporte_periodico, periodo_aporte):  
        self.deposito_inicial = deposito_inicial  
        self.tasa_interes_anual = tasa_interes_anual  
        self.aporte_periodico = aporte_periodico  
        self.periodo_aporte = periodo_aporte  
        self.historial = []  

    def calcular_interes_periodico(self):  
        """Calcula el interés periódico en función del período de capitalización."""  
        if self.periodo_aporte == "Semanal":  
            return self.tasa_interes_anual / 52  
        elif self.periodo_aporte == "Mensual":  
            return self.tasa_interes_anual / 12  
        elif self.periodo_aporte == "Bimestral":  
            return self.tasa_interes_anual / 6  
        elif self.periodo_aporte == "Trimestral":  
            return self.tasa_interes_anual / 4  
        else:  # Handle unexpected input  
            return 0  # Or raise an exception  

    def calcular_historial(self, num_periodos):  
        """Genera el historial de capitalización."""  
        interes_periodico = self.calcular_interes_periodico() / 100   

        for periodo in range(1, num_periodos + 1):
            capital_actual = self.deposito_inicial   
            ganancia = round(capital_actual * interes_periodico,2)
            capital_final = round(capital_actual * (1+interes_periodico) ** self.aporte_periodico,2)

            if periodo > 1:    
                capital_actual = round(self.aporte_periodico + capital_actual + ganancia,2) 
                ganancia = round(capital_actual * interes_periodico,2) 

            capital_final = round(capital_actual * (1+interes_periodico) ** self.aporte_periodico,2)

            self.historial.append((periodo, self.aporte_periodico if periodo > 1 else 0, capital_actual, round(ganancia, 2), round(capital_final, 2)))  
            capital_actual = capital_final  


def validate_input(value):  
    try:  
        fvalue = float(value)  
        if fvalue < 0:  
            return False  
        return True  
    except ValueError:  
        return False  


def iniciar_simulacion(campos):  
    try:  
        deposito_inicial = float(campos["DEPÓSITO INICIAL:"].get())  
        tasa_interes_anual = float(campos["TASA DE INTERÉS ANUAL:"].get())  
        aporte_periodico = float(campos["APORTE PERIÓDICO:"].get())  
        num_periodos = int(campos["NÚMERO DE PERÍODOS:"].get())  
        periodo_aporte = campos["PERIÓDO DE CAPITALIZACIÓN:"].get() # Corrected key here  

        if not all(validate_input(v) for v in [deposito_inicial, tasa_interes_anual, aporte_periodico, num_periodos]):  
            messagebox.showerror("Error", "Invalid input. Please enter positive numbers only.")  
            return  

        simulador = AhorroConInteresCompuesto(deposito_inicial, tasa_interes_anual, aporte_periodico, periodo_aporte)  
        simulador.calcular_historial(num_periodos)  
        mostrar_resultados(simulador.historial) 

    except ValueError as e:  
        messagebox.showerror("Error", f"Invalid input: {e}")  
    except Exception as e:  
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")  


if __name__ == "__main__":  
    ventana, campos, boton_simular = crear_ventana_principal()  

    row = 0  
    etiquetas = ["DEPÓSITO INICIAL:", "TASA DE INTERÉS ANUAL:", "APORTE PERIÓDICO:", "NÚMERO DE PERÍODOS:"]  
    for etiqueta in etiquetas:  
        label = tk.Label(ventana, text=etiqueta)  
        label.grid(row=row, column=0, padx=5, pady=5, sticky="w")  
        entry = tk.Entry(ventana, validate="key", validatecommand=(ventana.register(validate_input), '%S'))  
        entry.grid(row=row, column=1, padx=5, pady=5)  
        campos[etiqueta] = entry  
        row += 1  

    # Combobox for PERIÓDO DE CAPITALIZACIÓN
    label = tk.Label(ventana, text="PERIÓDO DE CAPITALIZACIÓN:")  
    label.grid(row=row, column=0, padx=5, pady=5, sticky="w")  
    periodos = ["Semanal", "Mensual", "Bimestral", "Trimestral"]   
    periodo_combobox = ttk.Combobox(ventana, values=periodos)  
    periodo_combobox.grid(row=row, column=1, padx=5, pady=5)  
    campos["PERIÓDO DE CAPITALIZACIÓN:"] = periodo_combobox  

    boton_simular.config(command=lambda: iniciar_simulacion(campos))  
    ventana.mainloop()