# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:58:05 2021

@author: MedNo
"""

a_list = [1, 2, 3, 4, 5]

#Devuelve el indice del parametro
a_list.index(4)

#Lanza una excepcion del tipo ValueError
a_list.index(6)

#Opciones indicando una sublista
a_list.index(4, 1)
a_list.index(4, 0, 2)
a_list.index(4, 1, 4)
