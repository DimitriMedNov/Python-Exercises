l1 = input("Proporcione el lado 1: ")
l2 = input("Proporcione el lado 2: ")
l3 = input("Proporcione el lado 3: ")

if (l1 == l2 and l2 == l3):
    print("Es equilatero")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("Es isosceles")
else:
    print("Es escaleno")
