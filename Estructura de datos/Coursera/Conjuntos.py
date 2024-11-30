# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 20:22:49 2021

@author: MedNo
"""

#No tienen elementos repetidos

frutas = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana', 'kiwi'}

'pera' in frutas
'yerba' in frutas

# Conjunto vacio
set()

# Otra formas de crear conjuntos
a = set('abracadabra')
b = set('alacazam')

# Operaciones dse conjunto
a - b #letras en a pero no en b
a | b #letras en a o en b o en ambas
a & b #letras en a y en b
a ^ b #letras en a o b pero no en ambos

# Comprension de conjuntos
a = {x for x in  'abracadabra' if x not in 'abc'}
