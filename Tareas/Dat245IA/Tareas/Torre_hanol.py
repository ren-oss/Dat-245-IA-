import time
from collections import deque
import os


class Pila:
    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
    
    def ver_items(self):
        return list(self.items)
    
    def __len__(self):
        return len(self.items)

class Cola:
    def __init__(self):
        self.items = deque()
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()
    
    def esta_vacia(self):
        return len(self.items) == 0

# ---------- FUNCIONES ----------
def mostrar_torres(torres, n):
    """
    Dibuja las torres de forma gráfica en texto.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # limpia pantalla
    print("\n=== TORRES DE HANÓI ===\n")
    alturas = [t.ver_items() for t in torres]
    
    for nivel in range(n, 0, -1):
        linea = ""
        for torre in alturas:
            if len(torre) >= nivel:
                disco = torre[nivel-1]
                linea += f"{'=' * disco:^{n*2}} "
            else:
                linea += f"{'|':^{n*2}} "
        print(linea)
    print(" A".center(n*2), " B".center(n*2), " C".center(n*2))
    time.sleep(0.8)

def torres_de_hanoi_iterativo(n, origen, auxiliar, destino, registro, torres):
    pila_acciones = []
    pila_acciones.append((n, origen, auxiliar, destino, False))

    while pila_acciones:
        n, origen, auxiliar, destino, procesado = pila_acciones.pop()

        if n == 1:
            disco = origen.desapilar()
            destino.apilar(disco)
            registro.encolar(f"Mover disco {disco} de {origen.nombre} a {destino.nombre}")
            mostrar_torres(torres, N_GLOBAL)
        elif not procesado:
            pila_acciones.append((n - 1, auxiliar, origen, destino, False))
            pila_acciones.append((n, origen, auxiliar, destino, True))
            pila_acciones.append((n - 1, origen, destino, auxiliar, False))

# ---------- PROGRAMA PRINCIPAL ----------
if __name__ == "__main__":
    N_GLOBAL = int(input("Ingresa el número de discos (3-8 recomendado): "))
    
    # Crear las 3 torres
    A = Pila("A")
    B = Pila("B")
    C = Pila("C")

    # Inicializar torre A
    for i in range(N_GLOBAL, 0, -1):
        A.apilar(i)
    
    torres = [A, B, C]
    movimientos = Cola()
    
    mostrar_torres(torres, N_GLOBAL)
    torres_de_hanoi_iterativo(N_GLOBAL, A, B, C, movimientos, torres)
    
    print("\n--- MOVIMIENTOS REALIZADOS ---")
    while not movimientos.esta_vacia():
        print(movimientos.desencolar())

    print("\n ¡Completado! Todos los discos están en la torre C.")
