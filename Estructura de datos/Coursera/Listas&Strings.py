# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:22:56 2021

@author: MedNo
"""

nombre = 'Agustin'

lista = list(nombre)

#El indexado funciona de igual manera
nombre[0]
lista[0]

#El slincing funciona de igual manera
nombre[:4]
lista[:4]

#La funcion len funciona de igual manera
len(nombre)
len(lista)

#El in funciona en ambas
'A' in nombre
'A' in lista

#El not in funciona en ambas
'z' not in nombre
'z' not in lista

#Los Strings tambien se pueden recorrer con un for
for letra in nombre:
    print(letra)
    
#Los Strings son inmutables
lista[2] = 'o'
nombre[2] = 'o' #TytpeError

'Hola' + nombre
nombre + '!!'
nombre[:2] + 'o' + nombre[3:]