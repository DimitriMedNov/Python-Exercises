# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:20:18 2021

@author: MedNo
"""
    
# lugares de cómo quedaron los atletas después de una carrera

class CircularLinkedList():
    class Runner():
        def __init__(self, name):
            if (name.isalpha()): self.name = name
            else:
                while ((all(name.isalpha() or name.isspace() for name in name))):
                    name = input("Ingresa un nombre válido.")
                self.name = name
            self.previousRunner = None
            self.nextRunner = None
    def __init__(self):
        self.head = None
        self.tail = None
        self.numRunners = 0
    def printList(self):
        array = []
        currentRunner = self.head
        pivot = True
        counter = self.numRunners
        while counter != 0:
            if pivot != False or currentRunner != self.head:
                array.append(currentRunner.name.title())
                currentRunner = currentRunner.nextRunner
                pivot = False
                counter -=1 
            else:
                break
        print("\nCarrera Anahuac Mayab 2021")
        print(str(array))
        print("Número de participantes: ", str(self.numRunners), "\n")
    def prepend(self, name):
        newRunner = self.Runner(name)
        if self.head == None and self.tail == None:
            self.head = newRunner
            self.tail = newRunner
        else:
            self.head.previousRunner = newRunner
            newRunner.nextRunner = self.head
            self.tail.nextRunner = newRunner
            newRunner.previousRunner = self.tail
            self.head = newRunner
        self.numRunners += 1
    def append(self, name):
        newRunner = self.Runner(name)
        if self.head == None and self.tail == None:
            self.head = newRunner
            self.tail = newRunner
        else:
            self.tail.nextRunner = newRunner
            newRunner.previousRunner = self.tail
            newRunner.nextRunner = self.head
            self.head.previousRunner = newRunner
            self.tail = newRunner
        self.numRunners += 1
    def shift(self):
        if self.numRunners == 0:
            print("No hay participantes")
            self.head = None
            self.tail = None
        else:
            deletedRunner = self.head
            self.head = deletedRunner.nextRunner
            self.head.previousRunner = self.tail
            self.tail.nextRunner = self.head
            deletedRunner.previousRunner = None
            deletedRunner.nextRunner = None
            self.numRunners -= 1
            return print(deletedRunner.name)
    def pop(self):
        if self.numRunners == 0:
            print("No hay participantes")
            self.head = None
            self.tail = None
        else:
            deletedRunner = self.tail
            self.tail = deletedRunner.previousRunner
            self.tail.nextRunner = self.head
            self.head.previousRunner = self.tail
            deletedRunner.previousRunner = None
            deletedRunner.nextRunner = None
            self.numRunners -= 1
            return print(deletedRunner.name)
    def get(self, position):
        if int(position) == self.numRunners - 1:
            print(self.tail.name)
            return self.tail
        elif int(position) == 0:
            print(self.head.name)
            return self.head
        elif not (int(position) >= self.numRunners or int(position) < 0):
            balancedPosition = int(self.numRunners / 2)
            if (int(position) <= balancedPosition):
                currentRunner = self.head
                counter = 0
                while counter != int(position):
                    currentRunner = currentRunner.nextRunner
                    counter += 1
                print(currentRunner.name)
                return currentRunner
            else:
                currentRunner = self.tail
                counter = self.numRunners - 1
                while counter != int(position):
                    currentRunner = currentRunner.previousRunner
                    counter -= 1
                print(currentRunner.name)
                return currentRunner
        else: print("Posición no válida. Te regresamos al menú.")
        
        
        
    def update(self, position, name):
        targetRunner = self.get(position)
        if targetRunner != None:
             if (name.isalpha()): targetRunner.name = name
             else:
                while ((all(name.isalpha() or name.isspace() for name in name))):
                    name = input("Ingresa un nombre válido.")
                targetRunner.name = name
        else: print("Posición no válida. Te regresamos al menú.")
        
        
        
        
    def insert(self, position, name):
        if int(position) == self.numRunners - 1:
            return self.append(name)
        elif not (int(position) >= self.numRunners or int(position) < 0):
            newRunner = self.Runner(name)
            previousRunners = self.get(position)
            nextRunners = previousRunners.nextRunner
            previousRunners.nextRunner = newRunner
            newRunner.previousRunner = previousRunners
            newRunner.nextRunner = nextRunners
            nextRunners.previousRunner = newRunner
            self.numRunners += 1
        else: print("Posición no válida. Te regresamos al menú.")
        
        
        
    def remove(self, position):
        if int(position) == 0:
            return self.shift()
        elif int(position) == self.numRunners - 1:
            return self.pop()
        elif not (int(position) >= self.numRunners or int(position) < 0):
            removedRunner = self.get(position)
            previousRunners = removedRunner.previousRunner
            nextRunners = removedRunner.nextRunner
            previousRunners.nextRunner = nextRunners
            nextRunners.previousRunner  = previousRunners
            removedRunner.previousRunner = None
            removedRunner.nextRunner = None
            self.numRunners -= 1
            return removedRunner
        else: print("Posición no válida. Te regresamos al menú.")
        
        
        
    def reverse(self):
        if (self.numRunners > 1):
            revertedRunners = None
            self.head.previousRunner = None
            self.tail.nextRunner = None
            currentRunner = self.head
            self.tail = currentRunner
            while currentRunner != None:
                revertedRunners = currentRunner.previousRunner
                currentRunner.previousRunner = currentRunner.nextRunner
                currentRunner.nextRunner = revertedRunners
                currentRunner = currentRunner.previousRunner
            self.head = revertedRunners.previousRunner
            self.head.previousRunner = self.tail
            self.tail.nextRunner = self.head
        else: print("No hay suficientes participantes para revertir. Te regresamos al menú.")


lugares = CircularLinkedList()
opcion = "1"
while (opcion != "0"):
    lugares.printList()
    print ("Usted ha elegido la opcion: 5\n")
    print ('------Lista Circular------'. center(30))
    print("1. Agregar un participante al inicio")
    print("2. Agregar un participante al final")
    print("3. Sacar al primer participante de la lista")
    print("4. Sacar al último participante de la lista")
    print("5. Obtener el nombre de un participante según su lugar")
    print("6. Cambiar el participante de cierto lugar")
    print("7. Agregar nuevo participante en cierto lugar")
    print("8. Eliminar el participante de cierto lugar")
    print("9. Revertir la tabla de participantes")
    print("0. Salir")
    opcion = input(" Digite una opcion: ")
    
    if (opcion == "1"):
        corredor = input("participante: ")
        lugares.prepend(corredor)
    
    if (opcion == "2"):
        corredor = input("participante: ")
        lugares.append(corredor)
    
    if (opcion == "3"): lugares.shift()
    
    if (opcion == "4"): lugares.pop()
    
    if (opcion == "5"): 
        position = input("Posición: ")
        lugares.get(position)
    
    if (opcion == "6"):
        position = input("Posición: ")
        name = input("participante: ")
        lugares.update(position, name)
    
    if (opcion == "7"): 
        position = input("Posición: ")
        name = input("participante: ")
        lugares.insert(position, name)
    
    if (opcion == "8"):
        position = input("Posición: ")
        lugares.remove(position)
    
    if (opcion == "9"): lugares.reverse()
                
