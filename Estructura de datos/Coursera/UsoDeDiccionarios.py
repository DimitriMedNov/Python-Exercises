# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 00:11:47 2021

@author: MedNo
"""

#Formas de definir un diccionario
precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75}
precios = dict(manzana=3.5, banana=4.5, kiwi=6.0, pera=3.75)
precios = dict([('manzana', 3.5), ('banana', 4.5), ('kiwi', 6.0), ('pera', 3.75)])

# Acceso a los elementos por claves
precios['manzana']       # 3.5
precios[ 'banana']       # 4.5
precios['kiwi']          #6.0
precios['pera']          # 3.75
precios['melon']         #KeyError

# Agregar un elemento (clave-valor)
precios ['melon'] = 5.75

# Actualizar un elemento (clave-valor)
precios['manzana'] = 3.0

# Borrar un elemento (clave-valor)
del precios['kiwi']

# Pertenencia
'banana' in precios
'sandia' not in precios

