def esRFC(pRFC):
    valido = True
    for i in  range(0, len(pRFC), 1):
        if i <= 3:
            if not str(pRFC[i]).isalpha():
                valido = False
                break
        elif i <= 9:
            if not str(pRFC[i]).isdigit():
                valido = False
                break
        else:
            if not str(pRFC[i]).isalnum():
                valido = False
                break
    return valido

vNombre = [None]*5
vRFC = [None]*5
for i in range(0, 5, 1):
    vNombre[i] = input ("Proporcione el nombre ")
    esValido = False
    while(not esValido):
        vRFC[i] = input("Proporcine el RFC de " + vNombre[i] + ": ")
        esValido = esRFC(vRFC[i])
        if not esValido:
            print("Entrada no valida. Intente de nuevo. ")

print("Nombre\t\tRFC")
for i in range(0, 5, 1):
    print(vNombre[i], "\t",vRFC[i])
print()
print("Nombre\t\tRFC")
for i in range(o, 5, 1):
    print(str(vNombre[i]).upper(), "\t", str(vRFC[i]).upper())
