# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 00:32:58 2021

@author: MedNo
"""

precios = {'manzana':3.5, 'bananas':4.5, 'kiwi': 6.0, 'pera':3.75}

# Cantidad de elenentos clave-valor
len(precios)

# Obtiene el vator para tas clave indicada, se puede indicar un default si no existe.
precios.get('manzana')
precios.get('melon')
precios.get('melon', 0.00)

# Si existe devuelve el valor, sino to crea con el valor default o si no se inidca el default con None.
precios.setdefault('banana')
precios.setdefault('sandia', 6.7)

# Actualización de un diccionario
precios.update({'banana': 4.0, 'durazno': 5.5})
precios.update([('durazno', 5.5)])

# me devuelve una vista con las claves del diccionario
precios.keys()

# me devuelve una vista con los valores del diccionario
precios.values()

# me devuelve una vista con los itens del diccionario
precios.items()

#  Saca el elenento de la clave indicada, se puede poner un default si no existe
precios.pop('manzana')
precios.pop('melon', 0.00)
precios.pop('melon')

# Saca un elenento siguiendo el orden: LIFO
precios.popitem()

# Copia superficial de los diccionarios
copia_precios = precios.copy()

# Borra todos los elenentos
precios.clear()