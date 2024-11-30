def getTipoTrian(la1, la2, la3):
    if (la1 == la2 and la2 == la3):
        res = "Es equilatero"
    elif la1 == la2 or la2 == la3 or la3 == la1:
        res = "Es isosceles"
    else:
       res = "Es escaleno"
    return res

l1 = float(input("Proporcione el lado 1: "))
l2 = float(input("Proporcione el lado 2: "))
l3 = float(input("Proporcione el lado 1: "))

print("Seleccione una opcion")
print("A Determinar si el triangulo es rectangulo")
print("B Determinar el tipo de triangulo")
print("S Salir")
opcion = input("Su opcion fue: ")

if(opcion == "A" or opcion == "a"):
    print("En construccion")
elif opcion == "b" or opcion == "B":
    print(getTipoTrian(l1, l2, l3))
elif opcion == "s" or opcion == "S":
    print("Bye")
else:
    print("Opcion invalida")