/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package caballos;

/**
 *
 * @author Renzo
 */
public class Caballo {
     private int[] movX = {2, 1, -1, -2, -2, -1, 1, 2};
    private int[] movY = {1, 2, 2, 1, -1, -2, -2, -1};
    private Tablero tablero;

    public Caballo(Tablero tablero) {
        this.tablero = tablero;
    }

    public boolean resolver(int x, int y, int paso) {
        int n = tablero.getN();

        if (paso == n * n) {
            return true;
        }

        for (int k = 0; k < 8; k++) {
            int nextX = x + movX[k];
            int nextY = y + movY[k];

            if (tablero.esValido(nextX, nextY)) {
                tablero.setPos(nextX, nextY, paso);
                if (resolver(nextX, nextY, paso + 1))
                    return true;
                else
                    tablero.setPos(nextX, nextY, -1); // retrocede
            }
        }
        return false;
    }
    public void mostrar(){
        System.out.println("Recorrido del caballo:");   
        tablero.mostrar();
    }
}

