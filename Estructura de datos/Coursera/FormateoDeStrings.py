# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:38:06 2021

@author: MedNo
"""
import string

name = 'Micho'
prueba = 'Prueba'
formatter = string.Formatter()
formatter.format('Hola {}', name)

'Hola {}'.format(name)

'{} + {} = {}'.format(2,5,7)

'{1} + {2} = {0}'.format(7, 5, 2)

'Hola {name}'.format(name=name)

'{0} + {1} = {result}'.format(2, 5, result=7)

'{0:f} + {1:f} = {result:f}'.format(2, 5, result=7)

'{0:.3f} + {1:.3f} = {result:.3f}'.format(2, 5, result=7)

'{:d}'.format(25)

'{:.0f}'.format(25.50)

'Hola {name:16}'.format(name=name)

'Hola {name:<16}'.format(name=name)

'Hola {name:>16}'.format(name=name)

'Hola {name:^16}'.format(name=name)

'Hola {name:*^16}'.format(name=name)

#Examen Semana 1

'{2} - {0} - {1}'.format(1, 2, 3)

'{:d}'.format(2.5) #ValueError

'{:*^10}'.format(prueba)

nro_cuenta = 32673

saldo = 100.2543

'El saldo de la cuenta {} es ${:.2f}'.format(nro_cuenta,saldo)

'El saldo de la cuenta {:s} es ${:.2f}'.format(nro_cuenta,saldo)#Value Error

'El saldo de la cuenta {:d} es ${}'.format(nro_cuenta,saldo)

'El saldo de la cuenta {} es ${}'.format(nro_cuenta,saldo)