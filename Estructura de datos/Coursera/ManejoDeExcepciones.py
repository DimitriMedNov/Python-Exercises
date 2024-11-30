# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 09:53:12 2021

@author: MedNo
"""
t = 1/0

try:
    t = 1/0
except ZeroDivisionError:
    print("Division por cero")
    

def find(elemento, lista):
    """Devuelve el indice donde se encuentra el @elemento de la lista.
        Si no lo encuentra devuelve -1.
    """
    index = 0
    while True:
        try:
            if lista[index] == elemento:
                return index
        except IndexError:
            return -1
        index += 1
            
# elemplos de find
find(4,[2, 3, 4, 5])
find(1,[2, 3, 4, 5])


def divide(x, y):
    "Divide dos numeros"
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division por cero")
    else:
        print("El resultado es: ", result)
    finally:
        print("ejecutando la clausula finally")
        
# elemplos de divide
divide(2, 1)
divide(2, 0)