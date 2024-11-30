# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:28:44 2021

@author: MedNo
"""

#Escribir un String en el archivo
with open('/Users/MedNo/OneDrive/Escritorio/Programacion/Estructura de datos/Coursera/Hola Mundo 3.txt', 'w') as a_file:
    a_file.write('Hola mundo!')
    
#Escribir muchas lineas en el archivo
with open('/Users/MedNo/OneDrive/Escritorio/Programacion/Estructura de datos/Coursera/Hola Mundo 3.txt', 'w') as a_file:
    a_file.writelines(['Linea 1.\n','Linea 2.\n','Linea 3.\n','Linea 4.\n'])
    
#Escribir un String en el archivo, agregandolo al final del mismo
with open('/Users/MedNo/OneDrive/Escritorio/Programacion/Estructura de datos/Coursera/Hola Mundo 3.txt', 'a') as a_file:
    a_file.write('Hola mundo!')


with open('/Users/MedNo/OneDrive/Escritorio/Programacion/Estructura de datos/Coursera/Hola Mundo 3.txt', 'w') as a_file:
    a_file.write(100)
    


with open('/Users/MedNo/OneDrive/Escritorio/Programacion/Estructura de datos/Coursera/Hola Mundo 3.txt', 'r+') as a_file:
    a_file.write('Hola mundo!')
    
with open('path_to_file', 'x') as a_file:
    a_file.write('Hola mundo!')