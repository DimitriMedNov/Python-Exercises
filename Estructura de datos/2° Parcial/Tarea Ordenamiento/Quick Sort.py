# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:21:55 2021

@author: mednov
"""

def Quick_sort(lista):
    Quick_sort_Aux(lista, 0, len(lista)-1)
    
def Quick_sort_Aux(lista, principio, final):
    if principio < final:
        punto_particion = partir(lista, principio, final)
        
        Quick_sort_Aux(lista, principio, punto_particion -1)
        Quick_sort_Aux(lista, punto_particion +1, final)
        
def partir(lista, principio, final):
    pivote = lista[principio]
    
    izq = principio +1 
    der = final 
    terminado = False
    
    while not terminado:
        while izq<=der and lista[izq] <= pivote:
            izq += 1
            
        while lista[der] >= pivote and der >= izq:
            der -=1
            
        if der < izq:
            terminado = True 
        else:
            temporal = lista[izq]
            lista[izq] = lista[der]
            lista[der] = temporal 
            
    temporal = lista[principio]
    lista[principio] = lista[der]
    lista[der] = temporal 
    
    return der


print("Cuantos numeros le gustaria ordenar: ")
cantidad=int(input())

Cantidad=[None]*cantidad
X=cantidad-1

print (f"Ponga {cantidad} numeros: ")
        
mi_lista = []  

for i in range(cantidad):
    ingresado = input("Ingrese:") 
    mi_lista.append(ingresado)
    
print ("Original: ")
print(mi_lista)  
            
Quick_sort(mi_lista)
print("Ordenado: ")
print(mi_lista)
    