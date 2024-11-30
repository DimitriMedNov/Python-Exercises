
diaE = 745
diaL = 1140
segur = 0.07
print("Seleccione una opcion")
print("Precio x dia de auto Economico es de $745")
print("Precio x dia de auto de Lujo es de $1140")
print("E Auto Economico")
print("L Auto de Lujo")

opcion = input("Su opcion fue: ")

if(opcion == "E" or opcion == "e"):
    dias = int(input("Proporcione cuantos dias rento el auto economico: "))
    renta = dias*diaE
    print("Tipo auto: Económico")
    print("Días de renta: ",dias," dias")
    print("Seguro de daños: 0.0")
    print("Total a pagar es: ",renta)
elif opcion == "L" or opcion == "l":
    dias2 = int(input("Proporcione cuantos dias rento el auto de lujo: "))
    renta2 = dias2*diaL
    print("Tipo auto: Lujo")
    print("Días de renta: ",dias2," dias")
    seguro = (renta2 * segur)
    print("Seguro de daños: ",seguro)
    total = renta2 + seguro
    print("Total a pagar es: ",total)

#El while no me salia

#def getCargo():
    #seguro = 0
    #seguro = renta2*0.07
    #print(seguro)
    #return seguro