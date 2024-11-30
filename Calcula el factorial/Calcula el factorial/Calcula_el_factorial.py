
#obtener factorial
def getFactorial(num):
    factorial = 1
    if num > 0:
        for i in range (num, 0, -1):
            factorial *= i #factorial = factorial * 1
    return factorial

#obtener potencia
def getPotencia(base, exp):
    potencia = 1
    if exp > 0:
        for i in range (0, exp, 1):
            potencia *= base #potencia = potencia * base
    return potencia

#menu para repetir
opcion = "g"
while opcion != "s" and opcion != "S":
    print ("A. Calcular el factorial ")
    print ("B. Calcular la potencia ")
    opcion = input("S. Salir ")
    if opcion == "A" or opcion == "a":
        numero = int(input("Proporcione su numero: "))
        fact = getFactorial(numero)
        print ("El factorial de ", numero, "es ", fact)
    elif opcion == "b" or opcion == "B":
        base = float(input("Proporcione su numero: "))
        exponente = int(input("Proporcione el exponente: "))
        potencia = getPotencia(base, exponente)
        print (base, " elevado a ", exponente, "potencia es igual a ", potencia )
