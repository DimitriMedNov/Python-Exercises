/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package ordenamiento;

import java.util.Scanner;

public class Funciones {
    Scanner sc = new Scanner(System.in);
    
    private int[] fact;
    private int size, IDX = -1;
    
    public Funciones(int _size){
        this.size = _size;
        this.fact = new int[this.size];
    }
    
    public void add (int _fact){
        this.IDX++;
        if(this.IDX < this.size) {
            this.fact[this.IDX] = _fact;
        }
    }
    
    public void showfacts(){
        for(int i = 0; i<this.size; i++){
            System.out.print(this.fact[i] + "\t");
        }
        
        System.out.println();
    }
    
//TIPOS DE ORDENAMIENTO
    
    public void bubble_order(){
        for(int i = 0; i < this.size - 1; i++){
            for(int j = i + 1; j < this.size; j++){
                if(this.fact[i] > this.fact[j]){
                    int Aux = this.fact[i];
                    this.fact[i] = this.fact[j];
                    this.fact[j] = Aux;
                }
            }
        }
    }
    
    public void order_for_selection(){
        for(int i = 0; i < this.size; i++){ 
            int iless = i;
            
            for(int j = i + 1; j < this.size; j++){ 
                if(this.fact[iless] > this.fact[j]){
                    iless = j;
                }
            }
            
            if(i != iless){
                int Aux = this.fact[i];
                this.fact[i] = this.fact[iless];
                this.fact[iless] = Aux;
            }
        }
    }
    
    public void order_for_insertion(){
        for(int i = 0; i < this.size; i++){
            System.out.print("Numero " + (i + 1) + ": ");
            
            int _number = sc.nextInt();
            int j = i;
            
            if(j > 0){
                int Aux = this.fact[j - 1];
                
                while(_number < Aux && j > 0){
                    this.fact[j] = this.fact[j - 1];
                    j = j - 1;
                    
                    if(j > 0){
                        Aux = this.fact[j - 1];
                    }
                }
            }
            this.fact[j] = _number;
        }
        this.showfacts();
    }
    
    public void exchange(int _i, int _j){
        int Aux = this.fact[_i];
        this.fact[_i] = this.fact[_j];
        this.fact[_j] = Aux;
    }
    
    public void order_for_shell(){
        int interval = this.size / 2;
        
        while(interval > 0){
            for(int i = interval; i < this.size; i++){
                int j = i - interval;
                
                while(j >= 0){
                    int k = j + interval;
                    
                    if(this.fact[j] <= this.fact[k]){
                        j = -1;
                    }
                    
                    else{
                        this.exchange(j, j + 1);
                        j = j-interval;
                    }
                }
            }
            interval = Math.round(interval / 2);
        }
    }
    
    public void order_for_quicksort(int _first, int _last){
        int central = Math.round((_first + _last) / 2);
        int pivot = this.fact[central];
        int i = _first;
        int j = _last;
        
        do{
            while(this.fact[i] < pivot){
                i = i + 1;
            }
            
            while(this.fact[j] > pivot){
                j = j - 1;
            }
            
            if(i <= j){
                this.exchange(i, j);
                i = i + 1;
                j = j - 1;
            }
            
        }while(i < j);
        
        if(_first < j){
            this.order_for_quicksort(_first, j);
        }
        
        if(_last > i){
            this.order_for_quicksort(i, _last);
        }
    }
}
