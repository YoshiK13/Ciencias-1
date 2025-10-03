# Programa para optimizar el juego de la caja de dulces
# Reglas:
#1 Hay una caja de medidas M*M (Maximo 5 x 5)
#2 Si se toma un dulce la fila superior e inferiror se cierra
#3 Si se toma un dukce las casilas a su derecha e izquierda se cierran

# Por:
# Davidson Esfleider Sanchez Gordillo - 20231020183
# Diego Felipe Diaz Roa - 20201020147
# Dania Lizeth Guzmán Triviño - 20221020061
# Joshoa Alarcon Sanchez - 20221020013
  
# --------ALGORITMO--------

def contadorFilas(matriz):
    sumaMatriz = []
    for fila in matriz:
        sumaMatriz.append(sum(fila))

    return sumaMatriz

def voraz(array):
    respuesta = {"total":0, "posiciones":[]}
    sumaMaxima = [0] * len(array)
    tamanoLista = len(array)

    # Iniciar en primera casilla
    sumaMaxima[0] = array[0]
    sumaMaxima[1] = max(array[0], array[1])

    # hacer las posibles sumas de combinaciones
    for i in range(2, len(array)):
        sumaMaxima[i] = max(sumaMaxima[i-1], sumaMaxima[i-2] + array[i])

    # Consegir posiciones tomadas
    posiciones = []
    i = tamanoLista - 1
    while i >= 0:
        if i == 0:
            posiciones.append(0)
            break
        if sumaMaxima[i] == sumaMaxima[i-1]:
            i -= 1
        else:
            posiciones.append(i)
            i -= 2
    posiciones.reverse()

    respuesta["total"] = sumaMaxima[-1]
    respuesta["posiciones"] = posiciones

    return respuesta

# Consegir el maximo de dulces
def maximoDulces(matriz):
    # Datos
    dulcesFilas = contadorFilas(matriz)
    filasEscojidas = []
    maxDulces = 0
    dulcesFilasInverso = dulcesFilas[::-1]

    # Mapeo para el voraz inverso
    mapeoInversos = {}
    for i in range(tamanoMatrizFilas):
        mapeoInversos[str(i)] = 5 - i

    # Escojer que filas a trabajar
    if voraz(dulcesFilas)["total"] > voraz(dulcesFilasInverso)["total"] or voraz(dulcesFilas)["total"] == voraz(dulcesFilasInverso)["total"]:
        filasEscojidas = voraz(dulcesFilas)["posiciones"]

    else:
        filasEscojidas = [*map(mapeoInversos.get, voraz(dulcesFilasInverso)["posiciones"])]

    # Maximo de dulces posible
    for i in range(len(filasEscojidas)):
        filaInversa = matriz[filasEscojidas[i]][::-1]
        if voraz(matriz[filasEscojidas[i]])["total"] > voraz(filaInversa)["total"] or voraz(matriz[filasEscojidas[i]])["total"] == voraz(filaInversa)["total"]:
            maxDulces += voraz(matriz[filasEscojidas[i]])["total"]

        else:
            maxDulces += voraz(filaInversa)["total"]

    return maxDulces

# --------PROGRAMA--------

tamanoMatrizFilas = 0 
tamanoMatrizColumnas = 0
matriz = []
resultados = []

# Tomar datos
while True:

    tamanoMatriz = input()
    tamanoMatrizFilas, tamanoMatrizColumnas = tamanoMatriz.split()
    tamanoMatrizFilas = int(tamanoMatrizFilas)
    tamanoMatrizColumnas = int(tamanoMatrizColumnas)
    matriz = []

    if (tamanoMatrizFilas == 0) and (tamanoMatrizColumnas == 0):
        break

    for i in range(tamanoMatrizFilas):
        listaTemp = []

        listaTemp = input()
        listaTemp = list(map(int, listaTemp.split()))
        matriz.append(listaTemp)

    resultados.append(maximoDulces(matriz))

# Dar resultado
for elemento in resultados:
    print(elemento)