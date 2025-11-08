# Hacer un programa que sirva apara crear, visualizas y editar arboles.
# Tipos de arboles que se pueden usar: Binario y AVL
# Funciones: Insertar, Buscar, Eliminar, Mostrar

# Integrantes:
# Davidson Esfleider Sanchez Gordillo - 20231020183
# Diego Felipe Diaz Roa - 20201020147
# Dania Lizeth Guzmán Triviño - 20221020061
# Joshoa Alarcon Sanchez - 20221020013

from Logica import NodoBinario, NodoAVL

# Codigos ANSI para colores
CYAN = "\033[36m"
RESET = "\033[0m"

class App:
    def __init__(self):
        self.raiz = None

        # Verificar el tipo de arbol a usar
        while True:
            print("Seleccione el tipo de árbol a usar:")
            print("1. Binario")
            print("2. AVL")
            opcion = input("Ingrese 1 o 2: ").strip()
            if opcion == "1":
                self.tipo = "binario"
                break
            elif opcion == "2":
                self.tipo = "avl"
                break
            else:
                print("Opcion invalida para la seleccion de tipo de arbol. Intenta de nuevo. \n")

        print(f"Usando árbol: {self.tipo}\n")

    def insertar(self, valor):
        # Crear el tipo de nodo segun la eleccion del usuario
        if self.tipo == "avl":
            nuevo_nodo = NodoAVL(valor)

            if self.raiz is None:
                self.raiz = nuevo_nodo
                print(f"Nodo {valor} insertado como raiz")

            else:
                # En AVL, agregar_hijo puede devolver una nueva raiz para el subárbol
                self.raiz = self.raiz.agregar_hijo(nuevo_nodo)
                print(f"Nodo {valor} insertado (AVL)")

        else:
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

        # Si se va a eliminar la raiz
        if self.raiz.valor == valor:
            # Mantener el mismo comportamiento para binarios y AVL en los casos simples
            if self.raiz.hijos[0] is None and self.raiz.hijos[1] is None:
                self.raiz = None
                print(f"Raiz eliminada, el arbol esta vacio")
            
            elif self.raiz.hijos[0] is None:
                self.raiz = self.raiz.hijos[1]

                if self.raiz is not None:
                    self.raiz.padre = None

                print(f"Raiz eliminada")
            
            elif self.raiz.hijos[1] is None:
                self.raiz = self.raiz.hijos[0]

                if self.raiz is not None:
                    self.raiz.padre = None

                print(f"Raiz eliminada")
            
            else:
                sucesor = self.raiz.hijos[0].encontrar_maximo_izq()
                valor_sucesor = sucesor.valor

                # Para AVL, eliminar_nodo puede rebalancear; usamos la llamada y luego reasignamos la raiz si es necesario
                if self.tipo == "avl":
                    resultado = self.raiz.eliminar_nodo(valor_sucesor)

                    # Manejar ambos posibles formatos de retorno (tupla nueva_raiz, eliminado) o la forma antigua
                    if isinstance(resultado, tuple) and len(resultado) == 2:
                        nueva_raiz, eliminado = resultado
                        # reasignar la raiz si la operación produjo una nueva raiz
                        self.raiz = nueva_raiz if nueva_raiz is not None else None
                        if self.raiz is not None:
                            self.raiz.padre = None

                    elif isinstance(resultado, (NodoAVL, NodoBinario)):
                        self.raiz = resultado

                else:
                    self.raiz.eliminar_nodo(valor_sucesor)

                self.raiz.valor = valor_sucesor
                print(f"Raiz eliminada")
        
        else:
            if self.tipo == "avl":
                resultado = self.raiz.eliminar_nodo(valor)

                # Manejar la nueva firma: (nueva_raiz, eliminado)
                if isinstance(resultado, tuple) and len(resultado) == 2:
                    nueva_raiz, eliminado = resultado
                    if not eliminado:
                        print(f"No se encontro el nodo con valor {valor}")
                    else:
                        self.raiz = nueva_raiz
                        if self.raiz is not None:
                            self.raiz.padre = None
                        print(f"Nodo {valor} eliminado")

                else:
                    # Compatibilidad con implementaciones antiguas
                    if resultado is None:
                        print(f"No se encontro el nodo con valor {valor}")
                    else:
                        if isinstance(resultado, (NodoAVL, NodoBinario)):
                            self.raiz = resultado
                        print(f"Nodo {valor} eliminado")

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
        # Formatear la representación del nodo. Si es un NodoAVL, mostrar (valor, factor)
        if isinstance(nodo, NodoAVL):
            # Mostrar el factor de balanceo en cian
            repr_nodo = f"({nodo.valor}, {CYAN}{nodo.factor_balance}{RESET})"

        else:
            repr_nodo = f"{nodo.valor}"

        if es_izquierdo is None:
            # Es la raíz
            print(f"{repr_nodo}")
        
        elif es_izquierdo:
            print(f"{prefijo}├── {repr_nodo}")
        
        else:
            print(f"{prefijo}└── {repr_nodo}")
        
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
            # Mostrar titulo según el tipo de arbol seleccionado
            if getattr(self, 'tipo', None) == 'avl':
                print("  SISTEMA DE MANEJO DE ARBOLES AVL")

            else:
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

                if getattr(self, 'tipo', None) == 'avl':
                    print(f"Arbol AVL con factores de balance mostrados en {CYAN}cian{RESET}.\n")

                self.mostrar_arbol()
            
            elif opcion == "5":
                print("\nGracias por usar el sistema.")
                break
            
            else:
                print("Opcion invalida. Intenta de nuevo.")


# Ejecutar la aplicacion
app = App()
app.menu()