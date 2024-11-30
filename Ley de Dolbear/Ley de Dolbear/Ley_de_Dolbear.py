def getClasficacion(pTC):
    clasf = "";
    if pTC < 20:
        clasf = "No clasificada"
    elif pTC <= 25:
        clasf = "Ideal"
    elif pTC <= 32:
        clasf = "Peligrosa"
    else:
        clasf = "Contraindicada"
    return clasf

def getDolbear (N60):
    tc = ((N60 - 40) / 7) + 10
    return tc

DIAS_SEMANA = 7
vDias = ["Lunes ", "Martes ", "Míercoles", "Jueves ", "Viernes ", "Sábado ", "Domingo "]
vN60 = [None]*DIAS_SEMANA
vTC = [None]*DIAS_SEMANA
vClas = [None]*DIAS_SEMANA
salir = "n"

#ENTRADA DE DATOS / CALCULOS
while(salir !="s" and salir != "S"):
    suma = 0
    for i in range(0, DIAS_SEMANA, 1):
        vN60[i] = int(input("Proporcione el número de sonidos por minuto para el " + vDias[i] + ": "))
        vTC[i] = getDolbear(vN60[i])
        vTC[i] = round(vTC[i], 2)
        suma = suma + vTC[i]
        vClas[i] = getClasficacion(vTC[i])
    promedio = suma / DIAS_SEMANA
#imprimir tabla
print("Dia \tN60\tTC\tClasificacion")
for i in range(0, DIAS_SEMANA, 1):
     print(vDias[i], "\t", vN60[i], "\t", vTC[i], "\t", vClas[i])
print("El promedio es: ", round(promedio, 2))

for i in range (0, DIAS_SEMANA, 1):
     if vClas[i] == "Peligrosa" or vClas[i] == "Contraindicada":
         print(vDias[i], " - ", vClas[i])
salir = input("¿Desea terminar el programa? s/n ")