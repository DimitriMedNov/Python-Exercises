# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:25:53 2021

@author: MedNo
"""

import math

class NegativeNumber(Exception):
    "Excepcion de tipo numero negativo"
    pass

def raiz_cuadrada(number):
    if number < 0:
        raise ValueError("Numero negativo")
    return math.sqrt(number)