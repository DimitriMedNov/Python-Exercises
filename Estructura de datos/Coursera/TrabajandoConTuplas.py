# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 23:29:33 2021

@author: MedNo
"""

tupla = (1, 2.5, 'Hola')

tupla[0] #1
tupla[1] #2.5
tupla[2] #'Hola

tupla[:2]  #(1, 2.5)

#Tupla vacia
tupla_vacia_1 = ()
tupla_vacia_2 = tuple()

# Tupla de un elemento.
tupla_2 = (5,) #Es una tupla
numero = (5) #Es un número

#Son inmutables
tupla[2] = 3
#Longitud de una tupla
len(tupla)