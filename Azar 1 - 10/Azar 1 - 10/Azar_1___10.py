from random import random, randint

continuar = 's';
while continuar == 'S' or continuar == 's':
    intentos = 0
    gano = False
    aleatorio = randint(1, 10)
    while intentos < 3 and not gano:
     numero = int(input("Proporcione un numero: "))
     if numero == aleatorio:
         gano = True
     else:
         print("Lo siento ese no es el numero.")
         intentos += 1        
       
         if gano:
             print("Felicidades has ganado del juego.")
         else:
             print("Lo siento has perdido, el numero era", aleatorio)
             continuar = input("Desea jugar de nuevo? S/N")
