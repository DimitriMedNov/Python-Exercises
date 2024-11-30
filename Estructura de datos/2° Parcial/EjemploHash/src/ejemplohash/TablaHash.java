/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejemplohash;

/**
 *
 * @author Dimitri Medina Novelo
 */
public class TablaHash {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       //Arreglo de almacenamiento en la tabla
       Maestro.Tam = 15;
       Maestro []arrayProf = new Maestro[Maestro.Tam];
       
       System.out.println("Profes: \n");
       
       Maestro a = new Maestro(1685, "Viridiana Pacheco ");
       arrayProf[a.hashCode()]=a;
       System.out.println("Profe: Viridiana Pacheco" + "|| id: 1685 ");
       System.out.println("Metodo Hash: "+a.hashCode());
       System.out.println("\n");
       
       a = new Maestro(5461, "Carlos Lara");
       arrayProf[a.hashCode()]=a;
       System.out.println("Profe: Carlos Lara" + "|| id: 5461");
       System.out.println("Metodo Hash: "+a.hashCode());
       System.out.println("\n");
       
       a = new Maestro(7894, "Sergio Arjona");
       arrayProf[a.hashCode()]=a;
       System.out.println("Profe: Sergio Arjona" + "|| id: 7894");
       System.out.println("Metodo Hash: "+a.hashCode());
       System.out.println("\n");
       
       Alumno.Tam = 10;
       Alumno []arrayStudnt = new Alumno[Alumno.Tam];
       
       System.out.println("Alumnos: \n");
       
       Alumno b = new Alumno(2131, "Roberto Randolph");
       arrayStudnt[b.hashCode()]=b;
       System.out.println("Alumno: Roberto Randolph" + "|| id: 2131");
       System.out.println("Metodo Hash: "+b.hashCode());
       System.out.println("\n");
       
       b = new Alumno(3969, "Dimitri Medina");
       arrayStudnt[b.hashCode()]=b;
       System.out.println("Alumno: Dimitri Medina" + "|| id: 3969");
       System.out.println("Metodo Hash: "+b.hashCode());
       System.out.println("\n");
       
       b = new Alumno(3974, "Mike Canto");
       arrayStudnt[b.hashCode()]=b;
       System.out.println("Alumno: Mike Canto" +  "|| id: 3974");
       System.out.println("Metodo Hash: "+b.hashCode());
       System.out.println("\n");
    }
    
}