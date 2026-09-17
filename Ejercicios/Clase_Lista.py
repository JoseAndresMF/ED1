class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class Lista_Enlazada:

    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    # Agregamos un nuevo dato al inicio (a la cabeza)
    def agregar_nodo_inicio(self,dato):
        nuevo_nodo = Nodo(dato)

        nuevo_nodo.siguiente = self.cabeza

        self.cabeza = nuevo_nodo
        self.longitud +=1

    def agregar_nodo(self,dato):
        nuevo_nodo = Nodo(dato)
        
        # Si la lista esta vacia
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.longitud +=1
            return

        # Si la lista contiene al menos un nodo
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
            
        actual.siguiente = nuevo_nodo
        self.longitud += 1
        

    def mostrar(self):
        actual = self.cabeza
        elementos = []

        while actual is not None:
            elementos.append(str(actual.dato)+ " -->")
            actual = actual.siguiente

        print( "".join(elementos) + " None")

    def longitud_lista(self) -> int:
        actual = self.cabeza
        contador = 0

        while actual is not None:
            contador +=1
            actual = actual.siguiente

        return contador

    # Elimina la primera ocurrencia del dato. O(n)
    def eliminar_nodo(self, dato):     
        # Si esta vacia
        if self.cabeza is None:
            print("La lista esta vacia")
            return

        # Si el dato es la cabeza
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            self.longitud -=1
            return

        anterior = self.cabeza
        actual = self.cabeza.siguiente 
        while actual is not None:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente
                self.longitud -=1
                return
            anterior = actual
            actual = actual.siguiente

    def eliminar_nodo_por_indice(self, indice):
        if indice > self.longitud_lista():
            print("Indice fuera de rango")
            return

        if indice == 0: 
            self.cabeza = self.cabeza.siguiente
            self.longitud -=1
            return

        anterior = self.cabeza
        actual = self.cabeza.siguiente
        for i in range(1,self.longitud_lista()):
            if actual is None: 
                print("Indice fuera de Ranguito")
            if i == indice:
                anterior.siguiente = actual.siguiente
                self.longitud -=1
                return
            anterior = actual
            actual = actual.siguiente

        self.longitud =-1
        


lista = Lista_Enlazada()

lista.agregar_nodo(22)
lista.agregar_nodo(33)
lista.agregar_nodo(44)
lista.agregar_nodo(55)

lista.mostrar()
print(lista.longitud)

lista.agregar_nodo_inicio(11)

lista.mostrar()
print(lista.longitud)

"""
lista.eliminar_nodo(30)
lista.eliminar_nodo(50)
lista.mostrar()
print(lista.longitud_lista())
"""

lista.eliminar_nodo_por_indice(6)
lista.mostrar()
##print(lista.longitud_lista())
print(lista.longitud)