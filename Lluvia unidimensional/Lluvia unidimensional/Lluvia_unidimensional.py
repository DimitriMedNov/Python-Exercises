numMeses = 8
Meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto"]
cantLluvia = [None]*numMeses

for i in range (0, numMeses, 1):
    msg = "Proporcione la cantidad mensual en mm de " + Meses[i]+ ": "
    cantLluvia[i] = float(input(msg))
    pormedio = 0
    suma = 0
    suma = suma + cantLluvia[i]
    promedio = suma / numMeses

print("")
print (f"El promedio mensual de los {numMeses} Meses es {promedio} ")
print("")
print (f"Los Meses que estuvieron por debajo del promedio ({promedio}) son: ")

for i in range (0, numMeses, 1):
    if(cantLluvia[i] < promedio):
        print(Meses[i]," con: ",cantLluvia[i], " mm")

print("")
print("Los Meses que estuvieron entre 50 y 200 mm fueron: ")

for i in range (0, numMeses, 1):
    if ((cantLluvia[i] >= 50) & (cantLluvia[i] <= 200)):
        print(Meses[i]," con: ",cantLluvia[i], " mm")
print("")