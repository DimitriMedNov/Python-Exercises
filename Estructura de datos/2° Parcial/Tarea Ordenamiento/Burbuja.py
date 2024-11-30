8# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:11:06 2021

@author: mednov
""" 
    
def Burbuja(lista):
    for numPasada in range(len(lista)-1,0,-1):
        for i in range(numPasada):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                
#print("Cuantos numeros deseas ordenar: ")
cantidad=5

# cantidad=[None]*cantidad

# X=cantidad-1

# print (f"Inserta {cantidad} numeros: ")
        
mi_lista = [12,345,34,35,35]  

# for i in range(cantidad):
#     ingresado = input("Ingrese:") 
#     mi_lista.append(ingresado)
    
print ("Original: ")
print(mi_lista)  
            

Burbuja(mi_lista)
print("Ordenado: ")
print(mi_lista)

#prof no se pq  me da problemas al momento de runnearlo cuando el codigo le pide los datos al usario