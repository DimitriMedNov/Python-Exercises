# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:52:02 2021

@author: MedNo
"""

# Abrir archivo
a_file = open('C:/Users/MedNo/OneDrive/Escritorio/Programacion/Estructura de datos/Coursera/Hola Mundo.txt', 'r')

# Leer todo el contenido del archivo
a_file.read()

#Cerrar archivo
a_file.close()

# Abrir un archivo como un context manager utilizando la sentencia with.

with open('/Users/MedNo/OneDrive/Escritorio/Programacion/Estructura de datos/Coursera/Hola Mundo.txt', 'r') as a_file:
    a_file.read()