NUMERO_ALUMNOS = 5
cals =[None]*NUMERO_ALUMNOS
alumnos = [None]*NUMERO_ALUMNOS

#Entrada dendatos
for i in range(0, NUMERO_ALUMNOS, 1):
    msg = "Proporciona el nombre del alumno " + str(i + 1) + ":"
    alumnos[i] = input(msg)
    esValido = False
    while not esValido:
        msg = "Proporcione la calificacion de " + alumnos[i] + ":"
        cals[i] = float(input(msg))
        if cals[i] >= 0 and cals[i] <= 10:
            esValido = True
        else:
            print("La calificacion debe estar entre 0 y 10. Intente de nuevo")
#Proceso
suma = 0.0
mayor = cals[0]
idxMayor = 0

for j in range(0, NUMERO_ALUMNOS, 1):
    suma += cals[j]
    if cals[j] > mayor:
        mayor = cals[j]
        idxMayor = j
promedio = suma / NUMERO_ALUMNOS
#Resultados
print("El promedio es ", promedio)
print("La mejor calificacion la tiene ", alumnos[idxMayor], "con", cals[idxMayor])
print("Los alumnos con calificacion arriba del promedio son:")
for k in range(0, NUMERO_ALUMNOS, 1):
    if(cals[k] > promedio):
        print(alumnos[k], " con ", cals[k])
