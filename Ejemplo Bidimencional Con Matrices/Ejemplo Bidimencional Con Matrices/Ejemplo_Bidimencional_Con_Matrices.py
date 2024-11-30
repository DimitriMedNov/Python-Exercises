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

#vNombre = [None]*5
#vRFC = [None]*5
CANTIDAD_PARES = 2 # ----> Aqui es el numero de personas que necesitas
mDatos = [[None]*2 for i in range(CANTIDAD_PARES)]
mDatos2 = [[1,2,3], [0,9,8]]

mDatos2[0][0] = "HOLA"
#mDatos[0][0] = "HOLA"
#mDatos2[3][0] = "MARY"
#mDatos2[2][1] = "52.89"
#mDatos2[0][1] = "JUAN"

for fila in range(0, CANTIDAD_PARES, 1):
    for col in range(0, 2, 1):
        if col == 0:
            mDatos[fila][col] = input("Proporcione el nombre de la persona: ")
        else:
            valido = False
            while not valido:
                mDatos[fila][col] = input("Proporcione el RFC de " + mDatos[fila][0] + ": ")
                valido = esRFC(mDatos[fila][col])
                if not valido:
                    print("Entrada no valida. Intente de nuevo.")

print("Nombre", "RFC")
for fila in range(0, CANTIDAD_PARES, 1):
    texto = ""
    for col in range(0, 2, 1):
        texto += mDatos[fila][col] + "\t"
    print(texto)

for fila in range(0, 2, 1):
    for col in range(0, 3, 1):
        print (mDatos2[fila][col])
