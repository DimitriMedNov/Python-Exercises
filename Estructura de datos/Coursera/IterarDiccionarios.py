# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 00:40:59 2021

@author: MedNo
"""

precios = {'manzana':3.5, 'banana':4.5, 'kiwi':6.0, 'pera':3.75}

#  vistas de diccionarios
claves = precios.keys()

valores = precios.values()

items = precios.items()

precios['melon'] = 5.5
        
#  Iteración de diccionarios
for fruta, precio in precios.items():
    print("Precio de", fruta, ": $", precio)