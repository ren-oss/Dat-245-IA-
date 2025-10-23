/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package calculadora;

/**
 *
 * @author Renzo
 */
public class Calculadora {
    // Atributos
    private double resultado;

    // Constructor
    public Calculadora() {
        resultado = 0;
    }

    // Métodos de operaciones básicas
    public double sumar(double a, double b) {
        resultado = a + b;
        return resultado;
    }

    public double restar(double a, double b) {
        resultado = a - b;
        return resultado;
    }

    public double multiplicar(double a, double b) {
        resultado = a * b;
        return resultado;
    }

    public double dividir(double a, double b) {
        if (b == 0) {
            System.out.println("Error: División entre cero no permitida.");
            return 0;
        }
        resultado = a / b;
        return resultado;
    }

    // Método para obtener el último resultado guardado
    public double getResultado() {
        return resultado;
    }

    // Método para reiniciar la calculadora
    public void limpiar() {
        resultado = 0;
    }
    public void mostrar(){
        System.out.println("Resultado: " + resultado);
    }
}
