def resolver_min_cover():
    def caso_individual():
        M = int(input())
        segmentos = []
        
        # Leer datos
        while True:
            linea = input().strip()
            if linea == "0 0":
                break
            L, R = map(int, linea.split())

            if R >= 0 and L <= M:
                segmentos.append((L, R))
        
        if not segmentos:
            return 0, []
        
        # Organizar elementos
        segmentos.sort()
        
        # Aplicar algoritmo voraz
        resultado = []
        pos_actual = 0
        i = 0
        
        while pos_actual < M and i < len(segmentos):
            if segmentos[i][0] > pos_actual:
                return 0, []
            
            extremo_derecho = pos_actual
            mejor_segmento = None
            
            while i < len(segmentos) and segmentos[i][0] <= pos_actual:
                if segmentos[i][1] > extremo_derecho:
                    extremo_derecho = segmentos[i][1]
                    mejor_segmento = segmentos[i]
                i += 1
            
            if extremo_derecho <= pos_actual:
                return 0, []
            
            resultado.append(mejor_segmento)
            pos_actual = extremo_derecho
        
        # Comprobar que se cubrió de 0 a M
        if pos_actual >= M:
            return len(resultado), resultado
        else:
            return 0, []
    
    # Leer input
    T = int(input())
    input()  # Leer espacio
    
    for case in range(T):
        count, segmentos = caso_individual()
        
        if count == 0:
            print("0")
        else:
            print(count)
            for L, R in segmentos:
                print(L, R)
        
        if case < T - 1:
            print()
            input()

resolver_min_cover()