import random

minusculas = "abcdefghijklmnñopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!#$%&/()=?'¿¡+*-+_.,;@"

uso_para = minusculas + mayusculas + numeros + simbolos

ancho_contrasena = 15

contrasena = "".join(random.sample(uso_para, ancho_contrasena))

print("Contraseña generada: ( " + contrasena + " )")
