/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package caballos;



/**
 *
 * @author Renzo
 */
public class ColaTablero {
    private int max=50;
    private Tablero v[]=new Tablero[max+1];
    private int ini,fin;
    
    ColaTablero()
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
    void adicionar(Tablero elem)
    {
        if(!esllena())
        {
            v[fin+1]=elem;
            fin=fin+1;
        }
        else
            System.out.println("Cola llena...");
    }
    Tablero eliminar()
    {
        Tablero elem=null;
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
        ColaTablero aux=new ColaTablero();
        
        while(!esvacia())
        {
            Tablero px=eliminar();
            px.mostrar();
            aux.adicionar(px);
        }
        vaciar(aux);
    }
    void vaciar(ColaTablero z)
    {
        while(!z.esvacia())
            adicionar(z.eliminar());
    }

    
}
