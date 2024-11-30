#opcion 1
print("Solo lee numeros si pones una letra el programa se jode")
ent = int(input("Proporcione un numero: ")) #str
valor = ent * ent
print(valor)
print()

#opcion 2
print("Aqui el porgrama ya no se jode si pones letras")
valido = False
while not valido:
    entrada = input("Proporcione un numero: ") #str
    valido = entrada.isnumeric()
    if not valido:
        print("Entrada no valida. Intente de nuevo. ")
valor = float(entrada)
valor = valor * valor
print(valor)