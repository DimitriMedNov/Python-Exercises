# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:05:02 2021

@author: MedNo
"""

name = "Agustín"
"Hola %s" % name
"El numero es %d" % 5
"El numero es %2d" % 5 #Son dos digitos pero como solo se puso 5 imprime 05
"El decimal es %f" %6.5
"El decimal es %.2f" % 6.5
"Hola %(name)s" % {'name' : name}

"Hola {}".format(name) #Remplaza los {} por lo que esta en los ()
"La suma de 1 + 2 es {0}".format(1+2)

' '.join(["Hola",name])
' '.join(["1","2","3","4"])

#Examen Semana 1
a_string = 'Hola Mundo Python!'
"Hola||| %s" % a_string[-7]

s6 = [1,2,3]
'-'.join([str(y) for y in s6])
"{}-{}-{}".format(1,2,3)

