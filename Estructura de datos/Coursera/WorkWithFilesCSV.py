# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:30:57 2021

@author: MedNo
"""
import csv

#Leer un archivo CSV
with open('/Users/MedNo/OneDrive/Escritorio/Programacion/Estructura de datos/Coursera/Hola Mundo CSV 1.txt', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))


#Escribir un archivo CSV
with open('/Users/MedNo/OneDrive/Escritorio/Programacion/Estructura de datos/Coursera/Hola Mundo CSV 1.txt', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Pedro', 'Gont', '9996481677','qpd42@gmail.com'])