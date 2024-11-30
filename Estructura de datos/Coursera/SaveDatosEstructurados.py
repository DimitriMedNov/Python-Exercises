# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:16:15 2021

@author: MedNo
"""
import json

# serializar un objeto
json.dumps([1, 2, 3])

# deserializar un objeto
json.loads('[1, 2, 3]')

# Escribir como json directamente a un archivo
with open('/Users/MedNo/OneDrive/Escritorio/Programacion/Estructura de datos/Coursera/Hola Mundo 4.txt', 'w') as a_file:
    json.dump([1, 2, 3,], a_file)
    
# Leer un json directamente desde un archivo
with open('/Users/MedNo/OneDrive/Escritorio/Programacion/Estructura de datos/Coursera/Hola Mundo 4.txt', 'r') as a_file:
    a_list = json.load(a_file)