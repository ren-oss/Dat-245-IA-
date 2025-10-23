/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package calculadora;

/**
 *
 * @author Renzo
 */
public class ColaC {
    private int max=50;
    private Calculadora v[]=new Calculadora[max+1];
    private int ini,fin;
    
    ColaC()
    {
        ini=fin=0;
    }
    boolean esvacia()
    {
        if(ini==0 && fin==0)
            return true;
        return false;
    }
    boolean esllena()
    {
        if(fin==max)
            return true;
        return false;
    }
    int nroelem()
    {
        return fin-ini;
    }
    void adicionar(Calculadora elem)
    {
        if(!esllena())
        {
            v[fin+1]=elem;
            fin=fin+1;
        }
        else
            System.out.println("Cola llena...");
    }
    Calculadora eliminar()
    {
        Calculadora elem=null;
        if(!esvacia())
        {
            elem=v[ini+1];
            ini=ini+1;
            if(ini==fin)
                ini=fin=0;
        }
        else
            System.out.println("Cola Vacia...");
        return elem;
    }
    void mostrar()
    {
        ColaC aux=new ColaC();
        
        while(!esvacia())
        {
            Calculadora px=eliminar();
            px.mostrar();
            aux.adicionar(px);
        }
        vaciar(aux);
    }
    void vaciar(ColaC z)
    {
        while(!z.esvacia())
            adicionar(z.eliminar());
    }

}
