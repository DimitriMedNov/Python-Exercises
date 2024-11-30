/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tablahash;

//import java.lang.reflect.Array;
import java.util.Arrays;

/**
 *
 * @author Dimitri Medina Novelo
 */
public class TablaHash {

    /**
     * @param args the command line arguments
     */
    //Constructor
    String [] arreglo;
    int tamaño, contador;
    public TablaHash(int tam){
        tamaño=tam;
        arreglo=new String[tam];
        Arrays.fill(arreglo,"-1");
    }
    public void funcionHash(String[] cadenaArreglo, String[] arreglo){
        int i;
        for(i=0;i<cadenaArreglo.length;i++){
              String elemento=cadenaArreglo[i];
              int indiceArreglo=Integer.parseInt(elemento)%29;
              System.out.println("El indice es "+ indiceArreglo + " Para el Elemento o Valor "+ elemento);
              //Solucionador de colisiones
              while(arreglo[indiceArreglo]!="-1"){
                  indiceArreglo++;
                  System.out.println("Ocurrio una colision en el indice "+(indiceArreglo-1)+" Cambiar al indice "+indiceArreglo);
                  indiceArreglo%=tamaño;
              }
              arreglo[indiceArreglo]=elemento;
        }
    }
    //Metodo para mostrar la tabla 
    public void mostrar(){
        int incremento = 0,i,j;
        for (i = 0; i < 1; i++){
            incremento +=8;
            for (j = 0; j < 71; j++){
                 //System.out.print("-");
            }
            System.out.println();
            for (j = incremento - 30; j < incremento; j++){
                System.out.format("| %3s "+" ", j);
            }
            System.out.println("|");
            for (int n = 0; n < 71; j++){
                //System.out.println("-");
            }
            
            System.out.println();
            
            for (j = incremento - 30; j < incremento; j++){
                
                if (arreglo[j].equals("-1"))   {
                    System.out.println("|         ");
                }else {
                    System.out.format("| %3s "+" ", arreglo);
                }
            }
            System.out.println("|");
            for (j = 0; j < 71; j++){
                //System.out.println("-");
            }
            System.out.println();
        }
    }
    
    //Metodo para buscar Clave
    public String buscarClave(String elemento){
        int indiceArreglo=Integer.parseInt(elemento)%29;
        int contandor=0;
        while(arreglo[indiceArreglo]!="-1"){
            if(arreglo[indiceArreglo]==elemento){
                System.out.println("El elemento ("+ elemento + ") Fue encontrado  en el indice -----> "+ indiceArreglo);
                return arreglo[indiceArreglo];
            }
            indiceArreglo++;
            indiceArreglo%=tamaño;
            contador++;
            if(contador>7){
                break;
            }
        }
        return null;
    }
    
    //Main
    public static void main(String[] args) {
        // TODO code application logic here
        TablaHash hash = new TablaHash(30);
        String[] elementos={"4467","7637","7638","5737","3734","7186","7637","2893"}; 
        hash.funcionHash(elementos, hash.arreglo);
        //hash.mostrar();
        String buscar=hash.buscarClave("3734");
        if(buscar==null){
            System.out.println("El elemento no se encuentra en la tabla ");
        }
    }
    
}
