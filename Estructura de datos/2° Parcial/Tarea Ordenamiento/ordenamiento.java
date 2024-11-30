/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ordenamiento;

public class ordenamiento {
   public static void main(String[] args){
       System.out.println("Ordenamientos");
       
       System.out.println("Bubble");
       Funciones o1 = new Funciones(7);
       
       o1.add(94);
       o1.add(49);
       o1.add(75);
       o1.add(79);
       o1.add(10);
       o1.add(89);
       o1.add(64);
       
       System.out.println("Sin Bubble");
       o1.showfacts();
       
       System.out.println("Con Bubble");
       o1.bubble_order();
       o1.showfacts();
       
       System.out.println("\nSeleccion");
      Funciones o2 = new Funciones(6);

       o2.add(235);
       o2.add(2345);
       o2.add(233);
       o2.add(486);
       o2.add(749);
       o2.add(625);

       System.out.println("Sin Seleccion");
       o2.showfacts();

       System.out.println("Con Seleccion");
       o2.order_for_selection();
       o2.showfacts();
       
       System.out.println("\nInserccion");
       Funciones o3 = new Funciones(5);
       
       System.out.println("\nOrdenados con Inserccion");
       o3.order_for_insertion();
       
       System.out.println("\nShell");
       Funciones o4 = new Funciones(9);

       o4.add(45);
       o4.add(789);
       o4.add(54);
       o4.add(9);
       o4.add(79);
       o4.add(82);
       o4.add(63);
       o4.add(23);
       o4.add(35);

       System.out.println("Sin Shell");
       o4.showfacts();

       System.out.println("Con Shell");
       o4.order_for_shell();
       o4.showfacts();
       
       System.out.println("\nQuicksort");
       Funciones o5 = new Funciones(10);

       o5.add(648);
       o5.add(51545);
       o5.add(45648);
       o5.add(48944);
       o5.add(51687);
       o5.add(48);
       o5.add(46735);
       o5.add(54868);
       o5.add(16488);
       o5.add(78943);

       System.out.println("Sin Quicksort ");
       o5.showfacts();

       System.out.println("Con Quicksort");
       o5.order_for_quicksort(0, 4);
       o5.showfacts();
   }
}