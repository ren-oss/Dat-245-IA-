/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package caballos;

/**
 *
 * @author Renzo
 */
public class Tablero {
    private int[][] tablero;
    private int n; // tamaño del tablero (n x n)

    public Tablero(int n) {
        this.n = n;
        tablero = new int[n][n];
        inicializar();
    }

    public void inicializar() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                tablero[i][j] = -1; // casilla no visitada
            }
        }
    }

    public void mostrar() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.printf("%2d ", tablero[i][j]);
            }
            System.out.println();
        }
    }

    public boolean esValido(int x, int y) {
        return (x >= 0 && x < n && y >= 0 && y < n && tablero[x][y] == -1);
    }

    public void setPos(int x, int y, int paso) {
        tablero[x][y] = paso;
    }
    public int getPos(int x, int y) {
        return tablero[x][y];
    }

    public int getN() {
        return n;
    }

    public int[][] getTablero() {
        return tablero;
    }

    public void setTablero(int[][] tablero) {
        this.tablero = tablero;
    }

    public void setN(int n) {
        this.n = n;
    }
    
}
