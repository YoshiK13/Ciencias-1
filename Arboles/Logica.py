# 1) Binarios y realizar operaciones básicas como insercion, busqueda y borrado.
# Haciendo usos de resursividad, donde cada nodo puede verse como un árbol en sí mismo.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []
        self.padre = None

    def agregar_hijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

    def eliminar_nodo(self, hijo):
        hijo.padre = None
        self.hijos.remove(hijo)

class NodoBinario(Nodo):

    def __init__(self, valor):
        super().__init__(valor)
        self.hijos = [None, None] # Inicializa con dos hijos vacios

    def agregar_hijo(self, hijo):
        # Si el valor del hijo es menor o igual al nodo actual, va al hijo izquierdo (indice 0)
        # Si es mayor, va al hijo derecho (indice 1)
        # Y se hace de manera recursiva
        if hijo.valor <= self.valor:
            if self.hijos[0] is None:
                self.hijos[0] = hijo
                hijo.padre = self
            else:
                self.hijos[0].agregar_hijo(hijo)

        else:
            if self.hijos[1] is None:
                self.hijos[1] = hijo
                hijo.padre = self
            else:
                self.hijos[1].agregar_hijo(hijo)

    # Se busca entre los hijos de manera recursiva segun el valor
    def buscar_nodo(self, valor):
        nodos_encontrados = []
    
        if self.valor == valor:
            nodos_encontrados.append(self)
    
        # Buscar en el subarbol izquierdo
        if self.hijos[0] is not None and  valor <= self.valor:
            nodos_encontrados.extend(self.hijos[0].buscar_nodo(valor))
    
        # Buscar en el subarbol derecho
        if self.hijos[1] is not None and valor >= self.valor:
            nodos_encontrados.extend(self.hijos[1].buscar_nodo(valor))
    
        return nodos_encontrados

    # Funcion nesesaria para eliminar nodos con dos hijos, busca el minimo en el subarbol derecho
    def encontrar_minimo(self):
        nodo_actual = self
        while nodo_actual.hijos[0] is not None:
            nodo_actual = nodo_actual.hijos[0]

        return nodo_actual

    def eliminar_nodo(self, valor):
        nodos_encontrados = self.buscar_nodo(valor)

        # Si no se encontro el nodo, retornar None
        if not nodos_encontrados:
            return None
        
        # Tomar el primer nodo encontrado
        nodo_eliminar = nodos_encontrados[0]

        # Caso 1: Nodo sin hijos
        if nodo_eliminar.hijos[0] is None and nodo_eliminar.hijos[1] is None:
            if nodo_eliminar.padre is not None:
                if nodo_eliminar.padre.hijos[0] == nodo_eliminar:
                    nodo_eliminar.padre.hijos[0] = None
                else:
                    nodo_eliminar.padre.hijos[1] = None
                nodo_eliminar.padre = None
            
            return nodo_eliminar

        # Caso 2: Nodo con un solo hijo
        elif nodo_eliminar.hijos[0] is None or nodo_eliminar.hijos[1] is None:
            hijo = nodo_eliminar.hijos[0] if nodo_eliminar.hijos[0] is not None else nodo_eliminar.hijos[1]
            
            if nodo_eliminar.padre is not None:
                if nodo_eliminar.padre.hijos[0] == nodo_eliminar:
                    nodo_eliminar.padre.hijos[0] = hijo
                else:
                    nodo_eliminar.padre.hijos[1] = hijo
                hijo.padre = nodo_eliminar.padre
            
            else:
                hijo.padre = None # Si el nodo a eliminar es la raiz, su hijo se convierte en la nueva raiz
            
            nodo_eliminar.padre = None
            return nodo_eliminar

        # Caso 3: Nodo con dos hijos
        else:
            # Encontrar el minimo en el subarbol derecho
            sucesor = nodo_eliminar.hijos[1].encontrar_minimo()
            valor_sucesor = sucesor.valor
            self.eliminar_nodo(sucesor.valor)
            nodo_eliminar.valor = valor_sucesor
            
            return nodo_eliminar