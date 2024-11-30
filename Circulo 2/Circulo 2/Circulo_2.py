
PI = 3.1416

def getAreac( _radio):
    area = PI * _radio * _radio
    return area


r = input("Proporcione el radio del circulo: ")
area2 = getAreac(float (r))
print ("El area del circulo es: ", area2)

def getPerimetro( _radio):
    perimetro = (PI * 2) * _radio
    return perimetro


perimetro2 = getPerimetro(float (r))
print ("El perimetro del circulo es: ", perimetro2 )