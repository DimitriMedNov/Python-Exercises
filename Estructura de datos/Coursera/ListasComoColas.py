# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:38:47 2021

@author: MedNo
"""

from collections import deque

#Listas como colas
queue = [1, 2, 3]

queue.append(4)
queue.append(5)

queue.pop()
queue.pop()

#Colas implementadas eficientemente en la libreria estandar

queue = deque([1, 2, 3])

#Agrego los elementos
queue.append(4)
queue.append(5)

#Sacar los elementos
queue.popleft()
queue.popleft()