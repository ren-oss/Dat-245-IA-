/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package caballos;
import java.awt.BorderLayout;
import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;

/**
 *
 * @author Renzo
 */
public class MainTableroGrafico {

    /**
     * @param args the command line arguments
     */
    
    public static void main(String[] args) {
        // TODO code application logic here
        int n=5;
        Tablero tablero=new Tablero(n);
        tablero.inicializar();
        tablero.setPos(0, 0, 0); // posición inicial del caballo
        Caballo caballo=new Caballo(tablero);
        if(caballo.resolver(0, 0, 1))
            caballo.mostrar();
        else
            System.out.println("No tiene solución");
        JFrame frame = new JFrame("Recorrido del Caballo");
        JTextField display = new JTextField();
        display.setEditable(false);
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(n, n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                JButton boton = new JButton(tablero.getPos(i, j) == -1 ? "" : String.valueOf(tablero.getPos(i, j)));
                panel.add(boton);
            }
        }
        frame.add(display, BorderLayout.NORTH);
        frame.add(panel, BorderLayout.CENTER);
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setLocationRelativeTo(null); // Centrar la ventana
        /*Animaciones */
        frame.setVisible(true);
        frame.setLocationRelativeTo(null); // Centrar la ventana
        for (int k = 0; k < n * n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (tablero.getPos(i, j) == k) {
                        display.setText("Movimiento: " + k + " Posición: (" + i + ", " + j + ")");
                        try {
                            Thread.sleep(500); // Pausa de 500 milisegundos
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
            }
        }

    }
}