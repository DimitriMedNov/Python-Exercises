
Num_Periodos = 6
Salir = str("")

while (Salir != "s" or Salir != "S"):
    Salir = ("")
    InvIni = float(input("Proporcione su inversion inicial plz: "))
    Ti = float(input("Proporcione su tasa de interes plz: "))
    GananPeriods = [None]*Num_Periodos
    for i in range (0,Num_Periodos, 1):
        msg = "Proporcione las ganancias del periodo " + str(i+1)+ ": "
        GananPeriods[i] = float(input(msg))


    VPN = (-1*InvIni)
    for k in range (0,Num_Periodos, 1):
        dividir = 1 + (Ti/100)
        VPN = VPN + (GananPeriods[k]/(pow(dividir,k + 1)))

    print(f"Usted tiene ganancias de: {VPN}")
    if (VPN < 0):
        print("Me temo brother que su proyecto no es redituable :(")
    else:
        print("Felicidades compadre su proyecto si es redituable :)")
    Salir = input("Desea salir del programa? S/N: ")

