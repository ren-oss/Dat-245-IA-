/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package caballos;



/**
 *
 * @author Renzo
 */
public class PilaCaballo {
    private int max=100;
    private Caballo v[]=new Caballo[max+1];
    private int tope;
    
    PilaCaballo ()
    {
	tope = 0;
    }
    boolean esvacia ()
    {
	if (tope == 0)
	    return (true);
	return (false);
    }
    boolean esllena ()
    {
	if (tope == max)
	    return (true);
	return (false);
    }
    int nroelem ()
    {
	return (tope);
    }
    void adicionar (Caballo elem)
    {
	if (!esllena ())
	{
	    tope++;
	    v [tope] = elem;
	}
	else
	    System.out.println ("Pila llena");
    }
    Caballo eliminar ()
    {
	Caballo elem = null;
	if (!esvacia ())
	{
	    elem = v [tope];
	    tope--;
	}
	else
	    System.out.println ("Pila vacia");
	return (elem);
    }
    void mostrar ()
    {
	Caballo elem;
	if (esvacia ())
	    System.out.println ("Pila vacia");
	else
	{
	    System.out.println ("\n Productos de la Pila ");
	    PilaCaballo aux = new PilaCaballo ();
	    while (!esvacia ())
	    {
		elem = eliminar ();
		aux.adicionar (elem);
		elem.mostrar();
	    }
	    vaciar(aux);
	}
    }
    void vaciar (PilaCaballo a)
    {
	while (!a.esvacia ())
	    adicionar (a.eliminar ());

    }
}
