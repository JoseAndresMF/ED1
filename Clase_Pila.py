class Nodo():
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class Pila():
    def __init__(self):
        self.tope = None

    # PUSH: apilar un nuevo nodo al tope
    def apilar_nodo(self,dato):
        nuevo_nodo = Nodo(dato)

        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        print("PUSH: Nodo apilado, el nuevo tope es: ", self.tope.dato)

    # POP: Elimina el tope y devuelve ese dato
    def desapilar_nodo(self):
        if self.tope is None:
            print("Error: La pila esta vacia")
            return

        dato_desapilado = self.tope.dato
        self.tope = self.tope.siguiente
        print("POP: tope eliminado y devuelvo: ",dato_desapilado)
        return dato_desapilado

    # PEEK: Devolvemos el dato del tope sin eliminarlo
    def ver_tope(self):
        if self.tope is None:
            print("Error: No hay tope(Pila vacia)")
            return

        print("PEEK: El dato del tope es: ", self.tope.dato)
        return self.tope.dato

    # Verificar si la pila esta vacia
    def esta_vacia(self):
        return (self.tope is None)

    # Imprimir la pila
    def mostrar(self):
        actual = self.tope
        elemetos = []

        while actual is not None:
            elemetos.append(f"  | {actual.dato} |")
            actual = actual.siguiente

        print("\n -- TOPE --")
        print("\n".join(elemetos))
        print(" -------")

pila = Pila()

pila.apilar_nodo(5)
pila.apilar_nodo(10)
pila.apilar_nodo(15)
pila.apilar_nodo(35)
pila.apilar_nodo(50)

pila.mostrar()

pila.desapilar_nodo()
pila.desapilar_nodo()

pila.ver_tope()

pila.mostrar()


        
    