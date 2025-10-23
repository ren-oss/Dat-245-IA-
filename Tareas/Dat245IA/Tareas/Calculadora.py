import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- FUNCIONES DE CONVERSIÓN Y EVALUACIÓN ---------------- #

def es_operador(c):
    return c in ['+', '-', '*', '/', '^']

def prioridad(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0

# -------- INFIX A POSTFIX -------- #
def infija_a_postfija(expresion):
    pila = []
    salida = []
    for token in expresion.split():
        if token.isalnum():  # número o variable
            salida.append(token)
        elif token == '(':
            pila.append(token)
        elif token == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()
        else:
            while pila and prioridad(pila[-1]) >= prioridad(token):
                salida.append(pila.pop())
            pila.append(token)
    while pila:
        salida.append(pila.pop())
    return ' '.join(salida)

# -------- INFIX A PREFIX -------- #
def infija_a_prefija(expresion):
    expresion = expresion[::-1]
    expresion = expresion.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    expresion = expresion[::-1]
    postfija = infija_a_postfija(expresion[::-1])
    prefija = postfija.split()[::-1]
    return ' '.join(prefija)

# -------- EVALUAR POSTFIJA -------- #
def evaluar_postfija(expresion):
    pila = []
    pasos = []
    for token in expresion.split():
        if token.isdigit():
            pila.append(int(token))
        elif es_operador(token):
            b = pila.pop()
            a = pila.pop()
            if token == '+': pila.append(a + b)
            elif token == '-': pila.append(a - b)
            elif token == '*': pila.append(a * b)
            elif token == '/': pila.append(a / b)
            elif token == '^': pila.append(a ** b)
        pasos.append(str(pila))
    return pila[-1], pasos

# -------- EVALUAR PREFIJA -------- #
def evaluar_prefija(expresion):
    pila = []
    pasos = []
    for token in expresion.split()[::-1]:
        if token.isdigit():
            pila.append(int(token))
        elif es_operador(token):
            a = pila.pop()
            b = pila.pop()
            if token == '+': pila.append(a + b)
            elif token == '-': pila.append(a - b)
            elif token == '*': pila.append(a * b)
            elif token == '/': pila.append(a / b)
            elif token == '^': pila.append(a ** b)
        pasos.append(str(pila))
    return pila[-1], pasos

# ---------------- FUNCIONES DE INTERFAZ ---------------- #

def calcular():
    expresion = entrada_expr.get()
    tipo = tipo_expr.get()
    
    if not expresion.strip():
        messagebox.showwarning("Atención", "Por favor ingresa una expresión.")
        return

    try:
        if tipo == "Infija":
            post = infija_a_postfija(expresion)
            pre = infija_a_prefija(expresion)
            res, pasos = evaluar_postfija(post)
            salida_post.config(text=f"Postfija: {post}")
            salida_pre.config(text=f"Prefija: {pre}")
        elif tipo == "Postfija":
            res, pasos = evaluar_postfija(expresion)
            salida_post.config(text=f"Postfija: {expresion}")
            salida_pre.config(text="Prefija: (no aplica)")
        elif tipo == "Prefija":
            res, pasos = evaluar_prefija(expresion)
            salida_pre.config(text=f"Prefija: {expresion}")
            salida_post.config(text="Postfija: (no aplica)")
        else:
            return
        
        salida_res.config(text=f"Resultado: {res}")
        salida_pasos.config(text="Pasos:\n" + '\n'.join(pasos))
    
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# ---------------- INTERFAZ GRÁFICA ---------------- #

ventana = tk.Tk()
ventana.title("Calculadora de Expresiones (Infija, Prefija, Postfija)")
ventana.geometry("600x500")
ventana.configure(bg="#1a1a1a")

# Entrada
tk.Label(ventana, text="Expresión:", bg="#1a1a1a", fg="white", font=("Arial", 12)).pack(pady=5)
entrada_expr = tk.Entry(ventana, width=50, font=("Consolas", 12))
entrada_expr.pack(pady=5)

# Tipo
tk.Label(ventana, text="Tipo de expresión:", bg="#1a1a1a", fg="white", font=("Arial", 12)).pack(pady=5)
tipo_expr = ttk.Combobox(ventana, values=["Infija", "Prefija", "Postfija"], state="readonly")
tipo_expr.current(0)
tipo_expr.pack(pady=5)

# Botón Calcular
tk.Button(ventana, text="Calcular", command=calcular, bg="#008CBA", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

# Salidas
salida_pre = tk.Label(ventana, text="Prefija:", bg="#1a1a1a", fg="cyan", font=("Consolas", 11))
salida_pre.pack()

salida_post = tk.Label(ventana, text="Postfija:", bg="#1a1a1a", fg="lime", font=("Consolas", 11))
salida_post.pack()

salida_res = tk.Label(ventana, text="Resultado:", bg="#1a1a1a", fg="yellow", font=("Consolas", 11, "bold"))
salida_res.pack(pady=5)

salida_pasos = tk.Label(ventana, text="", bg="#1a1a1a", fg="#cccccc", font=("Consolas", 10), justify="left")
salida_pasos.pack(pady=5)

ventana.mainloop()
