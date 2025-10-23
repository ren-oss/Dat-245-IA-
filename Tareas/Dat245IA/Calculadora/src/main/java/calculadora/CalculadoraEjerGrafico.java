/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package calculadora;
import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
/**
 *
 * @author Renzo
 */
public class CalculadoraEjerGrafico {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Calculadora");
        Calculadora calc = new Calculadora();
        JTextField display = new JTextField();
        display.setEditable(false);
        
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(4, 4));
        
        String[] botones = {
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        };
        
        for (String texto : botones) {
            JButton boton = new JButton(texto);
            boton.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    String cmd = e.getActionCommand();
                    if ("0123456789".contains(cmd)) {
                        display.setText(display.getText() + cmd);
                    } else if (cmd.equals("C")) {
                        display.setText("");
                        calc.limpiar();
                    } else if (cmd.equals("=")) {
                        try {
                            String expr = display.getText();
                            String[] partes;
                            double resultado = 0;
                            if (expr.contains("+")) {
                                partes = expr.split("\\+");
                                resultado = calc.sumar(Double.parseDouble(partes[0]), Double.parseDouble(partes[1]));
                            } else if (expr.contains("-")) {
                                partes = expr.split("-");
                                resultado = calc.restar(Double.parseDouble(partes[0]), Double.parseDouble(partes[1]));
                            } else if (expr.contains("*")) {
                                partes = expr.split("\\*");
                                resultado = calc.multiplicar(Double.parseDouble(partes[0]), Double.parseDouble(partes[1]));
                            } else if (expr.contains("/")) {
                                partes = expr.split("/");
                                resultado = calc.dividir(Double.parseDouble(partes[0]), Double.parseDouble(partes[1]));
                            }
                            display.setText(String.valueOf(resultado));
                        } catch (Exception ex) {
                            display.setText("Error");
                        }
                    } else { // Operadores
                        display.setText(display.getText() + " " + cmd + " ");
                    }
                }
            });
            panel.add(boton);
        }
        
        frame.setLayout(new BorderLayout());
        frame.add(display, BorderLayout.NORTH);
        frame.add(panel, BorderLayout.CENTER);
        
        frame.setSize(300, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
    
}
