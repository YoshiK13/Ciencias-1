# Reglas
# 1) Lista de 0 a n-1. Con n de la forma 0 < n < 25

# 2) move a onto b: pone el bloque "a" sobre el bloque "b" despues de devolver los bloques que 
# estubieran sobre "a" y "b" a sus posiciones originales

# 3) move a over b: coloca el bloque "a" sobre la pila que contiene el bloque "b",  despues de
# regersar a sus posiciones originlaes los bloques sobre ql bloque "a"

# 4) pile a onto b: mueve la pila de bloques del bloque "a" y todos los bloques que estan apilados
# sobre el bloque "a" (manteniendo su orden), encima del bloque "b", despues de regresar todos los 
# bloques apilados sobre el bloque "b" a sus posiciones originales

# 5) pile a over b: pone la pila de bloques del bloque "a" y todos los bloques que estan apilados
# sobre el bloque "a" (manteniendo su orden), sobre la pila que contenga el bloque "b"

# 6) quit: termina el ingreso de comandos

# 7) Todo comando donde a = b debe ser ignorado

# Por:
# Davidson Esfleider Sanchez Gordillo - 20231020183
# Diego Felipe Diaz Roa - 20201020147
# Dania Lizeth Guzmán Triviño - 20221020061
# Joshoa Alarcon Sanchez - 20221020013

def ordenar_bloques():
    # Numero de bloques
    cant_bloques = int(input())
    
    # Lista de las pilas que continen bloques
    pilas_bloques = [[i] for i in range(cant_bloques)]
    
    # Registro para saber donde esta cada
    posicion_bloques = {i: i for i in range(cant_bloques)}

    # Regresar bloques encima de un "bloque" a su posicion original
    def regresar_bloques(bloque):
        pos = posicion_bloques[bloque]
        bloque_index = pilas_bloques[pos].index(bloque)
        
        # Obtener los bloques que estan encima
        bloques_encima = pilas_bloques[pos][bloque_index + 1:]
        
        # Removerlos de la pila
        pilas_bloques[pos] = pilas_bloques[pos][:bloque_index + 1]
        
        # Regresarlos a su posicion inicial
        for i_bloque in bloques_encima:
            pilas_bloques[i_bloque] = [i_bloque]
            posicion_bloques[i_bloque] = i_bloque
    
    # Mover un bloque y todos los que tienne encima a otra pila
    def mover_pila(bloque, pila_deseada):
        pos_origen = posicion_bloques[bloque]
        bloque_index = pilas_bloques[pos_origen].index(bloque)
        
        # Obtener la pila que incluye el bloque y todos los de encima
        pila = pilas_bloques[pos_origen][bloque_index:]
        
        # Remover la pila del stack original
        pilas_bloques[pos_origen] = pilas_bloques[pos_origen][:bloque_index]
        
        # Agregar la pila al stack destino
        pilas_bloques[pila_deseada].extend(pila)
        
        # Actualizar las posiciones de todos los bloques movidos
        for i_bloque in pila:
            posicion_bloques[i_bloque] = pila_deseada

   # Checkeo si los bloques_a y bloque_b estan en la misma pila 
    def misma_pila(bloque_a, bloque_b):
        return posicion_bloques[bloque_a] == posicion_bloques[bloque_b]
    
    # Procesar comandos
    while True:
        instruccion = input().strip().split()
        
        # Instruccion de saliada "quit"
        if instruccion[0] == "quit":
            break
        
        tipo_instruccion = instruccion[0]
        bloque_a = int(instruccion[1])
        operacion = instruccion[2]  # Tipo de operacion "onto" o "over"
        bloque_b = int(instruccion[3])
        
        # Evitar comandos ilegales
        if bloque_a == bloque_b or misma_pila(bloque_a, bloque_b):
            continue
        
        # Comando "move"
        if tipo_instruccion == "move":
            regresar_bloques(bloque_a)
            
            # Operacion "onto"
            if operacion == "onto":
                regresar_bloques(bloque_b)
                pila_deseada = posicion_bloques[bloque_b]

            # Operacion "over"
            else:
                pila_deseada = posicion_bloques[bloque_b]
            
            # Quitar el bloque_a de su pila original
            pos_origen = posicion_bloques[bloque_a]
            pilas_bloques[pos_origen].remove(bloque_a)
            
            # Mover el bloque_a a la pila del bloque_b
            pilas_bloques[pila_deseada].append(bloque_a)
            posicion_bloques[bloque_a] = pila_deseada

        # Comando "pile"    
        elif tipo_instruccion == "pile":
            
            # Operacion "onto"
            if operacion == "onto":
                regresar_bloques(bloque_b)
                pila_deseada = posicion_bloques[bloque_b]
            
            # Operacion "over"
            else:
                pila_deseada = posicion_bloques[bloque_b]
            
            # Mover la pila completa
            mover_pila(bloque_a, pila_deseada)
    
    # Regresar el output con formato
    for i in range(cant_bloques):
        if pilas_bloques[i]:
            print(f"{i}: " + " ".join(map(str, pilas_bloques[i])))
        else:
            print(f"{i}:")

# Ejecutar el simulador
ordenar_bloques()