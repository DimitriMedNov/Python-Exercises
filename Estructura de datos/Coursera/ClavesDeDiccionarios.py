# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 00:46:33 2021

@author: MedNo
"""
import datetime

a_dict = dict()

# Clave
a_dict['clave'] = 1
a_dict[1] = 1
a_dict[1.5] = 1
a_dict[(1, 2)] - 1

a_dict[datetime.date.today ()] = 1

# Una lista es un contenedor no inmutable, no puede ser hasheable
a_dict[[1, 2]] = 1

# Lo mismo con los conjuntos
a_dict[{'a'}] = 1

# Lo mismo con los diccionarios
a_dict[{'a': 1}] = 1