horasxdia = [None]*7
total_horas = 0
Dias = 7

dias = ["Lunes","Martes", "Miercoles","Jueves", "Viernes", "Sabado", "Domingo"]
sueldo = float(input("Sueldo por hora:  "))

for i in range (0,Dias,1):
    horasxdia[i] = int(input("Ingrese la cantidad de horas trabajadas en: " + dias[i] ))
    total_horas += horasxdia[i]

sueldosemanal = sueldo*total_horas

if sueldosemanal <= 1000:
    descuento = sueldosemanal * .05
elif sueldosemanal <= 2000:
    descuento = sueldosemanal *.07
elif sueldosemanal <= 3000:
    descuento = sueldosemanal * .09

print ("Su sueldo: ", sueldo)
print("Horas trabajadas: ", total_horas)
print("Se le deberia pagar: ", sueldosemanal)
print ("Perousted aplica a descuento: ", descuento)
print("Y el Monto Total a pagar con descuento ya aplicado: ", sueldosemanal - descuento)

