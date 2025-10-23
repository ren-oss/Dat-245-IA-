import tkinter as tk
from tkinter import ttk, messagebox

# ----------------------------------------------------------
# ESTRUCTURAS DE DATOS: PILA Y COLA
# ----------------------------------------------------------

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, dato):
        self.items.append(dato)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def esta_vacia(self):
        return len(self.items) == 0


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, dato):
        self.items.insert(0, dato)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0


# ----------------------------------------------------------
# FUNCIONES AUXILIARES
# ----------------------------------------------------------

def es_operador(c):
    return c in "+-*/^"

def prioridad(op):
    if op in ('+', '-'): return 1
    if op in ('*', '/'): return 2
    if op == '^': return 3
    return 0


# ----------------------------------------------------------
# CONVERSIÓN INFIX → POSTFIX (usando PILA)
# ----------------------------------------------------------

def infix_a_postfix(expr):
    pila = Pila()
    cola = Cola()
    tokens = expr.split()

    for token in tokens:
        if token.isalnum():
            cola.encolar(token)
        elif token == '(':
            pila.apilar(token)
        elif token == ')':
            while not pila.esta_vacia() and pila.cima() != '(':
                cola.encolar(pila.desapilar())
            pila.desapilar()
        elif es_operador(token):
            while (not pila.esta_vacia() and
                   prioridad(pila.cima()) >= prioridad(token)):
                cola.encolar(pila.desapilar())
            pila.apilar(token)

    while not pila.esta_vacia():
        cola.encolar(pila.desapilar())

    # convertir la cola en lista de salida
    salida = []
    while not cola.esta_vacia():
        salida.append(cola.desencolar())
    return ' '.join(salida)


# ----------------------------------------------------------
# EVALUAR POSTFIX (usando PILA)
# ----------------------------------------------------------

def evaluar_postfix(expr):
    pila = Pila()
    tokens = expr.split()

    for token in tokens:
        if token.isdigit():
            pila.apilar(float(token))
        elif es_operador(token):
            b = pila.desapilar()
            a = pila.desapilar()
            if token == '+': pila.apilar(a + b)
            elif token == '-': pila.apilar(a - b)
            elif token == '*': pila.apilar(a * b)
            elif token == '/': pila.apilar(a / b)
            elif token == '^': pila.apilar(a ** b)

    return pila.desapilar()


# ----------------------------------------------------------
# CONVERSIÓN INFIX → PREFIX (usando PILA)
# ----------------------------------------------------------

def infix_a_prefix(expr):
    expr = expr[::-1]
    expr = expr.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    pila = Pila()
    salida = []

    for token in expr.split():
        if token.isalnum():
            salida.append(token)
        elif token == '(':
            pila.apilar(token)
        elif token == ')':
            while not pila.esta_vacia() and pila.cima() != '(':
                salida.append(pila.desapilar())
            pila.desapilar()
        elif es_operador(token):
            while (not pila.esta_vacia() and
                   prioridad(pila.cima()) > prioridad(token)):
                salida.append(pila.desapilar())
            pila.apilar(token)

    while not pila.esta_vacia():
        salida.append(pila.desapilar())

    return ' '.join(salida[::-1])


# ----------------------------------------------------------
# EVALUAR INFIX DIRECTA (con eval)
# ----------------------------------------------------------

def evaluar_infix(expr):
    try:
        return eval(expr)
    except Exception:
        return "Error"


# ----------------------------------------------------------
# INTERFAZ GRÁFICA (Tkinter)
# ----------------------------------------------------------

def convertir():
    expr = entrada.get()
    tipo = tipo_expr.get()

    if not expr:
        messagebox.showwarning("Aviso", "Ingrese una expresión.")
        return

    if tipo == "Infija":
        postfix = infix_a_postfix(expr)
        prefix = infix_a_prefix(expr)
        resultado.set(f"Prefija: {prefix}\nPostfija: {postfix}")
    elif tipo == "Postfija":
        try:
            val = evaluar_postfix(expr)
            resultado.set(f"Valor: {val}")
        except:
            resultado.set("Error en la expresión postfija")
    elif tipo == "Prefija":
        resultado.set("Conversión prefija aún no implementada totalmente.")
    else:
        resultado.set("Seleccione un tipo válido.")

def evaluar():
    expr = entrada.get()
    tipo = tipo_expr.get()

    if tipo == "Infija":
        val = evaluar_infix(expr)
    elif tipo == "Postfija":
        val = evaluar_postfix(expr)
    else:
        val = "Solo implementado para infija/postfija"

    resultado.set(f"Resultado: {val}")


# Ventana principal
root = tk.Tk()
root.title("Calculadora con Pilas y Colas")
root.geometry("480x360")
root.resizable(False, False)
root.configure(bg="#eef2f3")

titulo = tk.Label(root, text="Calculadora de Expresiones (Pilas y Colas)",
                  font=("Arial", 14, "bold"), bg="#eef2f3")
titulo.pack(pady=10)

frame = tk.Frame(root, bg="#eef2f3")
frame.pack(pady=10)

tk.Label(frame, text="Expresión:", bg="#eef2f3", font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5)
entrada = tk.Entry(frame, width=40, font=("Consolas", 12))
entrada.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Tipo:", bg="#eef2f3", font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=5)
tipo_expr = ttk.Combobox(frame, values=["Infija", "Prefija", "Postfija"], state="readonly")
tipo_expr.grid(row=1, column=1, padx=5, pady=5)
tipo_expr.set("Infija")

boton_convertir = tk.Button(root, text="Convertir", command=convertir, bg="#4a90e2", fg="white", font=("Arial", 11), width=15)
boton_convertir.pack(pady=5)

boton_evaluar = tk.Button(root, text="Evaluar", command=evaluar, bg="#50b35a", fg="white", font=("Arial", 11), width=15)
boton_evaluar.pack(pady=5)

resultado = tk.StringVar()
resultado_label = tk.Label(root, textvariable=resultado, font=("Consolas", 12), bg="#eef2f3", fg="#333", justify="left")
resultado_label.pack(pady=15)

root.mainloop()
