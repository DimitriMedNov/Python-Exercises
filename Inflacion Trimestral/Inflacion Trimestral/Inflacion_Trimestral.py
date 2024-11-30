Trimestres = 4
Estados = 3
Estado = ["Campeche", "Quintana Roo", "Yucatan"]
inflacion = [[None]*(Trimestres + 4) for i in range(Estados + 3)]
titulos = ["Estado", "T1", "T2", "T3", "T4", "Promedio", "Menor", "Mayor"]

def promedioMes(idxFila):
    suma = 0.0
    for columna in range(1, (Trimestres + 1), 1):
        suma += inflacion[idxFila][columna]
    return suma / Trimestres

def promedioTri(idxColum):
    suma = 0.0
    for fila in range(0, Estados, 1):
        suma += inflacion[fila][idxColum]
    return suma / Meses

#Entrada de datos
for fila in range(0, Estados, 1):
    print("Proporcione la inlfacion de " +  Estado[fila] )
    for columna in range(0,Trimestres, 1):
        inflacion[columna]= float(input("Proporcione la inflacion del trimestre " + str(columna + 1) + ": "))