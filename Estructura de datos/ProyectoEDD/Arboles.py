# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 22:56:37 2021

@author: MedNo
"""


class arbolBinario():
    class nodoArbol():
        def __init__(self, nombre, dato):
            self.nombre = nombre.title()
            self.dato = dato
            self.hijoIzq = None
            self.hijoDer = None
        def __str__(self):
            return self.nombre + " - " + str(self.dato)
    def __init__(self):
        self.raiz = None
    def crearNodo(self, nombre, dato):
        nuevo = self.nodoArbol(nombre, dato)
        if self.raiz == None: self.raiz = nuevo
        else:
            aux = self.raiz
            while(True):
                padre = aux
                if (dato < aux.dato):
                    aux=aux.hijoIzq
                    if (aux == None):
                        padre.hijoIzq = nuevo
                        return
                else:
                    aux = aux.hijoDer
                    if(aux == None):
                        padre.hijoDer = nuevo
                        return
    def arbolVacio(self): 
        if self.raiz == None: return True
        else: return False
    def buscarNodo(self, dato):
        aux = self.raiz
        while aux.dato != dato:
            if dato < aux.dato: aux = aux.hijoIzq
            else: aux = aux.hijoDer
            if aux == None: return None
        return aux
    def obtenerReemplazo(self, nodo):
        reemplazarPadre = nodo
        reemplazo = nodo
        aux = nodo.hijoDer
        while aux != None:
            reemplazarPadre = reemplazo
            reemplazo = aux
            aux = aux.hijoIzq
        if reemplazo != nodo.hijoDer:
            reemplazarPadre.hijoIzq = reemplazo.hijoDer
            reemplazo.hijoDer = nodo.hijoDer
        print("El nodo reemplazo es " + str(reemplazo))
        return reemplazo
    def eliminarNodo(self, dato):
        aux = self.raiz
        padre = self.raiz
        esHijoIzq = True
        while aux.dato != dato:
            padre = aux
            if dato < aux.dato:
                esHijoIzq = True
                aux = aux.hijoIzq
            else:
                esHijoIzq = False
                aux = aux.hijoDer
            if aux == None: return False
        if aux.hijoIzq == None and aux.hijoDer == None:
            if aux == self.raiz: self.raiz = None
            elif esHijoIzq: padre.hijoIzq = None
            else: padre.hijoDer = None
        elif aux.hijoDer == None:
            if aux == self.raiz: self.raiz = aux.hijoIzq
            elif esHijoIzq: padre.hijoIzq = aux.hijoIzq
            else: padre.hijoDer = aux.hijoIzq
        elif aux.hijoIzq == None:
            if aux == self.raiz: self.raiz = aux.hijoDer
            elif esHijoIzq: padre.hijoIzq = aux.hijoDer
            else: padre.hijoDer = aux.hijoDer
        else:
            reemplazo = self.obtenerReemplazo(aux)
            if aux == self.raiz: self.raiz = reemplazo
            elif esHijoIzq: padre.hijoIzq = reemplazo
            else: padre.hijoDer = reemplazo
            reemplazo.hijoIzq = aux.hijoIzq
        return True
    def preorden(self, r):
        if r != None:
            print(r.nombre + " - " + str(r.dato))
            self.preorden(r.hijoIzq)
            self.preorden(r.hijoDer)
    def inorden(self, r): 
        if r != None:
            self.inorden(r.hijoIzq)
            print(r.nombre + " - " + str(r.dato))
            self.inorden(r.hijoDer)
    def postorden(self, r):
        if r != None:
            self.postorden(r.hijoIzq)
            self.postorden(r.hijoDer)
            print(r.nombre + " - " + str(r.dato))
                            


Calificaciones = arbolBinario()
opcion = "1"
while (opcion != "0"):
    print ("Usted ha elegido la opcion: 8\n")
    print ('------Arbol------'. center(30))
    print("\nConsumo de gasolina en Automoviles")
    print("1. Ingresar un Automovil")
    print("2. Eliminar un Automovil")
    print("3. Buscar un Automovil")
    print("4. Recorrido en preorden")
    print("5. Recorrido en inorden")
    print("6. Recorrido en postorden")
    print("0. Deseo salir")
    
    opcion = input("Digite una opcion: ")

    if (opcion == "1"):
        num = input("Cuantos Automoviles quieres agregar? ")

        for i in range (int(num)):
            nombre = input("Nombre del Automovil: ")
            dato = input("Cuantos kilometros por litro consume: ")
            Calificaciones.crearNodo(nombre, int(dato))
            
    if (opcion == "2"):
        if not Calificaciones.arbolVacio():
            dato = input("Kilometraje: ")

            if not Calificaciones.eliminarNodo(int(dato)): print("Nodo no encontrado.")
            else: print("El nodo ha sido eliminado.")
        else: print("El árbol está vacío. No hay nada que eliminar.")
        input("\nPresiona ENTER para continuar.")
    
    if (opcion == "3"):
        if not Calificaciones.arbolVacio():
            dato = input("Ingresa un Kilometraje valido para buscar en el árbol: ")
            dato=int(dato)
            n = Calificaciones.buscarNodo(dato)
            if n is None: print(f"{dato} no existe en el árbol")
            else: print("Nodo encontrado. ", str(Calificaciones.buscarNodo(dato)))
        else: print("El árbol está vacío. No hay nada que buscar.")
        input("\nPresiona ENTER para continuar.")
    
    if (opcion == "4"): 
        if not Calificaciones.arbolVacio(): Calificaciones.preorden(Calificaciones.raiz)
        else: print("El árbol está vacío. No se puede recorrer.")
        input("\nPresiona ENTER para continuar.")
    
    if (opcion == "5"):
        if not Calificaciones.arbolVacio(): Calificaciones.inorden(Calificaciones.raiz)
        else: print("El árbol está vacío. No se puede recorrer.")
        input("\nPresiona ENTER para continuar.")
    
    if (opcion == "6"):
        if not Calificaciones.arbolVacio(): Calificaciones.postorden(Calificaciones.raiz)
        else: print("El árbol está vacío. No se puede recorrer.")
        input("\nPresiona ENTER para continuar.")