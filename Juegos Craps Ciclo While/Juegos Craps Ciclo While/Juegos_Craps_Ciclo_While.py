from random import randint

continuar = "s"
while continuar == "s" or continuar == "S":
    intentos = 0
    puntos = 0
    Win = False
    Fail = False
    while intentos < 7 and not Win and not Fail:
        dummy = input("Presione enter para continuar")
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        suma = dado1 + dado2
        intentos += 1
        print("Has sumado ", suma, " dado1: ", dado1, ", dado2: ", dado2)
        if intentos == 1 and (suma == 7 or suma == 11):
            Win = true
        elif (intentos > 1 and suma == 7) or suma == 2 or suma == 3 or suma == 12: #elif = else y if
            Fail = true
        else:
            puntos += 1
            print("Tus puntos son: " , puntos)
    #fin de while
    if Fail:
        print("Haz perdido maquina :(")
    else:
        print("Enhorabuena haz ganado maquina :)")
    continuar = input("Desea seguir tirando daditos? S\N: ")

