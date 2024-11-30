from random import random, randint, uniform
veces = int(input("Cuantos aleatorios: "))
con = 1
for con in range(veces):
 print ("Random: ", random()) #Aleatorio real entre 0 y 1
 print ("Ranint: ", randint(20, 200)) #Aleatorio entero entre 0 y 10
 print ("Uniform: ",uniform(1, 10)) #Aleatorio real entre 1 y 10
 print ("Random * n: ", random() * 10) #Aleatorio real entre 1 y 10
