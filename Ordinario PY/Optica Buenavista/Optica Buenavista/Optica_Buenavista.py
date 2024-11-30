
compra = 3500
porcentaje = 100
IVA = .16

print ("Optica Buenavista")
edad = int(input("Proporcione su edad para aplicar el descuento a la compra: "))

descuento = 0
descuento = edad / porcentaje

descuento2 = 0
descuento2 = compra * descuento

importe = 0
importe = compra - (compra * descuento)

IVA2 = 0
IVA2 = importe * IVA

total = 0
total = importe + IVA2

print ("Su edad: ", edad)
print ("Monto de compra: ", compra)
print ("Descuento: ", descuento2 )
print ("Su importe con descuento aplicado es: ", importe)
print ("El IVA aplicado es: ", IVA2)
print ("Total a pagar: ", total)