PI=3.1416
def area_circulo(radio):
    area=PI*(radio**2)
    return round(area,2)

def perimetro_circulo(radio):
    perimetro=PI*radio*2
    return round(perimetro,2)

radio=float(input("Proporcione el radio del circulo: "))
area=area_circulo(radio)
perimetro=perimetro_circulo(radio)

print("El area del circulo es: ", area)
print("El perimetro del circulo es: ", perimetro)
