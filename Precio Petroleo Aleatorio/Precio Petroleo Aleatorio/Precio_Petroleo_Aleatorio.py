from random import uniform

NumDias = 30
petroleo = [None]*NumDias

#Lllenado de datos
for i in range (0, NumDias, 1):
    petroleo[i] = uniform(130, 150)

#proceso
suma = 0
mayor = petroleo[11]
idxmax = 11
menor = petroleo[0]
idxmen = 0

for i in range(0, NumDias, 1):
    suma = suma + petroleo[i]
    if petroleo[i] > mayor:
        mayor = petroleo[i]
        idxmax = i
    if petroleo[i] < menor:
        menor = petroleo[i]
        idxmen = i

promedio = suma / NumDias

#Salida de datos
print(f"El promedio es de {promedio}")
print("El precio mas alto fue:", mayor, " en el dia ", idxmax + 1 )
print("El precio mas bajo fue:", menor, " en el dia ", idxmen + 1 )
print("Los dias con precio superior al promedio son: ")
for i in range(0, NumDias, 1):
    if petroleo[i] > promedio:
        print (i + 1, " con ", petroleo[i])