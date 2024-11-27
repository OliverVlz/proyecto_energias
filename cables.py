import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import math

class CalculadoraCables:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de cables para instalaciones eléctricas")
        self.master.configure(bg="mistyrose")

        # Variables para opciones y entradas
        self.variable_opcion = tk.StringVar(value="Elige una opción")
        self.variable_sistema = tk.StringVar(value="Monofásico")
        self.variable_aislamiento = tk.StringVar(value="PVC")
        self.variable_Forma_montar = tk.StringVar(value="1 - 7")

        # Campos de entrada
        self.entry_longitud = tk.Entry(master)
        self.entry_longitud1 = tk.Entry(master)
        self.entry_demanda_potencia = tk.Entry(master)
        self.entry_carga = tk.Entry(master)
        self.entry_caida_tension = tk.Entry(master)
        self.entry_temperatura = tk.Entry(master)
        self.entry_seccion_cable = tk.Entry(master)

        # Resultados dinámicos
        self.label_resultado = tk.Label(master, text="", bg='#ffe4e1')

        # Crear interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Menú de opciones
        option_menu = tk.OptionMenu(
            self.master,
            self.variable_opcion,
            "Calcular caída de tensión y capacidad de conducción",
            "Dimensionar sección del cable",
            command=self.mostrar_campos
        )
        option_menu.configure(bg='#f6adad', activebackground='#f6adad')
        option_menu.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Crear campos y etiquetas comunes
        self.label_longitud = tk.Label(self.master, text="Longitud del cable (m):", bg='#ffe4e1')
        self.label_longitud1 = tk.Label(self.master, text="Longitud hasta la carga (m):", bg='#ffe4e1')
        self.label_sistema = tk.Label(self.master, text="Tipo de sistema:", bg='#ffe4e1')
        self.label_demanda_potencia = tk.Label(self.master, text="Demanda de potencia (kW):", bg='#ffe4e1')
        self.label_aislamiento = tk.Label(self.master, text="Aislamiento del conductor:", bg='#ffe4e1')
        self.label_caida_tension = tk.Label(self.master, text="Caída de tensión permitida (%):", bg='#ffe4e1')
        self.label_temperatura = tk.Label(self.master, text="Temperatura (°C):", bg='#ffe4e1')
        self.label_carga = tk.Label(self.master, text="Carga (A):", bg='#ffe4e1')
        self.label_seccion_cable = tk.Label(self.master, text="Sección del cable (mm²):", bg='#ffe4e1')

        self.label_Forma_montar = tk.Label(self.master, text="Forma de Montar:", bg='#ffe4e1')
        # Opciones
        self.option_sistema = tk.OptionMenu(self.master, self.variable_sistema, "Monofásico", "Trifásico")
        self.option_sistema.configure(bg='#f6adad', activebackground='#f6adad')
        self.option_aislamiento = tk.OptionMenu(self.master, self.variable_aislamiento, "PVC", "XLPE", "EPR")
        self.option_aislamiento.configure(bg='#f6adad', activebackground='#f6adad')
        self.option_Forma_montar = tk.OptionMenu(self.master, self.variable_Forma_montar, "1 - 7", "8 - 13")
        self.option_Forma_montar.configure(bg='#f6adad', activebackground='#f6adad')

        # Botón calcular
        self.button_calcular = tk.Button(self.master, text="Calcular", bg='#f6adad', activebackground='#f6adad')

        # Espacio para resultados
        self.label_resultado.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    def mostrar_campos(self, opcion):
        # Limpia los campos actuales
        self.limpiar_campos()

        if opcion == "Dimensionar sección del cable":
            self.mostrar_dimensionar_seccion()

        elif opcion == "Calcular caída de tensión y capacidad de conducción":
            self.mostrar_calcular_caida()

    def limpiar_campos(self):
        for widget in self.master.grid_slaves():
            if isinstance(widget, tk.Entry) or isinstance(widget, tk.OptionMenu) or isinstance(widget, tk.Label):
                widget.grid_remove()
        self.label_resultado.config(text="")

    def mostrar_dimensionar_seccion(self):
        # Limpiar cualquier widget previamente configurado
        self.limpiar_campos()

        # Mostrar todos los widgets necesarios
        self.label_longitud.grid(row=1, column=0, padx=10, pady=5)
        self.entry_longitud.grid(row=1, column=1, padx=10, pady=5)

        self.label_caida_tension.grid(row=3, column=0, padx=10, pady=5)
        self.entry_caida_tension.grid(row=3, column=1, padx=10, pady=5)

        self.label_demanda_potencia.grid(row=2, column=0, padx=10, pady=5)
        self.entry_demanda_potencia.grid(row=2, column=1, padx=10, pady=5)

        self.label_temperatura.grid(row=4, column=0, padx=10, pady=5)
        self.entry_temperatura.grid(row=4, column=1, padx=10, pady=5)

        self.label_aislamiento.grid(row=5, column=0, padx=10, pady=5)
        self.option_aislamiento.grid(row=5, column=1, padx=10, pady=5)

        self.label_Forma_montar.grid(row=6, column=0, padx=10, pady=5)
        self.option_Forma_montar.grid(row=6, column=1, padx=10, pady=5)

        self.label_sistema.grid(row=7, column=0, padx=10, pady=5)
        self.option_sistema.grid(row=7, column=1, padx=10, pady=5)

        self.button_calcular.config(command=self.dimensionar_seccion_cable)
        self.button_calcular.grid(row=8, column=0, columnspan=2, padx=10, pady=10)


    def mostrar_calcular_caida(self):
        # Limpiar cualquier widget previamente configurado
        self.limpiar_campos()

        # Mostrar widgets necesarios
        self.label_longitud.grid(row=1, column=0, padx=10, pady=5)
        self.entry_longitud.grid(row=1, column=1, padx=10, pady=5)

        self.label_longitud1.grid(row=2, column=0, padx=10, pady=5)
        self.entry_longitud1.grid(row=2, column=1, padx=10, pady=5)

        self.label_caida_tension.grid(row=3, column=0, padx=10, pady=5)
        self.entry_caida_tension.grid(row=3, column=1, padx=10, pady=5)

        self.label_temperatura.grid(row=4, column=0, padx=10, pady=5)
        self.entry_temperatura.grid(row=4, column=1, padx=10, pady=5)

        self.label_carga.grid(row=5, column=0, padx=10, pady=5)
        self.entry_carga.grid(row=5, column=1, padx=10, pady=5)

        self.label_seccion_cable.grid(row=6, column=0, padx=10, pady=5)
        self.entry_seccion_cable.grid(row=6, column=1, padx=10, pady=5)

        self.label_aislamiento.grid(row=7, column=0, padx=10, pady=5)
        self.option_aislamiento.grid(row=7, column=1, padx=10, pady=5)

        self.label_Forma_montar.grid(row=8, column=0, padx=10, pady=5)
        self.option_Forma_montar.grid(row=8, column=1, padx=10, pady=5)

        self.label_sistema.grid(row=9, column=0, padx=10, pady=5)
        self.option_sistema.grid(row=9, column=1, padx=10, pady=5)

        # Configurar el botón para usar el cálculo correcto
        self.button_calcular.config(command=self.calcular_caida_tension)
        self.button_calcular.grid(row=10, column=0, columnspan=2, padx=10, pady=10)


    def validar_entrada(self, entradas, nombres_campos):
        for valor, nombre in zip(entradas, nombres_campos):
            if not valor.strip():
                messagebox.showerror("Error de entrada", f"El campo '{nombre}' está vacío.")
                return False
            try:
                float(valor)
            except ValueError:
                messagebox.showerror("Error de entrada", f"'{valor}' no es un valor válido en '{nombre}'.")
                return False
        return True
    
    def mostrar_resultados(self, resultados, errores=None):
        """
        Actualiza las etiquetas dinámicamente con los resultados o errores.
        :param resultados: Diccionario con las claves y valores a mostrar (puede incluir etiquetas como 'Sección', 'Voltaje', etc.).
        :param errores: Mensaje de error si hay algo que reportar.
        """
        self.limpiar_resultados()

        if errores:
            self.label_resultado.config(text=errores, bg='#ffe4e1')
            self.label_resultado.grid(row=10, column=0, columnspan=2, padx=10, pady=10)
            return

        # Mostrar resultados
        row_offset = 15  # Comienza después de los campos de entrada
        for idx, (titulo, valor) in enumerate(resultados.items()):
            label = tk.Label(self.master, text=f"{titulo}: {valor}", bg='#ffe4e1')
            label.grid(row=row_offset + idx, column=0, columnspan=2, padx=10, pady=5)
            self.result_labels.append(label)

    def limpiar_resultados(self):
        """
        Limpia las etiquetas de resultados para evitar conflictos en el diseño dinámico.
        """
        for label in getattr(self, "result_labels", []):
            label.grid_remove()
        self.result_labels = []

    def calcular_caida_tension(self):
        try:
            # Obtener valores de entrada
            longitud = float(self.entry_longitud.get())
            longitud1 = float(self.entry_longitud1.get())
            carga = float(self.entry_carga.get())
            caida_tension = float(self.entry_caida_tension.get())
            temperatura = float(self.entry_temperatura.get())
            seccion_cable = float(self.entry_seccion_cable.get())
            sistema = self.variable_sistema.get()
            forma_montar = self.variable_Forma_montar.get()
            aislamiento = self.variable_aislamiento.get()

            # Validar tipo de sistema
            if sistema == "Monofásico":
                voltaje = 120
            elif sistema == "Trifásico":
                voltaje = 380
            else:
                self.mostrar_resultados({}, errores="Tipo de sistema inválido.")
                return

            # Calcular valores comunes
            longitud2 = longitud - longitud1
            value_Fa = 0.82
            value_fc = self.calcular_fc(temperatura, aislamiento)

            # Validar el valor de Fc
            if value_fc is None:
                self.mostrar_resultados({}, errores="No se pudo calcular el factor de corrección (Fc). Verifique la temperatura y el aislamiento.")
                return

            # Validar caída de tensión
            if caida_tension > 5:
                self.mostrar_resultados({}, errores="Caída de tensión no permitida (>5%).")
                return

            # Validar temperatura
            if aislamiento == "PVC" and temperatura > 60:
                self.mostrar_resultados({}, errores="La temperatura para aislamiento PVC no debe ser mayor a 60°C.")
                return

            # Calcular caída de tensión para longitud > 40 m
            if longitud > 40:
                value_k_obtenido = self.calcular_k(seccion_cable, sistema, forma_montar)
                if value_k_obtenido is None:
                    self.mostrar_resultados({}, errores="No se pudo calcular el valor de k. Verifique la sección y el sistema.")
                    return
                ΔV_calculado = value_k_obtenido * carga * longitud2 * 0.001
                porcentaje1 = (ΔV_calculado / voltaje) * 100
                porcentaje2 = caida_tension - porcentaje1
                ΔV_restante = porcentaje2 * 0.01 * voltaje
                value_I_Real = (ΔV_restante / (value_k_obtenido * longitud1 * 0.001)) - carga
                value_I_Real = value_I_Real * value_Fa * value_fc
                value_I_perm = self.calcular_I_permitida(seccion_cable, forma_montar)

                if value_I_perm > value_I_Real:
                    resultados = {
                        "Caída de tensión calculada": f"ΔV = {round(ΔV_calculado, 2)} V",
                        "Corriente equivalente": f"I' = {round(value_I_Real, 2)} A",
                        "Corriente permitida": f"I = {round(value_I_perm, 2)} A",
                    }
                    self.mostrar_resultados(resultados)
                else:
                    self.mostrar_resultados({}, errores="I' > Iper, por tanto no es posible usar un cable con esta sección.")
            else:  # Calcular caída de tensión para longitud <= 40 m
                value_k_obtenido = self.calcular_k(seccion_cable, sistema, forma_montar)
                if value_k_obtenido is None:
                    self.mostrar_resultados({}, errores="No se pudo calcular el valor de k. Verifique las entradas.")
                    return
                ΔV_permitido = voltaje * caida_tension * 0.01
                ΔV_calculado = value_k_obtenido * carga * longitud2 * 0.001
                value_I_Real = carga / (value_Fa * value_fc)

                if ΔV_permitido > ΔV_calculado:
                    resultados = {
                        "Caída de tensión calculada": f"ΔV = {round(ΔV_calculado, 2)} V",
                        "Caída de tensión permitida": f"ΔV = {round(ΔV_permitido, 2)} V",
                        "Corriente equivalente": f"I' = {round(value_I_Real, 2)} A",
                    }
                    self.mostrar_resultados(resultados)
                else:
                    self.mostrar_resultados({}, errores="ΔV permitido > ΔV calculado, por tanto no es posible usar un cable con esta sección.")

        except Exception as e:
            self.mostrar_resultados({}, errores=f"Error en el cálculo: {e}")


    def dimensionar_seccion_cable(self):
        entradas = [
            self.entry_longitud.get(),
            self.entry_demanda_potencia.get(),
            self.entry_caida_tension.get(),
            self.entry_temperatura.get(),
        ]
        nombres_campos = ["Longitud del cable", "Demanda de potencia", "Caída de tensión", "Temperatura"]

        if not self.validar_entrada(entradas, nombres_campos):
            return

        longitud, demanda_potencia, caida_tension, temperatura = map(float, entradas)
        sistema = self.variable_sistema.get()
        aislamiento = self.variable_aislamiento.get()
        forma_montar = self.variable_Forma_montar.get()

        # Valores por defecto para cálculos
        value_Fa = 0.82
        value_fc = self.calcular_fc(temperatura, aislamiento)

        voltaje = 120 if sistema == "Monofásico" else 380

        # Calcular corriente y sección del cable
        try:
            if longitud > 40:
                if caida_tension <= 5:
                    if (aislamiento == 'PVC' and temperatura <= 60) or aislamiento in ['XLPE', 'EPR']:
                        value_I = (demanda_potencia * 1000) / (math.sqrt(3) * voltaje * 0.9)
                        value_k = caida_tension * 0.01 * voltaje / (value_I * longitud * 0.001)
                        
                        # Calcular sección del cable
                        seccion_cable = self.calcular_s(value_k, sistema)
                        
                        # Validar si seccion_cable es None
                        if seccion_cable is None:
                            self.mostrar_resultados({}, errores="No se pudo calcular una sección válida para el cable.")
                            return

                        value_I_Real = value_I / (value_Fa * value_fc)
                        value_I_perm = self.calcular_I_permitida(seccion_cable, forma_montar)

                        resultados = {
                            "Sección del cable necesaria": f"{seccion_cable} mm²",
                            "Caída de tensión calculada": f"ΔV = {round(caida_tension * 0.01 * voltaje, 2)} V",
                            "Corriente calculada": f"I = {round(value_I, 2)} A",
                            "Corriente equivalente": f"I' = {round(value_I_Real, 2)} A",
                            "Corriente permitida": f"I = {round(value_I_perm, 2)} A",
                        }
                        self.mostrar_resultados(resultados)
                    else:
                        self.mostrar_resultados({}, errores="La temperatura para PVC no debe ser mayor a 60°C.")
                else:
                    self.mostrar_resultados({}, errores="Caída de tensión no permitida (>5%).")
            else:
                if caida_tension <= 5:
                    if (aislamiento == 'PVC' and temperatura <= 60) or aislamiento in ['XLPE', 'EPR']:
                        value_I = (demanda_potencia * 1000) / (math.sqrt(3) * voltaje * 0.9)
                        value_I_Real = value_I / (value_Fa * value_fc)
                        
                        # Calcular sección del cable
                        seccion_cable = self.calcular_seccion(value_I_Real, aislamiento, forma_montar)
                        
                        # Validar si seccion_cable es None
                        if seccion_cable is None:
                            self.mostrar_resultados({}, errores="No se pudo calcular una sección válida para el cable.")
                            return

                        value_k_obtenido = self.calcular_k(seccion_cable, sistema, forma_montar)
                        if value_k_obtenido is None:
                            self.mostrar_resultados({}, errores="No se pudo calcular el valor de k. Verifique las entradas.")
                            return

                        ΔV_calculado = value_k_obtenido * value_I * longitud * 0.001
                        ΔV_permitido = voltaje * caida_tension * 0.01

                        resultados = {
                            "Sección del cable necesaria": f"{seccion_cable} mm²",
                            "Caída de tensión calculada": f"ΔV = {round(ΔV_calculado, 2)} V",
                            "Caída de tensión permitida": f"ΔV = {round(ΔV_permitido, 2)} V",
                            "Corriente calculada": f"I = {round(value_I, 2)} A",
                            "Corriente equivalente": f"I' = {round(value_I_Real, 2)} A",
                        }
                        self.mostrar_resultados(resultados)
                    else:
                        self.mostrar_resultados({}, errores="La temperatura para PVC no debe ser mayor a 60°C.")
                else:
                    self.mostrar_resultados({}, errores="Caída de tensión no permitida (>5%).")
        except Exception as e:
            self.mostrar_resultados({}, errores=f"Error en el cálculo: {e}")


#FUNCIONES DE CALCULOS**************************************************************************************************   
    def calcular_k(self, value_s, tipo_sistema, forma_montar_value):
        vector_seccion = [1, 1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240, 300, 400, 500]
        if forma_montar_value == "1 - 7":        
            if tipo_sistema == "Monofásico":        
                vector_k = [34, 23, 14, 8.7, 5.8, 3.5, 3.31, 1.52, 1.12, 0.82, 0.63, 0.49, 0.41, 0.36, 0.32, 0.26, 0.23, 0.2, 0.19]
            elif tipo_sistema == "Trifásico":
                vector_k = [29, 20, 12, 7.5, 5.1, 3, 1.96, 1.28, 0.96, 0.73, 0.54, 0.42, 0.35, 0.31, 0.27, 0.23, 0.2, 0.18, 0.16]
            else:
                return None
        else:
            if tipo_sistema == "Monofásico":        
                vector_k = [34, 23, 14, 9, 6.18, 3.84, 2.57, 1.76, 1.36, 1.09, 0.86, 0.7, 0.62, 0.56, 0.5, 0.45, 0.4, 0.37, 0.34]
            elif tipo_sistema == "Trifásico":
                vector_k = [29.5, 19.86, 12.33, 7.82, 5.35, 3.33, 2.22, 1.52, 1.18, 0.95, 0.74, 0.62, 0.54, 0.48, 0.44, 0.39, 0.35, 0.32, 0.29]
            else:
                return None

        if value_s in vector_seccion:
            index = vector_seccion.index(value_s)
            return vector_k[index]
        else:
            return None


    #funcion para obtener el valor de la seccion
    #-------------------------------------------------------------------------------------------------------------------------

    def calcular_s(self, value_k2, tipo_sistema):
        vector_seccion = [1, 1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240, 300, 400, 500]
        if tipo_sistema == "Monofásico":        
            vector_k = [34, 23, 14, 8.7, 5.8, 3.5, 3.31, 1.52, 1.12, 0.82, 0.63, 0.49, 0.41, 0.36, 0.32, 0.26, 0.23, 0.2, 0.19]
        elif tipo_sistema == "Trifásico":
            vector_k = [29, 20, 12, 7.5, 5.1, 3, 1.96, 1.28, 0.96, 0.73, 0.54, 0.42, 0.35, 0.31, 0.27, 0.23, 0.2, 0.18, 0.16]
        else:
            messagebox.showerror("Error de cálculo", "Tipo de sistema inválido.")
            return None

        # Buscar la sección en el vector
        if value_k2 in vector_k:
            index = vector_k.index(value_k2)
            return vector_seccion[index]
        else:
            # Aproximar al valor más cercano en el vector
            closest_k = max([k for k in vector_k if k < value_k2], default=None)
            if closest_k is not None:
                index = vector_k.index(closest_k)
                return vector_seccion[index]
            else:
                # No hay valores válidos
                messagebox.showerror("Error de cálculo", "No se encontró una sección válida para el valor k.")
                return None


    #calcular el Fc
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    def calcular_fc(self, valor_temp, aislamiento_value):
        """
        Calcula el factor de corrección (Fc) según la temperatura y el tipo de aislamiento.
        """
        vector_temp = [10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
        if aislamiento_value == "PVC":
            vector_factor = [1.22, 1.17, 1.12, 1.07, 0.93, 0.87, 0.79, 0.71, 0.61, 0.50, 0.20, 0.20, 0.20, 0.20]
        else:
            vector_factor = [1.15, 1.12, 1.08, 1.04, 0.98, 0.96, 0.94, 0.92, 0.87, 0.84, 0.82, 0.80, 0.72, 0.61]

        # Verificar si la temperatura está en el rango
        if valor_temp in vector_temp:
            index = vector_temp.index(valor_temp)
            return vector_factor[index]
        else:
            # Manejo de error si el valor no está en el rango
            messagebox.showerror("Error de cálculo", f"La temperatura {valor_temp}°C no es válida.")
            return None



    #calcular la corriente permitida
    #----------------------------------------------------------------------------------------------------------------------------------------------
    def calcular_I_permitida(self,seccion_cable,Forma_montar_value):
        vector_seccion_nominal = [1, 1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240, 300, 400, 500]
        if Forma_montar_value == "1 - 7":
            vector_cond3_agrupados = [16, 20, 27, 36, 48, 66, 88, 116, 144, 175, 222, 268, 311, 353, 402, 474, 545, 652, 750]
        else:
            vector_cond3_agrupados = [18, 23, 31, 42, 54, 74, 100, 132, 163, 198, 252, 305, 353, 406, 462, 453, 620, 742, 852]

        if seccion_cable in vector_seccion_nominal:
            index = vector_seccion_nominal.index(seccion_cable)
            value_I_permitida = vector_cond3_agrupados[index]
            return value_I_permitida
        else:
            return None

    #Calcular seccion con el valor de la corriente Real   tabla 5.3-b  tabla 5.3-a
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def calcular_seccion(vself,value_corriente,value_material, Forma_montar_value):
        vector_seccion_nominal = [1, 1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240, 300, 400, 500]
        if value_material == "PVC":
            if Forma_montar_value == "8 - 13":
                vector_corriente=[13.5, 17.5, 24, 32, 41, 57, 76, 101, 125, 151, 192, 232, 269, 309, 353, 415, 473, 566, 651]
            else:
                vector_corriente=[12, 15.5, 21, 28, 36, 50, 68, 89, 111, 134, 171, 207, 239, 272, 310, 364, 419, 502, 578]
        #Para materia EPR o XLPE
        else:
            if Forma_montar_value == "8 - 13":
                vector_corriente=[18, 23, 31, 42, 54, 74, 100, 132, 163, 198, 252, 305, 353, 406, 462, 453, 620, 742, 852]
            else:
                # Para forma de montar 1- 7
                vector_corriente=[16, 20, 27, 36, 48, 66, 88, 116, 144, 175, 222, 268, 311, 353, 402, 474, 545, 652, 750]
        
        if value_corriente in vector_corriente:
            index = vector_corriente.index(value_corriente)
            value_seccion = vector_seccion_nominal[index]
            return value_seccion
        else:
            #Si el valor de la corriente no se encuentra en el vector, se aproxima al valor proximo pero mayor
            closest_corriente = min([c for c in vector_corriente if c > value_corriente])
            index = vector_corriente.index(closest_corriente)
            value_seccion = vector_seccion_nominal[index]
            return value_seccion
        

# Crear ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCables(root)
    root.mainloop()
