#FUNCION 1
def getPromedio():
    suma = 0
    for i in range (0, corredor, 1):
        suma += minutos[i]
    return suma / corredor

#FUNCION 2
def porDebajo():
    debajo = 0
    print ("Los corredores que estuvieron por debajo de 25min fueron: ")
    for i in range (0, corredor, 1):
        if (minutos[i] < 25):
            print(runners[i])
    return debajo

corredor = 7
runners = ["Corredor 1", "Corredor 2", "Corredor 3", "Corredor 4", "Corredor 5", "Corredor 6", "Corredor 7" ]
minutos = [None]*corredor

for i in range (0, corredor, 1):
    msg = "Proporcione los minutos en los que termino la carrea el " + runners[i]+ ": "
    minutos[i] = float(input(msg))

#FUNCION 1
promedio = getPromedio()
print ("El promedio de minutos en la carrera de los 7 corredores es ", promedio)

#FUNCION 2
deba = porDebajo()
print ("Carrera MAYAB ruge como Leon RRAAAAAAAR xd 0 _ ",deba)

for i in range (0, corredor, 1):
    mayor = minutos[1]
    idxmax = 1
    if (minutos[i] > mayor):
        mayor = minutos[i]
        idxmax = i
print("El tiempo mas largo registrado fue de: ", mayor ," minutos con el corredor numero: ", idxmax + 1)
minus = mayor / 5
print("Con um promedio de ", minus ," minutos por kilometro")