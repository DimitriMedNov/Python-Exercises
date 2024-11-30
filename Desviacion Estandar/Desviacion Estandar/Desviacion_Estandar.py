def getProm(n):
    sumaP=0
    for i in range(0,n,1):
        sumaP += vDatos[i]
    promedio=sumaP/n
    return promedio
N=int(input("Cuantos numeros: "))
vDatos=[None]*N
for i in range (0,N,1):
    vDatos[i]=float(input("Proporcione el valor " +  str(i+1)+": "))
media=getProm(N)
sumaDC = 0
for i in range(0,N,1):
    sumaDC += (vDatos[i]-media)**2
varianza = sumaDC / (N-1)
ds=varianza ** (1.0/2.0)
print("Promedio: ", media)
print("Varianza: ", varianza)
print("DS: ", ds)

