# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:23:19 2021

@author: mednov
"""

def Shell(lista):
    for i in range (0,9):
        aux = lista[i]
        p = i
        
        for j in range (i+1, 10):
            if(lista[j] < aux):
                aux = lista[j]
                p = j
                
        lista[p] = lista[i]
        lista[i] = aux
        

print("Cuantos numeros le gustaria ordenar: ")
cantidad=int(input())


print (f"Ponga {cantidad} numeros: ")

mi_lista = [] 

for i in range(cantidad):
    ingresado = input("Ingrese: ") 
    mi_lista.append(ingresado)
    
print ("Original: ")
print(mi_lista)  
            

Shell(mi_lista)
print("Ordenado: ")
print(mi_lista)
