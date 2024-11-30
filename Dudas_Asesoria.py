#ARRAY UNIDIMENSIONALES  1 FILA N COLUMNAS
data = [None] * 3
data0 = []
data1 = ["Ford","Volvo","BMW"]
data2 = ["Ford"] * 3  #STRING
data3 = ["Ford", None, 3, 3.0, False]

print(data0)
print(data)
print(data1)
print(data2)
print(data3)

list1 = [i for i in range(10)]

#ARRAY BIDIMENSIONALES N FILAS M COLUMNAS

data4 = [ [None] * 3 ] * 3
data5 = [ [5.1,7.4,3.2,9.9],
          [1.9,6.8,4.1,2.3],
          [2.9,6.4,4.3,1.4]]
print(data5)
#Fila no es un indice de posición, es un elemento de tu matriz
for fila in data5: #NO SE CONOCEN LOS INDEX DE POSición
    #print(fila) #NO ACCESO A LA POS DEL ELEMENTO
    for columna in fila:
        print(columna)
#range(3) -> 0,1,2
print("Longitud: ",len(data5))
for i in range(len(data5)): #SI SE CONOCEN LOS INDEX DE POS
    #print(i,": ",data4[i])
    for j in range(len(data5[i])):
        print(i,",",j,": ",data5[i][j])

#Segunda parte

print("Filas de una matriz", end=": ")
n = int(input())
print("Columnas de una matriz", end=": ")
m = int(input())

list = [ [None] * m ] * n
for fila in list:
    print(fila,type(fila), id(fila))
  
print("----------------------------")  
list2 = [ [None] * m for i in range(n)]
for fila in list2:
    print(fila,type(fila), id(fila))


print(list)
for i in range(len(list)): #RETORNA FILAS
    for j in range(len(list[i])): #RETORNAR COLUMNAS
        print("Valor [",i,"][",j,"]",end = ": ")
        list[i][j] = input()
print(list)


print(list2)
for i in range(len(list2)): #RETORNA FILAS
    for j in range(len(list2[i])): #RETORNAR COLUMNAS
        print("Valor [",i,"][",j,"]",end = ": ")
        list2[i][j] = input()
print(list2)

#Tercera parte

print("Filas de una matriz", end=": ")
n = int(input())
print("Columnas de una matriz", end=": ")
m = int(input())

list2 = [ [None] * m for i in range(n)]

print(list2)
for i in range(len(list2)): #RETORNA FILAS
    for j in range(len(list2[i])): #RETORNAR COLUMNAS
        print("Valor [",i,"][",j,"]",end = ": ")
        list2[i][j] = input()
print(list2)
list2.append([7,8,9,10,12,13]) #AGREGUE UNA FILA
print(list2)

count = 0;
for fila in list2:
    if count == 0:
        pass
    else:
        fila.append("new")
    count += 1
print(list2)

for fila in list2:
    print(fila)

list2.pop(len(list2)-1)

for i in range(len(list2)):
    for j in range(len(list2[i])):
        if(j == len(list2[i])-1):
            list2[i].pop(j)

        
for fila in list2:
    print(fila)

"""
x = []
x.append([1])
x.append([1,2])
x.append([1,2,3])
x.append([1,2,3,4])
print(x)
"""
#Extra
data = [None] * 3 
data0 = []
data1 = ["Ford","Volvo","BMW"]
data2 = ["Ford"] * 3  #STRING
data3 = ["Ford", None, 3, 3.0, False]
print(data0)
print(data)
print(data1)
print(data2)
print(data3)
"""

"""
data = [None] * 3 
print(data)
#for i in range(10) -> 0,1,2,3,4,5,6,7,8,9
list1 = [i for i in range(10)]
list2 = [i*i/2 for i in range(10)]
print(list1)
print(list2)

print(list2[5])

for element in list2:
    print(element)
"""

"""
list2 = [i*i/2 for i in range(10)]
print("Tamaño elementos: ",len(list2))
for i in range(len(list2)):
    print(i,": ",list2[i])
    
for i in range(5):
    list2.append(2.6+i)

print("Tamaño elementos: ",len(list2))
for i in range(len(list2)):
    print(i,": ",list2[i])
   
list2.pop(1) #ELIMINA POR INDICE
list2.remove(8.0) #ELIMINAR POR VALOR O ELEMENTO

print("Tamaño elementos: ",len(list2))
for i in range(len(list2)):
    print(i,": ",list2[i])
"""

"""
print("Ingrese los elementos de la lista", end = ': ')
n = int(input())
a = [None] * n
print(a)
for i in range(len(a)): #i = indice range(len(a)) = size
    print("Valor [",i,"]",end = ": ")
    a[i] = input()
print(a)
b = a.copy()
a.clear()
print(a)
print(b)
"""
#INT, FLOAT, DOUBLE, BOOLEAN, STRING, SHORT, LONG

#ARRAY BIDIMENSIONALES N FILAS M COLUMNAS
"""
data4 = [ [5.1,7.4,3.2,9.9],
          [1.9,6.8,4.1,2.3],
          [2.9,6.4,4.3,1.4]]
          
data5 = [ [None] * 3 ] * 3
data6 = [ [None] * 3 for i in range(3)]
data7 = [ [None for j in range(3)] for i in range(3) ]

print(data5)
print("----------------------")
print(data6)
print("----------------------")
print(data7)
"""

print("Filas de una matriz", end=": ")
n = int(input())
print("Columnas de una matriz", end=": ")
m = int(input())

list = [ [None] * m ] * n
print(list)
for i in range(len(list)): #RETORNA FILAS
    for j in range(len(list[i])): #RETORNAR COLUMNAS
        print("Valor [",i,"][",j,"]",end = ": ")
        list[i][j] = input()
print(list)


          
"""
print(data5)
#FILA no es un indice de posición, es un elemento de tu array
for fila in data5: #NO SE CONOCEN LOS INDEX DE POSICIÓN
    #print(fila) #NO ACCESO A LA POS DEL ELEMENTO
    for columna in fila:
        print(columna)
#range(3) -> 0,1,2
print("Longitud: ",len(data5))
for i in range(len(data5)): #SI SE CONOCEN LOS INDEX DE POS
    #print(i,": ",data4[i])
    for j in range(len(data5[i])):
        print(i,",",j,": ",data5[i][j])