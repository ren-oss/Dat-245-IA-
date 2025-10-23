import turtle

# ---------- FUNCION PARA DIBUJAR LA CURVA ----------
def hilbert(t, orden, angulo, paso):
    """
    Dibuja una curva de Hilbert usando recursión.
    
    t: objeto Turtle
    orden: nivel de profundidad (1, 2, 3, ...)
    angulo: ángulo de giro (normalmente 90°)
    paso: longitud de cada segmento
    """
    if orden == 0:
        return
    
    t.right(angulo)
    hilbert(t, orden - 1, -angulo, paso)
    t.forward(paso)
    t.left(angulo)
    hilbert(t, orden - 1, angulo, paso)
    t.forward(paso)
    hilbert(t, orden - 1, angulo, paso)
    t.left(angulo)
    t.forward(paso)
    hilbert(t, orden - 1, -angulo, paso)
    t.right(angulo)

# ---------- PROGRAMA PRINCIPAL ----------
if __name__ == "__main__":
    # Configurar ventana
    wn = turtle.Screen()
    wn.title("Curva de Hilbert - Método Gráfico 🌀")
    wn.bgcolor("black")

    # Crear tortuga
    t = turtle.Turtle()
    t.color("cyan")
    t.speed(0)  # Máxima velocidad
    t.pensize(2)

    # Parámetros
    orden = int(input("Ingresa el orden de la curva (1-7 recomendado): "))
    paso = 10  # tamaño de cada segmento
    tamaño = paso * (2 ** orden - 1)

    # Posicionar al inicio
    t.penup()
    t.goto(-tamaño / 2, tamaño / 2)
    t.pendown()

    # Dibujar la curva
    hilbert(t, orden, 90, paso)

    # Terminar
    t.hideturtle()
    wn.mainloop()
