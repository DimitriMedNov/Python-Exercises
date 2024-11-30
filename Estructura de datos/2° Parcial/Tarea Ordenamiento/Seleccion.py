# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:35:05 2021

@author: mednov
"""

def seleccion(lista):
  
    n = len(lista)-1

    while n > 0:
        p = buscar_max(lista, 0, n)
        
        lista[p], lista[n] = lista[n], lista[p]

        n = n - 1

def buscar_max(lista, ini, fin):

    pos_max = ini
    for i in range(ini+1, fin+1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max
        
print("Cuantos numeros deseas agregar: ")
cantidad=int(input())

calificacion=[None]*cantidad
X=cantidad-1

print (f"Ponga {cantidad} numeros: ")
        
mi_lista = []  

for i in range(cantidad):
    ingresado = input("Ingrese:") 
    mi_lista.append(ingresado)
    
print ("Original: ")
print(mi_lista)  
            

seleccion(mi_lista)
print("Ordenado: ")
print(mi_lista)