# Por:
# Davidson Esfleider Sanchez Gordillo - 20231020183
# Diego Felipe Diaz Roa - 20201020147
# Dania Lizeth Guzmán Triviño - 20221020061
# Joshoa Alarcon Sanchez - 20221020013

def criba_eratostenes(maximo):
    es_primo = [True] * (maximo + 1)
    es_primo[0] = es_primo[1] = False

    for i in range(2, int(maximo ** 0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, maximo + 1, i):
                es_primo[j] = False

    return es_primo

def backtrack(n, es_primo, disposicion, usado, posicion, soluciones):
    if posicion == n:
        if es_primo[disposicion[-1] + disposicion[0]]:
            soluciones.append(disposicion.copy())
        return

    for num in range(2, n + 1):
        if not usado[num] and es_primo[disposicion[posicion - 1] + num]:
            disposicion[posicion] = num
            usado[num] = True
            backtrack(n, es_primo, disposicion, usado, posicion + 1, soluciones)
            usado[num] = False


def generar_resultados(n, soluciones):
    resultado = []
    for i, solucion in enumerate(soluciones, 1):
        resultado.append(" ".join(map(str, solucion)))

    return resultado

def main():
    while True:
        try:
            resultado = []

            for i in range(2):
                n = int(input())
                if n <= 0:
                    print("El tamaño debe ser un número positivo.")
                    continue
                if n > 16:
                    print("Advertencia: Para n > 16 el cálculo puede tomar mucho tiempo.")
                    continue

                es_primo = criba_eratostenes(2 * n)
                soluciones = []
                disposicion = [0] * n
                usado = [False] * (n + 1)
                disposicion[0] = 1
                usado[1] = True
                backtrack(n, es_primo, disposicion, usado, 1, soluciones)

                resultado.append(f"Case {i+1}:")
                resultado.append(generar_resultados(n, soluciones))
                
            for elemento in resultado:
                if type(elemento) == list:
                    for resultado in elemento:
                        print(resultado)

                else:
                    print(elemento)
                
            break

        except ValueError:
            print("Error: Ingrese un número válido.")

main()