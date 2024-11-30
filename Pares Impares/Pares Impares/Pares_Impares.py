num = float(input("Ponga el numero que guste: "))

opcion = "W"

while (opcion != "s" and opcion != "S"):
    print("Seleccione una opción.")
    print("A. Sacar los numeros Impares que tiene su numero.")
    print("B. Sacar los numeros Pares que tiene su numero.")
    print("C. Proporcionar un nuevo número.")
    print("S. Salir.")
    opcion = input("Su opción: ")

    if(opcion == "A" or opcion == "a"):
        idf = 1
        while idf <= num:
            print(idf)
            idf += 2

    elif opcion == "b" or opcion == "B":
       idh = 2
       while idh <= num:
            print(idh)
            idh += 2

    elif opcion == "c" or opcion == "C":
        num = float(input("Ponga el numero que guste: "))

    elif opcion == "s" or opcion == "S":
        print("Hasta la vista bby.")

    else:
        print("Me temo que no puedo hacer nada por usted.")

