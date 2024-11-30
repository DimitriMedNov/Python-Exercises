# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 06:57:29 2020

@author: Alien
"""

"""funciones importantes
variablelista=[]
max(variable lista)
min(variablelista)
sum(variablelista)
len(variablelista)
sum/len=prom
variablelista.append agrega miembro a lista
dic = dict(zip(nomdia,temp)) crea diccionario con dos listas
"""



importe = 0
opc=1
while opc==1: 
     
     cantcliente = int(input(f"ingrese cantidad de clientes que atenderá :"))
     subtotal = 0
     comision = 0
     for q in range(cantcliente):
          sexo = int(input(f"ingrese sexo del cliente {q+1}: M=1 o F=2"))
          pago = int(input(f"ingrese forma de pago del cliente {q+1}: Efectivo=1 Tarjeta=2"))
          if sexo == 2:
               subtotal = 250
               print("subtotal: ", subtotal)
          elif sexo == 1:
               subtotal = 150
               print("subtotal: ", subtotal)
                    
          if pago == 1:
               
               desc=.05
               total = subtotal - (subtotal*desc) 
               comision = 0          
          elif pago == 2:
               comision = .05
               total = subtotal + (subtotal * comision)
               desc = 0
          print(f"Cliente {q+1}  ")     
          print("Sexo: Masculino=1 Femenino=2  ", sexo)
          print("pago: Efectivo=1  Tarjeta=2  ", pago)
         
          print("descuento: ", (subtotal*desc))
          print("subtotal: ", subtotal)
          print("total del usuario: ", total)
     opc = int(input("Desea repetir? 1=Y / 2 =N"))
          
