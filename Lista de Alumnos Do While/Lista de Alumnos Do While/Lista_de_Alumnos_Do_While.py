
nombres = [None]*5
cals = [None]*5
for idx in range(0, 5, 1):
 mensaje = "Proporciona el nombre " + str(idx + 1) + ": "
 nombres[idx] = input(mensaje)
 mensaje = "Proporcione la calificacion de: " + nombres[idx]
 cals[idx] = float(input(mensaje))
for i in range(4, -1, -1):
 print(nombres[i], " tiene ", cals[i])
while True:
 idxUser = int(input("Numero de la lista (1 - 5): "))
 print("El nombre del elemento ", idxUser, " es ", nombres[idxUser - 1])