vector = [None]*5
def getSaludo(nom):
    return "Hola " + nom
def getPromedio():
    suma = 0
    for i in range (0, 5, 1):
        suma += vector[i]
    return suma / 5
def impImpares(num):
    for i in range (1, int(num) + 1, 2):
        print (i)

nombre = input ("Cual es su nombre? ")
for i in range (0, 5, 1):
    vector[i] = float(input("Proporcione el numero " + str(1+i) + ": "))
promedio = getPromedio()
print(getSaludo(nombre))
print("El promedio es ", promedio)
print("Los numeros impares del ultimo valor son: ")
impImpares(vector[4])