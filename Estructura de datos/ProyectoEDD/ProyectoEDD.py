# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:56:43 2021

@author: Jesus Dimitri Medina Novelo
"""

while(True):
    print ("-------------- Menu ---------------")
    print ("Jesus D. Medina Novelo || 00396910")
    print ("-----------------------------------")
    
    #Arreglos
    print ("1.Arreglo\n") #Listo
    
    print ("2.Pilas\n") #Listo
    
    print ("3.Colas\n") #Listo
    
    #Listas
    print ("4.Lista Simple\n") #Listo
    
    print ("5.Lista Circular\n") #Listo
    
    #Ordenamientos
    print ("6.Quicksort\n") #Listo
    
    print ("7.Shell\n") #Listo
    
    #Arbol
    print ("8.Arbol\n") # Listo
    
    #Grafo
    print ("9.Grafo\n") # Listo 
    
    
    print ("0.Salir\n")
     
    print ("Introduce un numero entre 1 y 9\n")
       
    num = input("Seleccione una opción: ")
    
    print("\n")

    
    #ArregloS -------------------------------------------> 1
    if num == "1":
        class Arreglos():
            # imprime la lista de *****
            
            print ("Usted ha elegido la opcion: " + num+"\n")
            print ('------Arreglo------'. center(30))
            Array = input("Ha elegido crear una lista de? ")
                    
            num = input("De cuantas cosas conforma su lista? ")
            
            pasos = [None]*int(num)
            print()
            print ("Lista de " + Array+"\n")
            
            for i in range(0, int(num), 1):
                mensaje = "Ingrese las cosas que requerira su lista: " + str(i + 1) + ": "
                Pasos2 = input(mensaje)
                while ((all(Pasos2.isalpha() or Pasos2.isspace() for Pasos2 in Pasos2)) == False):
                    Pasos2 = input("Ingregue una opcion válida (No ints): ")
                pasos[i] = Pasos2
            print("\nLista de " + Array.title())
            print("Su conformacion: ")
            for i in range (0, int(num), 1):
                print("- ", pasos[i].title())
            print("\nMenu")
            print("1. Crear otra lista")
            opcion = input("2. Deseo salir\n")
            while (opcion != "1") and (opcion != "2"):
                opcion = input("Ingrese una opción válida: ")
                            
    
    #Pilas -------------------------------------------> 2
    elif num == "2":
        print ("Usted ha elegido la opcion: " + num+"\n")
        print ('------Pilas------'. center(30))
        pila = []
        cima = -1
        
        while True:
            print("\nMenu")
            print("Selecciona una opcion")
            print("1.Meter datos")
            print("2.Sacar datos")
            print("3.Pila vacia?")
            print("4.Mostrar Pila")
            print("5.Salir")
        
            opcion = input("Ingrese la opcion: ")
            
            if opcion == '1':
                print("Cuantos numeros le gustaria introducir: ")
                cantidad=int(input())
                
                print (f"Ponga {cantidad} numeros: ")
        
                if cima<cantidad:
                    for i in range(cantidad):
                        pila.append(input("Ingrese: ")) 
                        cima+=cantidad
                    
            elif opcion == '2':
                if cima >-cantidad:
                    print ("Se ha quitado el numrero --> "+pila.pop())
                    cima -=cantidad
                    
            elif opcion == '3':
                if cima == -1:
                    print("La pila esta vacia!")
                    
                else:
                    print("La pila no esta vacia :/")
                    
            elif opcion == '4':
                print ("La pila se conforma por estos numeros --> "+str(pila))
        
            elif opcion == '5':
                break
            
        print("Usted ha salido del programa\n")
    

    
    #Colas -------------------------------------------> 3 #Cambiar
    elif num == "3":
        lista = []
        class Colas():
            # lista de personas a las que tienes que contestar sus emails en orden de cuál te llegó primero

            def printLista():
                
                 if (len(lista) > 0): print("\nPacientes en sala de espera: ", lista,"\n")
                 if (len(lista) == 0): print("\nSin pacientes para atender\n")
            
            opcion = "1"
            
            while True:
                print("Usted ha elegido la opcion: 3\n")
                print ('------Colas------'. center(30))
                print("Digite una opcion ")
                print("\n--- Dr. Simi ---")
                print("1. Agregar personas para atender")
                print("2. Marcar persona atendida")
                print("3. Salir")
                
                opcion = input("Digite la opcion: ")               
                
                if (opcion == "1"):
                    num = input("¿Cuántas personas desea agregar? ")
                    
                    for i in range(0, int(num), 1):
                        nombre = input("Nombre: ")
                        lista.append(nombre.title())
                    printLista()
                
                if (opcion == "2"):
                    if (len(lista) == 0): print("La listá de pacientes esta vacia, no tiene a nadie por atender")
                    else:
                        num = input("¿A cuántas personas ya atendio? ")
                        for i in range(0, int(num), 1):
                            lista.pop(0)
                        printLista()
                        
                if (opcion == "3"):
                    break
            print("\nUsted ha salido del programa\n")
    
    #Lista simple -------------------------------------------> 4
    elif num == "4":
        print ("Usted ha elegido la opcion: " + num+"\n")
        print ('------Lista simple------'. center(30))
        
        class Node:
            def __init__(self, Value):
                self.Value = Value
                self.Next = None
                
            def __str__(self):
                return str(self.Value)
            
        class Linkedlist:
            def __init__(self):
                self.First = None
                self.Size = 0
                
            
            def Append(self, Value):
                MyNode = Node(Value)
                if self.Size == 0:
                    self.First = MyNode
                else:
                    Current = self.First
                    while Current.Next != None:
                        Current = Current.Next
                    Current.Next = MyNode
                    
                self.Size += 1
                
                return MyNode
            
            def Remove(self, Value):
                if self.Size == 0:
                    return False
                
                else:
                    Current = self.First
                    while Current.Next.Value != Value:
                        if Current.Next == None:
                            return False
                        else:
                            Current = Current.Next
                    DeleteNode = Current.Next
                    Current.Next = DeleteNode.Next
                    
                self.Size -= 1
                
                return DeleteNode
            
            def __len__(self):
                return self.Size
            
            def __str__(self):
                String ="["
                Current = self.First
                while Current != None:
                    String += str(Current)
                    String += str(",")
                    Current = Current.Next
                String += "]"
                
                return String
        
        List = Linkedlist()
        
        while True:
                    print("Menu")
                    print("Selecciona una opcion")
                    print("1.Meter datos a las lista")
                    print("2.Sacar datos de la lista")
                    print("3.Mostrar Lista")
                    print("4.Salir")
                
                    opcion = input("Ingrese la opcion: ")
                    
                    if opcion == '1':
                        print("Digite el numero para la lista: ")
                        List.Append(input("Ingrese el numero a poner en la lista: "))
                        
                    if opcion == '2':
                        num = input("Digite el numero que desea eliminar: ")
                        print ("Se ha quitado el numrero --> "+ str(List.Remove(num)))
        
                    if opcion == '3':
                        print ("La Lista se conforma por --> "+str(List))
                        
                    if opcion == '4':
                        break
                    
        print("Usted ha salido del programa\n")
   
    #Lista circular -------------------------------------------> 5 #Cambiar
    
    elif num == "5":
        while True:
                    import ListaCircle as Runner
                    break                                               
                
    #Quicksort -------------------------------------------> 6
    elif num == "6":
        print ("Usted ha elegido la opcion: " + num+"\n")
        print ('------Quicksort------'. center(30))
        while True:
            def Quick_sort(lista):
                Quick_sort_Aux(lista, 0, len(lista)-1)
                
            def Quick_sort_Aux(lista, principio, final):
                if principio < final:
                    punto_particion = partir(lista, principio, final)
                    
                    Quick_sort_Aux(lista, principio, punto_particion -1)
                    Quick_sort_Aux(lista, punto_particion +1, final)
                    
            def partir(lista, principio, final):
                pivote = lista[principio]
                
                izq = principio +1 
                der = final 
                terminado = False
                
                while not terminado:
                    while izq<=der and lista[izq] <= pivote:
                        izq += 1
                        
                    while lista[der] >= pivote and der >= izq:
                        der -=1
                        
                    if der < izq:
                        terminado = True 
                    else:
                        temporal = lista[izq]
                        lista[izq] = lista[der]
                        lista[der] = temporal 
                        
                temporal = lista[principio]
                lista[principio] = lista[der]
                lista[der] = temporal 
                
                return der
            
            print("Cuantos numeros le gustaria ordenar: ")
            cantidad=int(input())
            
            Cantidad=[None]*cantidad
            X=cantidad-1
            
            print (f"Ponga {cantidad} numeros: ")
                    
            mi_lista = []  
            
            for i in range(cantidad):
                ingresado = input("Ingrese: ") 
                mi_lista.append(ingresado)
                
            print ("\nOriginal: ")
            print(mi_lista)  
                        
            Quick_sort(mi_lista)
            print("\nOrdenado: ")
            print(mi_lista)
            break 
                
    #Shell -------------------------------------------> 7   
    elif num == "7":
        print ("Usted ha elegido la opcion: " + num+"\n")
        print ('------Shell------'. center(30))
        
        while True:
            def shell(lista):
                mitad = len(lista) // 2
                
                while mitad > 0:
                    for p in  range(mitad):
                        reducir_busqueda(lista, p, mitad)
                        
                        
                    mitad = mitad // 2
                    
            def reducir_busqueda(lista, inicio, salto):
                for i in range(inicio + salto, len(lista), salto):
                    valor = lista[i]
                    posicion  = i
                    
                    
                    while posicion >= salto and lista[posicion - salto] > valor:
                        lista[posicion] = lista[posicion - salto]
                        posicion = posicion - salto
                                    
                        
                    lista[posicion] = valor
                    
            numeros = []  

            cantidad = int(input("Cuantos numeros le gustaria ordenar: "))
            
            parseo = str(cantidad)
            
            print (f"Ingrese {cantidad} numeros ")
            
            for i in range(cantidad):
                 numeros.append(input("Ingrese el numero "+ str(i + 1) +": "))
            
                
            print ("\nOriginal: ")
            print(numeros)  
                        
            shell(numeros)
            print("\nOrdenado: ")
            print(numeros)
            break   
    
    
    #Arboles -------------------------------------------> 6
    elif num == "8":
        import Arboles as nodoArbol
               
                
    #Grafos -------------------------------------------> 7   
    elif num == "9":
        import Grafos as Graph
        
    #salir -------------------------------------------> 8 
    elif num == "0":
        break

print("Usted ha salido del programa\n")


      
      
      
      

        
    