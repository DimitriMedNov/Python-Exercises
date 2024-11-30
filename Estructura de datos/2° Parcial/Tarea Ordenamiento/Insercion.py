# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:30:58 2021

@author: mednov
"""

def Insercion(lista):
    for i in range(1,10):
        aux = lista[i]
        p = i -1
        
        while(aux < lista[p] and p >= 1):
            lista[p+1] = lista[p]
            p = p-1
            
        if lista[p] <= aux:
            lista[p+1] = aux
            
        else:
            lista[p+1] = lista[p]
            lista[p] = aux    
            

cantidad = 10 
print (f"Ponga {cantidad} numeros: ")
        
mi_lista = []  

for i in range(cantidad):
    ingresado = input("Ingrese:") 
    mi_lista.append(ingresado)
    
print ("Original: ")
print(mi_lista)  
            

Insercion(mi_lista)
print("Ordenado: ")
print(mi_lista)