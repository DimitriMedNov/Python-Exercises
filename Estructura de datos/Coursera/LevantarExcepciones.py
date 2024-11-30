# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:16:15 2021

@author: MedNo
"""

import math

def raiz_cuadrada(number):
    if number < 0:
        raise ValueError("Numero negativo")
    return math.sqrt(number)