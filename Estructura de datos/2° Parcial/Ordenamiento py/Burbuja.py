# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:11:06 2021

@author: mednov
""" 
    
def Burbuja(lista):
    for array in range(len(lista)-1,0,-1):
        for i in range(array):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

cantidad = int(input("Cuantos numeros deseas ordenar: "))
             


mi_lista = [None]*cantidad
X=cantidad-1

for i in range(cantidad):
    item = int(input("Ingrese:"))
    mi_lista[i] = item
    
print ("Original: ")
print(mi_lista)  
            

Burbuja(mi_lista)
print("Ordenado: ")
print(mi_lista)

