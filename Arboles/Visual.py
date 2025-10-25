# Hacer un programa que sirva apara crear, visualizas y editar arboles. 

# Integrantes:
# Davidson Esfleider Sanchez Gordillo - 20231020183
# Diego Felipe Diaz Roa - 20201020147
# Dania Lizeth Guzmán Triviño - 20221020061
# Joshoa Alarcon Sanchez - 20221020013

from Logica import NodoBinario

class App:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo_nodo = NodoBinario(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            print(f"Nodo {valor} insertado como raiz")

        else:
            self.raiz.agregar_hijo(nuevo_nodo)
            print(f"Nodo {valor} insertado")

    def buscar(self, valor):
        if self.raiz is None:
            print("El arbol esta vacio")
            return None
        
        nodos = self.raiz.buscar_nodo(valor)
        if nodos:
            print(f"Se encontraron {len(nodos)} nodo(s) con valor {valor}")
            return nodos
        
        else:
            print(f"No se encontró ningún nodo con valor {valor}")
            return None

    def eliminar(self, valor):
        if self.raiz is None:
            print("El arbol esta vacio")
            return None
        
        # Si se va a eliminar la raíz
        if self.raiz.valor == valor:
            if self.raiz.hijos[0] is None and self.raiz.hijos[1] is None:
                self.raiz = None
                print(f"Raiz eliminada, el arbol esta vacio")
            
            elif self.raiz.hijos[0] is None:
                self.raiz = self.raiz.hijos[1]
                self.raiz.padre = None
                print(f"Raiz eliminada")
            
            elif self.raiz.hijos[1] is None:
                self.raiz = self.raiz.hijos[0]
                self.raiz.padre = None
                print(f"Raiz eliminada")
            
            else:
                sucesor = self.raiz.hijos[1].encontrar_minimo()
                valor_sucesor = sucesor.valor
                self.raiz.eliminar_nodo(valor_sucesor)
                self.raiz.valor = valor_sucesor
                print(f"Raiz eliminada")
        
        else:
            nodo = self.raiz.eliminar_nodo(valor)
            if nodo:
                print(f"Nodo {valor} eliminado")
            
            else:
                print(f"No se encontro el nodo con valor {valor}")

    # Mostrar el arbol de forma visual
    def mostrar_arbol(self, nodo=None, prefijo="", es_izquierdo=None):
        if nodo is None:
            if self.raiz is None:
                print("El arbol esta vacio")
                return
            
            # Mostrar la raiz centrada
            self._mostrar_arbol_recursivo(self.raiz, "", None)
            print()
            return
    
    # Funcion recursiva para mostrar el arbol
    def _mostrar_arbol_recursivo(self, nodo, prefijo, es_izquierdo):
        if nodo is None:
            return
        
        # Determinar el conector
        if es_izquierdo is None:
            # Es la raíz
            print(f"{nodo.valor}")
        
        elif es_izquierdo:
            print(f"{prefijo}├── {nodo.valor}")
        
        else:
            print(f"{prefijo}└── {nodo.valor}")
        
        # Preparar el nuevo prefijo para los hijos
        if es_izquierdo is None:
            nuevo_prefijo = ""
        
        elif es_izquierdo:
            nuevo_prefijo = prefijo + "│   "
        
        else:
            nuevo_prefijo = prefijo + "    "

        # Mostrar hijos (primero izquierdo, luego derecho)
        if nodo.hijos[0] is not None or nodo.hijos[1] is not None:
            if nodo.hijos[0] is not None:
                self._mostrar_arbol_recursivo(nodo.hijos[0], nuevo_prefijo, True)
            
            else:
                print(f"{nuevo_prefijo}├──  ⃠")
            
            if nodo.hijos[1] is not None:
                self._mostrar_arbol_recursivo(nodo.hijos[1], nuevo_prefijo, False)
            
            else:
                print(f"{nuevo_prefijo}└──  ⃠")

    def menu(self):
        while True:
            print("\n" + "="*50)
            print("  SISTEMA DE MANEJO DE ARBOLES BINARIOS")
            print("="*50)
            print("1. Insertar nodo")
            print("2. Buscar nodo")
            print("3. Eliminar nodo")
            print("4. Mostrar árbol")
            print("5. Salir")
            print("="*50)
            
            opcion = input("\nSeleccione una opcion: ").strip()
            
            if opcion == "1":
                try:
                    valor = int(input("Ingrese el valor del nodo: "))
                    self.insertar(valor)
                except ValueError:
                    print("Error: Ingrese un numero valido")

            elif opcion == "2":
                try:
                    valor = int(input("Ingrese el valor a buscar: "))
                    self.buscar(valor)
                except ValueError:
                    print("Error: Ingrese un numero valido")

            elif opcion == "3":
                try:
                    valor = int(input("Ingrese el valor del nodo a eliminar: "))
                    self.eliminar(valor)
                except ValueError:
                    print("Error: Ingrese un numero valido")
            
            elif opcion == "4":
                print("\n--- VISUALIZACION DEL ARBOL ---")
                self.mostrar_arbol()
            
            elif opcion == "5":
                print("\nGracias por usar el sistema.")
                break
            
            else:
                print("Opcion invalida. Intenta de nuevo.")


# Ejecutar la aplicacion
app = App()
app.menu()